import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="緒方専用・番組ハブ", layout="wide")

# 現在の日付を「YYYYMMDD」形式で取得
today_str = datetime.now().strftime("%Y%m%d")

# カスタムCSS
st.markdown("""
<style>
.main-link { 
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
.channel-card { 
    background-color: #f8f9fa; 
    padding: 15px; 
    border-radius: 10px; 
    border-left: 6px solid #FF8C00; 
    margin-bottom: 15px; 
}
.channel-card a { text-decoration: none; color: #005A9C; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="text-align: right; font-size: 12px; color: #666;">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("📺 緒方専用・日付連動番組表")
st.write(f"📅 本日の自動取得URL日付: **{today_str}**")

# --- 1. メインボタン (CS番組表へ直行) ---
# 緒方さんの案を採用：日付を自動変数化
cs_direct_url = f"https://bangumi.org/epg/cs?broad_cast_date={today_str}"
st.markdown(f'<a href="{cs_direct_url}" target="_blank" class="main-link">➔ 本日のCS番組表（グリッド表示）を直接開く</a>', unsafe_allow_html=True)

st.write("")

# --- 2. タブエリア ---
tab1, tab2 = st.tabs(["📡 地上波・BS", "🎬 個別検索"])

with tab1:
    st.subheader("地上波・BS（本日分）")
    col1, col2 = st.columns(2)
    with col1:
        # 地上波(大阪)の直行URL
        gs_url = f"https://bangumi.org/epg/td?area_code=27&broad_cast_date={today_str}"
        st.markdown(f'<div class="channel-card"><strong>大阪・地上波</strong><br><a href="{gs_url}" target="_blank">➔ 本日の番組表</a></div>', unsafe_allow_html=True)
    with col2:
        # BSの直行URL
        bs_url = f"https://bangumi.org/epg/bs?broad_cast_date={today_str}"
        st.markdown(f'<div class="channel-card"><strong>BSデジタル</strong><br><a href="{bs_url}" target="_blank">➔ 本日の番組表</a></div>', unsafe_allow_html=True)

with tab2:
    st.subheader("キーワード検索")
    cs_list = [
        ("310 スーパー!ドラマTV", "スーパー!ドラマTV"),
        ("340 ディスカバリー", "ディスカバリーチャンネル"),
        ("342 ヒストリーch", "ヒストリーチャンネル"),
        ("343 ナシジオ", "ナショナル ジオグラフィック"),
        ("349 日テレNEWS24", "日テレNEWS24")
    ]
    for ch, kw in cs_list:
        search_url = f"https://bangumi.org/tfb/search?q={kw}"
        st.markdown(f'<div class="channel-card"><strong>{ch}</strong><br><a href="{search_url}" target="_blank">➔ 放送予定を確認</a></div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("※日付がズレている場合は、アプリを再読み込みしてください。")
