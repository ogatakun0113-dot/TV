import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="緒方メディアハブ", layout="wide")

# スタイリッシュなダークテーマ風カスタムCSS
st.markdown("""
<style>
    /* 全体背景とフォント */
    .stApp {
        background-color: #0e1117;
    }
    
    /* ヘッダーとクレジット */
    .credit { text-align: right; font-size: 14px; color: #888; margin-bottom: -10px; }
    h1 { color: #ffffff; font-size: 42px !important; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); }
    
    /* メインボタンのデザイン */
    .main-btn { 
        background: linear-gradient(135deg, #005A9C 0%, #00a2ff 100%);
        color: white !important; 
        padding: 25px; 
        border-radius: 15px; 
        text-align: center; 
        text-decoration: none; 
        display: block; 
        font-size: 24px; 
        font-weight: bold;
        box-shadow: 0 8px 15px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .main-btn:hover { 
        transform: translateY(-5px);
        box-shadow: 0 12px 20px rgba(0,162,255,0.4);
        text-decoration: none;
        color: #ffffff !important;
    }
    
    /* ラジオボタン専用カラー */
    .radio-btn {
        background: linear-gradient(135deg, #FF8C00 0%, #FFA500 100%) !important;
    }
    .radio-btn:hover {
        box-shadow: 0 12px 20px rgba(255,140,0,0.4) !important;
    }

    /* カレンダー部分の調整 */
    .stDateInput {
        background-color: #262730;
        border-radius: 10px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="credit">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("📺 緒方メディアハブ")

# --- 日付選択エリア ---
# アプリ起動時に「現在の日付」を取得してデフォルト値にする
st.info("📅 カレンダーから日付を選ぶと、すべてのリンクが自動で書き換わります")
selected_date = st.date_input("番組表の日付を選択", value=datetime.now())

# 日付パラメータ生成
date_param = selected_date.strftime("%Y%m%d")
display_date = selected_date.strftime("%Y年%m月%d日")

st.markdown(f"### ✨ {display_date} の番組表")

# --- 各種番組表へのダイレクトリンク ---

# 2列構成で配置
col1, col2 = st.columns(2)

with col1:
    # 1. 地デジ (大阪: ggm_group_id=84)
    td_url = f"https://bangumi.org/epg/td?broad_cast_date={date_param}&ggm_group_id=84"
    st.markdown(f'<a href="{td_url}" target="_blank" class="main-btn">📡 地デジ（大阪）</a>', unsafe_allow_html=True)

    # 2. BS放送
    bs_url = f"https://bangumi.org/epg/bs?broad_cast_date={date_param}"
    st.markdown(f'<a href="{bs_url}" target="_blank" class="main-btn">🛰️ BS放送</a>', unsafe_allow_html=True)

with col2:
    # 3. CS放送
    cs_url = f"https://bangumi.org/epg/cs?broad_cast_date={date_param}"
    st.markdown(f'<a href="{cs_url}" target="_blank" class="main-btn">🎬 CS放送</a>', unsafe_allow_html=True)

    # 4. ラジオ番組表 (追加)
    radio_url = f"https://bangumi.org/epg/radio?broad_cast_date={date_param}&ggm_group_id=84"
    st.markdown(f'<a href="{radio_url}" target="_blank" class="main-btn radio-btn">📻 ラジオ番組表</a>', unsafe_allow_html=True)

st.markdown("---")
st.caption(f"選択中の日付データ: {date_param} / 現在時刻に合わせて自動更新されます。")
