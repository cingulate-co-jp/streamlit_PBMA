import streamlit as st
import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd
import numpy as np

st.header('AI予測のダミーデータ')

df = pd.DataFrame(
    {
        'prediction': [110, 115, 110, 100, 105, 115, 120, 130, 125, 135, 110, 95]
    }, 
    index=['Mar', 'Apr', 'May', 'Jun', 'Juy', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb'],
)

df['upper'] = df['prediction']*1.08
df['lower'] = df['prediction']*0.95

st.session_state.df = df
# データフレームの表示
#st.subheader('DataFrame')
#st.dataframe(df)

st.header(f"{st.session_state.prediction}の入力")
num_rows = 12  # 任意の行数を決定
data = np.empty(12)

# st.columns()を使って5つのボックスを横に並べる
cols = st.columns(num_rows)

for i, col in enumerate(cols):
    # 各列に小数を入力するボックスを追加
    value = col.number_input(f"{df.index[i]}", min_value=0.0, max_value=1000.0, value=0.0, step=0.1)
    data[i] = value

# データをデータフレームとして保存
df['buyer_predict'] = data
st.write("入力されたデータフレーム")
st.dataframe(df)

# Matplotlibでデータを描画
st.subheader('Chart')

fig, ax = plt.subplots()
#AIデータ
ax.plot(
    df['prediction'], # median
    label='2023年度予測値',
    color='#434f98',
    alpha=1
)
ax.fill_between(
    df.index,
    df['lower'],
    df['upper'],
    facecolor='#434f98',
    alpha=0.15
)

# Buyer予測データ
ax.plot(
    df['buyer_predict'],
    color='#eca617',
    label=f'{st.session_state.prediction}',
    linestyle='--',
    linewidth=0.5,
    marker='x',
    markersize=10,
    markeredgewidth=3 # change marker(x) line width
)
ax.set_xticklabels(df.index)

ax.set_title(f'{st.session_state.category}')
ax.grid(alpha=0.5)
for spine in ax.spines.values():
    spine.set_color('#CDCCC9')

# StreamlitでMatplotlibのグラフを表示
st.pyplot(fig)
