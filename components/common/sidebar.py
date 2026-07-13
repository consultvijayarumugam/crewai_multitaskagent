import streamlit as st

from config.constants import VERSION
from services.memory_service import MemoryService
from components.agents.answer_log import render_answer_log


memory = MemoryService()


def render_sidebar():

    with st.sidebar:

        username = st.text_input(
            "Username",
            value=st.session_state.get("username", "vijay"),
            key="username"
        )

        profile = memory.get_profile(username.lower())
        facts = memory.get_facts(username.lower())

        st.divider()

        st.markdown("## 🧠 Memory")

        if profile.get("name"):
            st.write("**Name**")
            st.caption(profile["name"])

        if profile.get("company"):
            st.write("**Company**")
            st.caption(profile["company"])

        if profile.get("location"):
            st.write("**Location**")
            st.caption(profile["location"])

        if profile.get("designation"):
            st.write("**Designation**")
            st.caption(profile["designation"])

        if profile.get("email"):
            st.write("**Email**")
            st.caption(profile["email"])

        if facts:

            st.write("**Facts**")

            for fact in facts:
                st.caption(f"• {fact}")

        st.divider()

        render_answer_log()

        st.divider()

        st.markdown("## ⚙️ Settings")

        st.toggle(
            "Dark Mode",
            value=False,
            disabled=True
        )

        st.button(
            "🗑 Clear Chat",
            use_container_width=True
        )

        st.button(
            "📄 Export History",
            use_container_width=True
        )

        st.divider()

        st.caption(f"Version {VERSION}")