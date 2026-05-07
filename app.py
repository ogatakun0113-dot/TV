import streamlit as st

from datetime import datetime



# ページ設定

st.set_page_config(page_title="個人用番組表", layout="wide")



# カスタムCSS

st.markdown("""

<style>

.main-link { 

    background-color: #005A9C; 

    color: white !important; 

    padding: 20px; 

    border-radius: 10px; 

    text-align: center; 

    text-decoration: none; 

    display: block; 

    font-size: 20px; 

    font-weight: bold;

    margin-bottom: 20px;

}

.channel-card { background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 5px solid #FF8C00; margin-bottom: 15px; }

.channel-card a { text-decoration: none; color: #005A9C; font-weight: bold; }

</style>

""", unsafe_allow_html=True)



st.markdown('<p style="text-align: right; font-size: 12px; color: #666;">開発/制作：緒方</p>', unsafe_allow_html=True)

st.title("📺 個人用テレビ番組情報ハブ")



# 最も確実な「番組表ページ」へのボタン

st.markdown('<a href="https://bangumi.org/tfb/area_codes" target="_blank" class="main-link">➔ 全体の番組表を開く（Gガイド）</a>', unsafe_allow_html=True)



st.info("💡 上のボタンから「大阪」や「BS/CS」を選択すると確実に表示されます。")



# --- タブの作成 ---

category = st.tabs(["📡 地上波 (大阪)", "🛰️ BSデジタル", "🎬 CS (専門ch)"])



with category[0]:

    st.subheader("大阪エリアの放送局")

    st.write("各局の検索結果（放送予定）へリンクします。")

    ch_list = ["NHK総合", "MBS毎日放送", "ABCテレビ", "テレビ大阪", "関西テレビ", "読売テレビ"]

    cols = st.columns(3)

    for i, name in enumerate(ch_list):

        with cols[i % 3]:

            url = f"https://bangumi.org/tfb/search?q={name}"

            st.markdown(f'<div class="channel-card"><p>{name}</p><a href="{url}" target="_blank">番組一覧を確認</a></div>', unsafe_allow_html=True)



with category[1]:

    st.subheader("BS放送")

    st.markdown('<a href="https://bangumi.org/tfb/area_codes/bs" target="_blank">👉 BSの番組一覧へ</a>', unsafe_allow_html=True)
