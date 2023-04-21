import streamlit as st
import openai
import pandas as pd
import sys
import re
import requests
import os
import numpy as np
import openai
from langchain.llms import AzureOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationEntityMemory
from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from pypdf import PdfReader
from langchain.document_loaders import PyPDFLoader


with open('secrets.toml', 'r') as f:
    config = toml.load(f)



os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_BASE"] = config['OPENAI_API_BASE']
os.environ["OPENAI_API_KEY"] = config['OPENAI_API_KEY']


llm = AzureOpenAI(deployment_name="text-davinci-003")
embeddings = OpenAIEmbeddings(document_model_name="text-embedding-ada-002", chunk_size=1)

st.set_page_config(
    page_title="Home",
    page_icon="👨‍⚕️",
)


st.header("Welcome to Medical Smart Search👨‍⚕️")

with st.sidebar.expander(" 🛠️ Settings ", expanded=False):
    
    FILE = st.selectbox(label='File', options=['medical_paper.pdf'])

def get_answer(index, query):
    """Returns answer to a query using langchain QA chain"""

    docs = index.similarity_search(query)

    chain = load_qa_chain(llm)
    answer = chain.run(input_documents=docs, question=query)

    return answer

if FILE:
    loader = PyPDFLoader(FILE)
    pages = loader.load_and_split()
    faiss_index = FAISS.from_documents(pages, embeddings)

query = st.text_area("Ask a question about the document")

if query:
    
    docs = faiss_index.similarity_search(query, k=1)
    button = st.button("Submit")
    if button:
        st.write(get_answer(faiss_index, query))
