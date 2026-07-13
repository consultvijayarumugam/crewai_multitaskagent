import streamlit as st

from config.constants import APP_NAME
from config.icons import AI


def render_header():

    left, right = st.columns([8, 2])

    with left:

        st.markdown(
            f"""
            # {AI} {APP_NAME}
            """
        )

        st.caption(
            "Powered by CrewAI • Multi-Agent • Long-Term Memory"
        )

    with right:

        st.success("🟢 Online")

    st.divider()