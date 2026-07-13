import streamlit as st
from pathlib import Path


ANSWER_FILE = Path("storage/answers.txt")


def render_answer_log():

    st.markdown("## 🤖 Latest Agent Output")

    if not ANSWER_FILE.exists():

        st.info("No answers available.")

        return

    content = ANSWER_FILE.read_text(
        encoding="utf-8"
    ).strip()

    if not content:

        st.info("No answers available.")

        return

    sections = content.split("=" * 60)

    latest = sections[-1].strip()

    st.text_area(
        "",
        latest,
        height=350
    )