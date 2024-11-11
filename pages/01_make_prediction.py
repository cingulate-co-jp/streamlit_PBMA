import base_page
import streamlit as st
import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd
import numpy as np

st.header(f'{st.session_state.category}の{st.session_state.prediction}の入力')

input_col, disp_col = st.columns(2)
df_index = ['3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月', '1月', '2月']

# 初期化: 各入力欄のセッションステートを初期値0で設定
for i in range(len(df_index)):
    if df_index[i] not in st.session_state:
        st.session_state[df_index[i]] = 0

with input_col:
    st.subheader("予測の入力")
    data = np.empty(12)
    for i in range(len(data)):
    # 各列に数値を入力するボックスを追加
        value = input_col.number_input(
            f"{df_index[i]}", 
            min_value=0, max_value=1000, step=1,
            value=st.session_state[df_index[i]],
            key=f"{df_index[i]}_input"
        )

        # 入力された値をセッションステートに保存して次回のデフォルトに
        if value != st.session_state[df_index[i]]:
            st.session_state[df_index[i]] = value

        data[i] = value

    # データをデータフレームとして保存
    df = pd.DataFrame(
        {
            'buyer_prediction': data
        }, 
        index=df_index,
    )

with disp_col:
    st.subheader("入力された予測")

    if 'buyer_predicion' not in st.session_state:
        st.dataframe(df)
        st.session_state.prediction_df = df
    else:
        st.dataframe(st.session_state.prediction_df)

if st.button('Make prediction'):
    if 'buyer_predicion' not in st.session_state:
        st.session_state.buyer_prediction = df
    st.switch_page('pages/02_show_prediction.py')