import streamlit as st
import requests

st.title("Personal AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    st.chat_message(m["role"]).write(m["content"])

user = st.chat_input("Ask something")

if user:
    st.chat_message("user").write(user)
    st.session_state.messages.append({"role": "user", "content": user})

    r = requests.post("http://localhost:8000/chat", json={"message": user}).json()
    st.chat_message("assistant").write(r["response"])
    st.session_state.messages.append({"role": "assistant", "content": r["response"]})

