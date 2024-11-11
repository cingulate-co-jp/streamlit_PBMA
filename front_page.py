import base_page
import streamlit as st

# 共通設定を適用
base_page.configure_page()

st.header('未来予測ファクトブック')

### バイヤーの名前を入力 ###
# 初期値は空欄
if 'name' not in st.session_state:
    st.session_state.name = ''

# ラベルを表示
st.markdown(
    """
    <p style='font-size:20px;'>
    名前を入力してください<br>
    姓名の間に半角スペースを入れてください（例：山田 太郎）
    </p>
    """,
    unsafe_allow_html=True
)

# 名前の入力欄
name = st.text_input(
    "", 
    value=st.session_state.name
)

# 入力が変更された場合、session_stateに保存
if name != st.session_state.name:
    st.session_state.name = name

# 入力せずに空欄の場合，警告出して，次に進めないようにする
if name == '':
    st.warning('名前を入力してください')
    button_disable = True
else:
    button_disable = False
    # 入力内容を表示
    st.write(f'入力バイヤー : {name}')


### 予測カテゴリを入力 ###
# カテゴリの初期値
if 'category' not in st.session_state:
    st.session_state.category = ''

# 選択肢の定義
categories = [
    '', '食器洗剤', '猫フード', 'ヘアケア', '大人オムツ', 'カップラーメン',
     '衣料洗剤', '犬フード', 'ヘアカラー', '基礎化粧品', '小型ペット',
     '芳香剤', 'ポケットウェット', '目薬（アイケア）', '発熱マスク', 'スナック'
]

# ラベルを表示
st.markdown(
    """
    <p style='font-size:20px;'>
    予測カテゴリを選択してください
    </p>
    """,
    unsafe_allow_html=True
)

# 対象カテゴリの選択
target_category = st.selectbox(
    '',
    categories,
    index=categories.index(st.session_state.category)
)

# 選択が変わった場合、セッションステートに保存
if target_category != st.session_state.category:
    st.session_state.category = target_category

# 選択せずに空欄の場合，警告を出して，次に進めないようにする
if st.session_state.category == '':
    st.warning('予測するカテゴリを選択してください')
    button_disable = True
else:
    button_disable = False
    st.write(f'今回予測するカテゴリは{st.session_state.category}です')


# 何を予測するのかの選択肢
options_prediction = ['', 'トレンド', '見込み', '対策後見込み']

if 'prediction' not in st.session_state:
    st.session_state.prediction = ''

# ラジオボタンのラベルにスタイルを適用
st.markdown(
    """
    <p style='font-size:20px; '>
    予測の種類を選んでください
    </p>
    """,
    unsafe_allow_html=True
)

prediction_type = st.radio(
    '',
    options_prediction,
)

if prediction_type != st.session_state.prediction:
    st.session_state.prediction = prediction_type

if st.session_state.prediction == '':
    st.warning('行う予測の種類を選んでください')
    button_disable = True
else:
    button_disable = False
    st.write(f'今回は{st.session_state.prediction}の予測を行います')


if st.button('Next page', disabled=button_disable):
    st.switch_page('pages/01_make_prediction.py')