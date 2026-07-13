import streamlit as st


def render_stat_card(
    title: str,
    value,
    icon: str = "",
    help_text: str = ""
):

    with st.container(border=True):

        st.markdown(
            f"### {icon} {title}"
        )

        st.markdown(
            f"# {value}"
        )

        if help_text:
            st.caption(help_text)