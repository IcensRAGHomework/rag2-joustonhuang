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
    pass
