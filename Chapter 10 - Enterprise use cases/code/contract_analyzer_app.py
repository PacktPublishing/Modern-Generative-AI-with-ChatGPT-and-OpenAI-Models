import streamlit as st
import openai
import pandas as pd
import sys
import re
import requests
import os
import numpy as np
import toml
from streamlit_chat import message
import streamlit as st
import openai
from openai.embeddings_utils import get_embedding, cosine_similarity
from openai.embeddings_utils import distances_from_embeddings
import os


with open('secrets.toml', 'r') as f:
    config = toml.load(f)


openai.api_type = "azure"
openai.api_key = config['OPENAI_API_KEY']
openai.api_base = config['OPENAI_API_BASE']
openai.api_version = "2022-12-01"


contract = """

This Contract for Services ("Agreement") is entered into as of [date], by and between Company A ("Company") and Company B ("Service Provider").
1.	Services Provided. Service Provider agrees to provide the following services to Company (the "Services"): The Service Provider agrees to provide consulting services to the Company in the field of marketing, including but not limited to market research, development of a marketing strategy, and implementation of marketing campaigns. The Service Provider shall provide reports and recommendations to the Company based on the results of the market research and the agreed-upon marketing strategy.
2.	Compensation. Company shall pay Service Provider the sum of 1.000.000 (One Million) $ for the Services. Payment shall be made on 15/9/2023.
3.	Term. This Agreement shall commence on 1/5/2023 and continue until 31/12/2023, unless earlier terminated by either party upon 30 days' prior written notice.
4.	Independent Contractor. Service Provider is an independent contractor, and nothing in this Agreement shall be construed as creating an employer-employee relationship, partnership, or joint venture between the parties.
5.	Confidentiality. Service Provider agrees to keep confidential any and all information learned or obtained as a result of providing the Services to Company. Service Provider shall not disclose such information to any third party without Company's prior written consent.
6.	Ownership of Work Product. Service Provider agrees that any and all work product produced in connection with the Services shall be the sole property of Company.
7.	Representations and Warranties. Service Provider represents and warrants that it has the necessary expertise and experience to perform the Services in a professional and workmanlike manner.
8.	Indemnification. Service Provider agrees to indemnify and hold harmless Company, its officers, directors, employees, and agents from and against any and all claims, damages, liabilities, costs, and expenses arising out of or in connection with the Services.
9.	Governing Law. This Agreement shall be governed by and construed in accordance with the laws of Italy without regard to conflicts of laws principles.
10.	Entire Agreement. This Agreement constitutes the entire agreement between the parties and supersedes all prior or contemporaneous negotiations, agreements, representations, and understandings between the parties, whether written or oral.
IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first above written.
[Signature block for Company]
[Signature block for Service Provider]

"""
st.set_page_config(
    page_title="Home",
    page_icon="📝",
)

st.header("Welcome to Contract Analyzer portal 📝")



st.subheader('Contract #371')
        
st.write(contract)

st.subheader('Key clauses extraction 🔍')

col1, col2 = st.columns(2)

with col1:
    request = st.selectbox(
    'Select the key clause you want to extract',
    ("What is the termination clause?", "what is the confidentiality clause?", "what is the compensation and the due date?", "what is the indemnification clause?"))
    

with col2:
    if request:
        completions = openai.Completion.create(
            engine="test1",
            prompt= contract + request,
            max_tokens=2000,
            n=1,
            stop=None,
            temperature=0,
        )
        response = completions.choices[0].text.strip()
        st.write('\n\n\n' + response)
        
        
st.subheader('Analyzing language 💬')
        
col3, col4 = st.columns(2)

with col3:
    user_input = st.text_input("You:", "")
    
with col4:
    if user_input:
        completions = openai.Completion.create(
            engine="test1",
            prompt= contract + user_input,
            max_tokens=2000,
            n=1,
            stop=None,
            temperature=0,
        )
        response = completions.choices[0].text.strip()
        st.write('\n\n\n' + response)
        
        
st.subheader('Flagging potential issues 🚩')
        
col5, col6 = st.columns(2)

with col5:
    request = st.selectbox(
    'Select the key clause you want to extract',
    ("Are there ambiguities?", "Are there conflicting terms?"))
    
with col6:
    if request:
        completions = openai.Completion.create(
            engine="test1",
            prompt= contract + request,
            max_tokens=2000,
            n=1,
            stop=None,
            temperature=0,
        )
        response = completions.choices[0].text.strip()
        st.write('\n\n\n' + response)
        
        
st.subheader('Contract Templates 🖋️')
        
col7, col8 = st.columns(2)

with col7:
    service_provider = st.text_input("Service provider:", "")
    client = st.text_input("Client:", "")
    services_description = st.text_input("Service description:", "")
    start_date = st.text_input("Start date:", "")
    duration = st.text_input("Duration:", "")

    
with col8:
    if st.button('Generate template'):
        completions = openai.Completion.create(
            engine="test1",
            prompt= f"Generate a Service Delivery Agreement with the following elements: Service Provider: {service_provider}, Client: {client}, Description of Services: {services_description}, Start Date: {start_date}, Duration: {duration}",
            max_tokens=2000,
            n=1,
            stop=None,
            temperature=0,
        )
        response = completions.choices[0].text.strip()
        st.write('\n\n\n' + response)
