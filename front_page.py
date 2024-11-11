import base_page
import streamlit as st

from streamlit_google_oauth import google_oauth2_required

# 共通設定を適用
base_page.configure_page()

# 認証状態をセッションステートで管理
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

@google_oauth2_required
def main():
    user_id = st.session_state.user_id
    user_email = st.session_state.user_email 
    st.write(f"You're logged in {user_id}, {user_email}")
    st.session_state.authenticated = True

main()

if st.session_state.authenticated:
    st.write("認証に成功しました")
    if st.button("予測を開始する"):
         st.switch_page('pages/00_enter_information.py')