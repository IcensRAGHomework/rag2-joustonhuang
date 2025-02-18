from langchain_community.document_loaders import PyPDFLoader # type: ignore
from langchain_text_splitters import (CharacterTextSplitter, # type: ignore
                                      RecursiveCharacterTextSplitter) # Text Splitter
# hw02_01 需要的 import
from langchain.schema import Document # type: ignore # Document class
import re

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    # Load PDF using PyPDFLoader
    loader = PyPDFLoader(q1_pdf)
    doc1 = loader.load()

    # Text Splitter to split text
    # txt_split = CharacterTextSplitter() # seems like doens't work
    txt_split = CharacterTextSplitter(chunk_overlap=0) # seems like this is the correct one

    # Split text
    chunks = []
    for i, page in enumerate(doc1):
        # 使用 text_splitter 進行每一頁的文本切割
        page_chunks = txt_split.split_text(page.page_content)
        chunks.extend(page_chunks)  # 收集所有的 chunks

    # 4. 取得最後一個 chunk，並返回檔名、頁數與內容
    last_chunk = chunks[-1] if chunks else None
    if last_chunk:
        return Document(
            page_content=last_chunk,
            metadata={"filename": q1_pdf, "page_number": len(doc1)}
        )
    else:
        return None    
    # pass

def hw02_2(q2_pdf):

    # Read PDF text
    loader = PyPDFLoader(q2_pdf)
    doc2 = loader.load()
    
    # Merge all pages' text
    full_text = "\n".join([doc.page_content for doc in doc2])

    # Find text before ch.1 (Introduction)
    intro_pattern = r"^(.*?)(第\s+[一二三四五六七八九十百零]+\s*章)"
    intro_match = re.match(intro_pattern, full_text, re.DOTALL)

    # Process Introduction if exists
    intro_text = intro_match.group(1).strip() if intro_match else ""
    full_text_wo_intro = full_text[len(intro_text):]  

    # Avoid tuple problem by using re.finditer()
    chapter_and_article_pattern = r"(第\s+[一二三四五六七八九十百零]+\s*章|第\s*\d+(-\d+)?\s*條)"
    matches = [m.group(0) for m in re.finditer(chapter_and_article_pattern + r"[\s\S]*?(?=" + chapter_and_article_pattern + r"|$)", full_text_wo_intro)]

    # Merge all matched chapters and articles
    combined_sections = [s.strip() for s in matches]

    # Split further with RecursiveCharacterTextSplitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,  # fix chunk_size
        chunk_overlap=0   # Avoid chunk overlap
    )

    # Split text into chunks
    chunks = []
    if intro_text:  # Insert introduction text if exists
        chunks.append(intro_text)
    
    for section in combined_sections:
        chunks.extend(splitter.split_text(section))

    # Print chunks
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:\n{chunk}\n")

    print(f"Successfully split into {len(chunks)} chunks.")

    return len(chunks)
    # pass


if __name__ == '__main__':
    result1 = hw02_1(q1_pdf)
    result2 = hw02_2(q2_pdf)
    # print(result1)
    print(result2) # 111