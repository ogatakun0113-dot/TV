import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="個人用番組表", layout="wide")

# 現在の日付を「YYYYMMDD」形式で自動取得
today_str = datetime.now().strftime("%Y%m%d")

# カスタムCSS
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
    font-size: 22px; 
    font-weight: bold;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    margin-bottom: 15px;
}
.main-btn:hover { background-color: #004a80; text-decoration: none; }
.info-text { font-size: 14px; color: #666; margin-bottom: 20px; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="text-align: right; font-size: 12px; color: #666;">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("📺 緒方専用・番組表ダイレクトハブ")
st.write(f"📅 実行日: **{datetime.now().strftime('%Y年%m月%d日')}**")

st.markdown("---")

# 1. 地デジ (大阪: ggm_group_id=42)
td_url = f"https://bangumi.org/epg/td?broad_cast_date={today_str}&ggm_group_id=42"
st.markdown(f'<a href="{td_url}" target="_blank" class="main-btn">📡 地デジ（大阪）番組表を表示</a>', unsafe_allow_html=True)

# 2. BS放送
bs_url = f"https://bangumi.org/epg/bs?broad_cast_date={today_str}"
st.markdown(f'<a href="{bs_url}" target="_blank" class="main-btn">🛰️ BS放送 番組表を表示</a>', unsafe_allow_html=True)

# 3. CS放送
cs_url = f"https://bangumi.org/epg/cs?broad_cast_date={today_str}"
st.markdown(f'<a href="{cs_url}" target="_blank" class="main-btn">🎬 CS放送 番組表を表示</a>', unsafe_allow_html=True)

st.markdown("---")

# 補足：個別のCS局チェック用
with st.expander("🔍 特定のCS局をキーワード検索（参考）"):
    cs_list = [
        ("310 スーパー!ドラマTV", "スーパー!ドラマTV"),
        ("340 ディスカバリー", "ディスカバリーチャンネル"),
        ("342 ヒストリーch", "ヒストリーチャンネル"),
        ("343 ナシジオ", "ナショナル+ジオグラフィック"),
        ("349 日テレNEWS24", "日テレNEWS24")
    ]
    for ch, kw in cs_list:
        search_url = f"https://bangumi.org/tfb/search?q={kw}"
        st.write(f"・{ch}：[番組検索結果へ]({search_url})")

st.info("💡 ボタンを押すと別タブで「本日のグリッド番組表」が直接開きます。")
