import streamlit as st

from config.constants import VERSION


def render_sidebar():

    with st.sidebar:

        st.markdown("# 👤 User")

        st.text_input(
            "Username",
            value="vijay",
            key="username"
        )

        st.divider()

        st.markdown("## 🧠 Memory")

        st.write("**Company**")
        st.caption("Make Market")

        st.write("**Location**")
        st.caption("Chennai")

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