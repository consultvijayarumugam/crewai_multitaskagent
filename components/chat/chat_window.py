import streamlit as st

from components.chat.chat_message import render_chat_message
from components.chat.chat_input import render_chat_input


def render_chat(messages):

    st.subheader("💬 AI Conversation")

    for message in messages:

        render_chat_message(

            message["role"],

            message["content"]

        )

    return render_chat_input()