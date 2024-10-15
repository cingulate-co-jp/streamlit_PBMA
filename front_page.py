import streamlit as st

st.header('未来予測ファクトブック')

# Buyerの名前を入力
if 'name' not in st.session_state:
    st.session_state.name = '名前 太郎'
name = st.text_input(
    '名前を入力してください', 
    value=st.session_state.name
)
if name == '名前 太郎' or name == '':
    st.warning('名前を入力してください')
    button_disable = True
else:
    button_disable = False
    st.session_state.name = name
    st.write(f'Buyer : {name}')

# 予測カテゴリを入力
target_category = st.selectbox(
    '予測カテゴリ : ',
    ('', '食器洗剤', '猫フード', 'ヘアケア', '大人オムツ', 'カップラーメン',
     '衣料洗剤', '犬フード', 'ヘアカラー', '基礎化粧品', '小型ペット',
     '芳香剤', 'ポケットウェット', '目薬（アイケア）', '発熱マスク', 'スナック'),
     index=0
)

if 'category' not in st.session_state:
    st.warning('予測するカテゴリを選択してください')
    st.session_state.category = ''
    button_disable = True
else:
    button_disable = False
    if target_category == '':
        pass
    else:
        st.session_state.category = target_category
    st.write(f'今回予測するカテゴリは{st.session_state.category}です')


prediction = st.radio(
    '予測の種類を選んでください',
    ['トレンド', '見込み', '対策後見込み']
)
st.session_state.prediction = prediction
st.write(f'{prediction}の予測です')

if st.button('Next page', disabled=button_disable):
    st.write('次のページ読み込み中')
    st.switch_page('pages/01_AI_prediction.py')