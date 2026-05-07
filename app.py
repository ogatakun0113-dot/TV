import streamlit as st
from datetime import datetime

st.set_page_config(page_title="緒方専用・番組ハブ", layout="wide")

st.markdown("""
<style>
.main-btn { 
    background-color: #005A9C; 
    color: white !important; 
    padding: 20px; 
    border-radius: 12px; 
    text-align: center; 
    text-decoration: none; 
    display: block; 
    font-size: 20px; 
    font-weight: bold;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.sub-card { 
    background-color: #ffffff; 
    padding: 15px; 
    border: 1px solid #ddd;
    border-radius: 10px; 
    margin-bottom: 10px;
    border-left: 6px solid #FF8C00;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="text-align: right; font-size: 12px; color: #666;">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("📺 緒方専用・番組情報ハブ")

st.info("💡 最近のWebサイトは制限が厳しいため、以下のボタンから直接サイトを開くのが最も確実です。")

# --- 1. 最優先ボタン（全体の番組表） ---
st.markdown('<a href="https://bangumi.org/tfb/area_codes" target="_blank" class="main-btn">➔ Gガイド番組表を開く（地域・BS・CS選択）</a>', unsafe_allow_html=True)

st.write("")

# --- 2. 各ジャンルへのショートカット ---
tab1, tab2 = st.tabs(["📡 地上波・BS", "🎬 専門チャンネル(CS)"])

with tab1:
    st.subheader("放送波別リンク")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="sub-card"><strong>地上波（大阪）</strong><br><a href="https://bangumi.org/tfb/area_codes/27" target="_blank">➔ 番組表へ</a></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="sub-card"><strong>BSデジタル</strong><br><a href="https://bangumi.org/tfb/area_codes/bs" target="_blank">➔ 番組表へ</a></div>', unsafe_allow_html=True)

with tab2:
    st.subheader("お気に入りCS局（検索予約リンク）")
    st.write("※クリック後、画面下の「番組表」ボタンを押すと1週間分が表示されます。")
    cs_list = [
        ("310 スーパー!ドラマTV", "スーパー!ドラマTV"),
        ("340 ディスカバリー", "ディスカバリーチャンネル"),
        ("342 ヒストリーch", "ヒストリーチャンネル"),
        ("343 ナシジオ", "ナショナル ジオグラフィック"),
        ("349 日テレNEWS24", "日テレNEWS24")
    ]
    
    for ch, kw in cs_list:
        search_url = f"https://bangumi.org/tfb/search?q={kw}"
        st.markdown(f"""
        <div class="sub-card">
            <strong>{ch}</strong><br>
            <a href="{search_url}" target="_blank">➔ 放送予定を確認</a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.warning("【コツ】サイトが開いたら、画面を少し下にスクロールして「番組表」という青い文字（またはボタン）をタップしてください。それが一番確実な番組表への入り口です。")
