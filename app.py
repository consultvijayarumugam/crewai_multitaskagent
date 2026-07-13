import streamlit as st

from services.chat_service import ChatService

from components.header.header import render_header
from components.common.sidebar import render_sidebar
from components.dashboard.dashboard import render_dashboard
from components.chat.chat_window import render_chat


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Customer Support Portal",
    page_icon="🤖",
    layout="wide"
)

# ==========================================================
# SESSION STATE
# ==========================================================

if "username" not in st.session_state:
    st.session_state.username = "vijay"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "questions" not in st.session_state:
    st.session_state.questions = 0

if "research_calls" not in st.session_state:
    st.session_state.research_calls = 0

if "memory_updates" not in st.session_state:
    st.session_state.memory_updates = 0

if "avg_time" not in st.session_state:
    st.session_state.avg_time = 0.0

# ==========================================================
# SERVICES
# ==========================================================

chat_service = ChatService()

# ==========================================================
# SIDEBAR
# ==========================================================

render_sidebar()

# ==========================================================
# HEADER
# ==========================================================

render_header()

# ==========================================================
# DASHBOARD
# ==========================================================

render_dashboard()

# ==========================================================
# CHAT
# ==========================================================

prompt = render_chat(st.session_state.messages)

# ==========================================================
# HANDLE MESSAGE
# ==========================================================

if prompt:

    # Show User Message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # AI Thinking

    with st.spinner("🤖 AI Agents are working..."):

        result = chat_service.ask(
            st.session_state.username,
            prompt
        )

    # Show AI Response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["research"]
        }
    )

    st.rerun()