from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import streamlit as st

groq_api_key = "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"

st.title("This is a fun GenAI Streamlit project using Groq")

options = ["French","Italian","Hindi","German"]
choice = st.selectbox("Choose your preferred language:",options)

model = ChatGroq(model="gemma2-9b-it",groq_api_key=groq_api_key)

generic_temp = "You are a Language translator,please translate the text into {language}"
prompt = ChatPromptTemplate.from_messages([
    ("system",generic_temp),
    ("user","{text}")
])

parser = StrOutputParser()

chain = prompt|model|parser

input_text = st.text_input("Enter your text input")

if input_text:
    st.write(chain.invoke({"language":choice,"text":input_text}))


