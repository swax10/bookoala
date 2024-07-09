import streamlit as st
import pandas as pd
from agents.bookoala import Bookoala
from tools.books import books
from models.ollama_models import OllamaModel

st.title("🐨 Bookoala: A Book Recommendation AI")

with st.chat_message("assistant", avatar="🐨"):
    st.write("Hello! I'm Bookoala, a book recommendation AI. I can help you find books to read. 📚")

prompt = st.chat_input("Ask 🐨 for book recommendations:")

if 'modelConfig' not in st.session_state:
    st.session_state.modelConfig = {
        "tools": [books],
        "model_service": OllamaModel,
        "model_name": "llama3:instruct",
        "stop": "<|eot_id|>"
    }

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if "user" in message:
        with st.chat_message("user", avatar="😎"):
            st.write(message["user"])
    elif "assistant" in message:
        with st.chat_message("assistant", avatar="🐨"):
            if isinstance(message["assistant"], pd.DataFrame):
                st.dataframe(message["assistant"], use_container_width=True)
            else:
                st.write(message["assistant"])

if prompt:
    with st.chat_message("user", avatar="😎"):
        st.write(prompt)
    
    st.session_state.messages.append({"user": prompt})
    bookoala = Bookoala(tools=st.session_state.modelConfig["tools"], model_service=st.session_state.modelConfig["model_service"], model_name=st.session_state.modelConfig["model_name"], stop=st.session_state.modelConfig["stop"])
    response = bookoala.work(prompt)
    
    with st.chat_message("assistant", avatar="🐨"):
        if isinstance(response, pd.DataFrame):
            st.dataframe(response, use_container_width=True)
        else:
            st.write(response)
    
    st.session_state.messages.append({"assistant": response})