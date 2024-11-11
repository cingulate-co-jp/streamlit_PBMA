import streamlit as st

# 共通設定: サイドバー非表示とwideレイアウト
def configure_page():
    st.set_page_config(layout="wide")
    hide_sidebar_style = """
        <style>
            [data-testid="stSidebar"] {
                display: none;
            }
        </style>
    """
    st.markdown(hide_sidebar_style, unsafe_allow_html=True)