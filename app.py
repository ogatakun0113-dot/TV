import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="緒方専用・番組ハブ", layout="wide")

# 現在の日付を「YYYYMMDD」形式で自動取得
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
    margin-bottom: 25px;
}
.channel-card { 
    background-color: #f8f9fa; 
    padding: 15px; 
    border-radius: 10px; 
    border-left: 6px solid #FF8C00; 
    margin-bottom: 15px; 
    box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
}
.channel-card a { text-decoration: none; color: #005A9C; font-weight: bold; font-size: 16px; }
.channel-card a:hover { color: #ff4b4b; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="text-align: right; font-size: 12px; color: #666;">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("📺 緒方専用・日付自動連動番組表")
st.write(f"📅 本日の番組表日付: **{datetime.now().strftime('%Y年%m月%d日')}**")

# --- 1. CS番組表へ直行 (緒方さん提案のURL形式) ---
# 日付パラメータを自動計算して埋め込み
cs_direct_url = f"https://bangumi.org/epg/cs?broad_cast_date={today_str}"
st.markdown(f'<a href="{cs_direct_url}" target="_blank" class="main-link">➔ 本日のCS番組表（グリッド表示）を直接開く</a>', unsafe_allow_html=True)

# --- 2. タブエリア（地上波・BSも同様の仕組みで作成） ---
tab1, tab2 = st.tabs(["📡 地上波・BS (本日分)", "🎬 専門チャンネル個別"])

with tab1:
    st.subheader("地上波・BS（ダイレクト表示）")
    col1, col2 = st.columns(2)
    with col1:
        # 地上波(大阪:27)の直行URL
        gs_url = f"https://bangumi.org/epg/td?area_code=27&broad_cast_date={today_str}"
        st.markdown(f'<div class="channel-card"><strong>大阪・地上波</strong><br><a href="{gs_url}" target="_blank">➔ 本日の地上波番組表へ</a></div>', unsafe_allow_html=True)
    with col2:
        # BSの直行URL
        bs_url = f"https://bangumi.org/epg/bs?broad_cast_date={today_str}"
        st.markdown(f'<div class="channel-card"><strong>BSデジタル</strong><br><a href="{bs_url}" target="_blank">➔ 本日のBS番組表へ</a></div>', unsafe_allow_html=True)

with tab2:
    st.subheader("CS 注目局スケジュール")
    st.write("※各局の放送予定をピンポイントで確認できます。")
    cs_list = [
        ("310 スーパー!ドラマTV", "スーパー!ドラマTV"),
        ("340 ディスカバリー", "ディスカバリーチャンネル"),
        ("342 ヒストリーch", "ヒストリーチャンネル"),
        ("343 ナシジオ", "ナショナル+ジオグラフィック"),
        ("349 日テレNEWS24", "日テレNEWS24")
    ]
    
    cols = st.columns(2)
    for i, (ch_name, kw) in enumerate(cs_list):
        with cols[i % 2]:
            search_url = f"https://bangumi.org/tfb/search?q={kw}"
            st.markdown(f"""
            <div class="channel-card">
                <p style="margin:0;"><strong>{ch_name}</strong></p>
                <a href="{search_url}" target="_blank">🔍 放送予定を表示</a>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.info("💡 日付は自動更新されます。もし古い日付が出る場合はアプリを再読み込み（リロード）してください。")
