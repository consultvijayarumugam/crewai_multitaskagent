import streamlit as st

from services.chat_service import ChatService

st.set_page_config(
    page_title="Customer Support AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Customer Support AI")

st.write(
    "Multi-Agent Customer Support System powered by CrewAI"
)

chat_service = ChatService()

username = st.text_input(
    "Username",
    value="Vijay"
)

question = st.text_area(
    "Ask your question"
)

if st.button("Submit"):

    if question.strip() == "":

        st.warning("Please enter your question.")

    else:

        with st.spinner("Agents are working..."):

            result = chat_service.ask(
                username,
                question
            )

        st.success("Conversation Completed")

        st.subheader("🤖 Assistant Answer")

        st.write(
            result["assistant"]
        )

        st.subheader("🌐 Web Verified Answer")

        st.write(
            result["research"]
        )

        st.metric(
            "Execution Time",
            f'{result["execution_time"]} sec'
        )