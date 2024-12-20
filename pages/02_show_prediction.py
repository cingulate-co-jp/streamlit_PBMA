import base_page
import streamlit as st
import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd

base_page.configure_page()

st.header('AI予測とあなたの予測の結果')
df = pd.DataFrame(
    {
        'prediction': [110, 115, 110, 100, 105, 115, 120, 130, 125, 135, 110, 95]
    }, 
    index=['3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月', '1月', '2月'],
)

df['upper'] = df['prediction']*1.08
df['lower'] = df['prediction']*0.95

st.session_state.AI_prediction = df


df = pd.concat([st.session_state.prediction_df, st.session_state.AI_prediction],
          axis=1)
# Matplotlibでデータを描画
#st.subheader('Chart')

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
    df['buyer_prediction'],
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

st.subheader('入力されたデータ')
st.dataframe(df)

if st.button('Back to prediction'):
    st.switch_page('pages/01_make_prediction.py')