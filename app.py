import streamlit as st
from datetime import datetime, timedelta

# ページ設定
st.set_page_config(page_title="緒方専用・番組ハブ", layout="wide")

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
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="text-align: right; font-size: 12px; color: #666;">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("📺 緒方専用・番組表ダイレクトハブ")

# --- カレンダー設置エリア ---
st.info("📅 見たい日付を下のカレンダーから選んでください")
# デフォルトで今日を選択、前後1週間の範囲で選べるように設定
selected_date = st.date_input("日付を選択", value=datetime.now(), help="カレンダーをタップして日付を選べます")

# 選択された日付を「YYYYMMDD」形式に変換
date_param = selected_date.strftime("%Y%m%d")
display_date = selected_date.strftime("%Y年%m月%d日")

st.success(f"✅ **{display_date}** の番組表リンクを作成しました")
st.write("")

# --- 各種番組表へのダイレクトボタン ---

# 1. 地デジ (大阪: ggm_group_id=42)
td_url = f"https://bangumi.org/epg/td?broad_cast_date={date_param}&ggm_group_id=42"
st.markdown(f'<a href="{td_url}" target="_blank" class="main-btn">📡 {display_date} の地デジ（大阪）</a>', unsafe_allow_html=True)

# 2. BS放送
bs_url = f"https://bangumi.org/epg/bs?broad_cast_date={date_param}"
st.markdown(f'<a href="{bs_url}" target="_blank" class="main-btn">🛰️ {display_date} のBS放送</a>', unsafe_allow_html=True)

# 3. CS放送
cs_url = f"https://bangumi.org/epg/cs?broad_cast_date={date_param}"
st.markdown(f'<a href="{cs_url}" target="_blank" class="main-btn">🎬 {display_date} のCS放送</a>', unsafe_allow_html=True)

st.markdown("---")
st.caption(f"※選択された日付パラメータ: {date_param}")
