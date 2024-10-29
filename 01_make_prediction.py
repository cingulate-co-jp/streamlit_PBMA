import streamlit as st
import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd
import numpy as np

st.header(f'{st.session_state.category}の{st.session_state.prediction}の入力')


num_rows = 12  # 任意の行数を決定
data = np.empty(12)

# st.columns()を使って5つのボックスを横に並べる
cols = st.columns(num_rows)
df_index = ['Mar', 'Apr', 'May', 'Jun', 'Juy', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb']
for i, col in enumerate(cols):
    # 各列に小数を入力するボックスを追加
    value = col.number_input(f"{df_index[i]}", min_value=0, max_value=1000, value=0, step=1)
    data[i] = value

# データをデータフレームとして保存
df = pd.DataFrame(
    {
        'buyer_prediction': data
    }, 
    index=df_index,
)

st.write("入力されたデータフレーム")

if 'buyer_predicion' not in st.session_state:
    st.dataframe(df)
else:
    st.dataframe(st.session_state.buyer_prediction)

if st.button('Make prediction'):
    if 'buyer_predicion' not in st.session_state:
        st.session_state.buyer_prediction = df
    st.switch_page('pages/02_show_prediction.py')