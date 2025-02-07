from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

# hw02_01 需要的 import
from langchain.schema import Document

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    # Load PDF using PyPDFLoader
    loader = PyPDFLoader(q1_pdf)
    doc1 = loader.load()

    # Text Splitter to split text
    txt_split = CharacterTextSplitter(chunk_overlap=0) 
    # pass

def hw02_2(q2_pdf):
    pass
