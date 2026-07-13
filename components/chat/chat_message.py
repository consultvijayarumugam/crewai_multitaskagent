import streamlit as st


def render_chat_message(role: str, message: str):

    if role == "user":

        with st.chat_message("user"):

            st.write(message)

    else:

        with st.chat_message("assistant"):

            st.write(message)