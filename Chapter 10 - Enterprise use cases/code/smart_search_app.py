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




df = pd.read_pickle("medical_df.pkl")


def create_context(
    question, df, max_len=1800, size="ada"
):
    """
    Create a context for a question by finding the most similar context from the dataframe
    """

    q_embeddings = openai.Embedding.create(input=question, engine='embedding')["data"][0]["embedding"]

    # Get the distances from the embeddings
    df['distances'] = distances_from_embeddings(q_embeddings, df['embeddings'].values, distance_metric='cosine')


    returns = []
    cur_len = 0

    # Sort by distance and add the text to the context until the context is too long
    for i, row in df.sort_values('distances', ascending=True).iterrows():
        
        # Add the length of the text to the current length
        cur_len += row['n_tokens'] + 4
        
        # If the context is too long, break
        if cur_len > max_len:
            break
        
        # Else add it to the text that is being returned
        returns.append(row["text"])

    # Return the context
    return "\n\n###\n\n".join(returns)

def answer_question(
    df,
    engine="test1",
    question="how can I treat pneumonia?",
    max_len=1800,
    temperature = 0,
    size="ada",
    debug=False,
    max_tokens=1500,
    stop_sequence=None
):
    """
    Answer a question based on the most similar context from the dataframe texts
    """
    context = create_context(
        question,
        df,
        max_len=max_len,
        size=size,
    )
    # If debug, print the raw model response
    if debug:
        print("Context:\n" + context)
        print("\n\n")

    try:
        # Create a completions using the question and context
        response = openai.Completion.create(
            engine="test1",
            prompt=f"Answer the question based on the context below\n\n{context}\n\n---\n\nQuestion: {question}\nAnswer:",
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response["choices"][0]["text"].strip()
    except Exception as e:
        print(e)
        return ""
    
    
#st.set_page_config("My Personal Blog")

st.set_page_config(
    page_title="Home",
    page_icon="👨‍⚕️",
)


st.header("Welcome to Medical Smart Search👨‍⚕️")



#option = st.selectbox(
#    'Need some help?',
#    ('-','Translate this article', 'Summarize this article', 'Do a sentiment analysis on this article', 'Extract relevant #information'))



st.subheader('Enter your question here!', '🖊️')

query = st.text_area("Write your query here")
if query:
    response=answer_question(df, question=query)
    st.write(response)


st.write("")
