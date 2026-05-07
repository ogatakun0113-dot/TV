import streamlit as st
from datetime import datetime

st.set_page_config(page_title="個人用番組表", layout="wide")

st.markdown("""
<style>
.main-link { background-color: #005A9C; color: white !important; padding: 15px; border-radius: 10px; text-align: center; text-decoration: none; display: block; font-size: 18px; font-weight: bold; margin-bottom: 20px; }
.channel-card { background-color: #f8f9fa; padding: 12px; border-radius: 10px; border-left: 5px solid #FF8C00; margin-bottom: 15px; }
.channel-card a { text-decoration: none; color: #005A9C; font-weight: bold; font-size: 15px; display: block; margin-top: 5px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="text-align: right; font-size: 12px; color: #666;">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("📺 緒方専用・直行番組表ハブ")

# eoテレビの大阪・全チャンネル表示へ直行するリンク
st.markdown('<a href="https://eonet.jp/tv/guide/epg/index.php?area=01&broad=G" target="_blank" class="main-link">➔ 大阪の全番組表をいきなり開く</a>', unsafe_allow_html=True)

category = st.tabs(["📡 地上波 (大阪)", "🛰️ BSデジタル", "🎬 CS (専門5局)"])

# 地上波
with category[0]:
    st.subheader("大阪・地上波")
    # eoテレビの地域コードを利用
    st.markdown('<div class="channel-card"><a href="https://eonet.jp/tv/guide/epg/index.php?area=01&broad=G" target="_blank">➔ 地上波番組表（グリッド表示）へ直行</a></div>', unsafe_allow_html=True)

# BS
with category[1]:
    st.subheader("BSデジタル")
    st.markdown('<div class="channel-card"><a href="https://eonet.jp/tv/guide/epg/index.php?area=01&broad=B" target="_blank">➔ BS番組表（グリッド表示）へ直行</a></div>', unsafe_allow_html=True)

# CS：緒方さん指定の5局
with category[2]:
    st.subheader("CS 専門チャンネル（直行リンク）")
    # CSはeoテレビ内の各ジャンルページへ飛ばすことで確実に表示させます
    cs_channels = [
        {"名": "スーパー! ドラマTV", "URL": "https://eonet.jp/tv/guide/epg/index.php?area=01&broad=S&genre=01"},
        {"名": "ディスカバリー", "URL": "https://eonet.jp/tv/guide/epg/index.php?area=01&broad=S&genre=06"},
        {"名": "ヒストリーch", "URL": "https://eonet.jp/tv/guide/epg/index.php?area=01&broad=S&genre=06"},
        {"名": "ナシジオ", "URL": "https://eonet.jp/tv/guide/epg/index.php?area=01&broad=S&genre=06"},
        {"名": "日テレNEWS24", "URL": "https://eonet.jp/tv/guide/epg/index.php?area=01&broad=S&genre=04"},
    ]
    cols = st.columns(2)
    for i, cs in enumerate(cs_channels):
        with cols[i % 2]:
            st.markdown(f'<div class="channel-card"><p><strong>{cs["名"]}</strong></p><a href="{cs["URL"]}" target="_blank">➔ ジャンル別番組表を開く</a></div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("※eoテレビのシステムを利用しています。1クリックで番組表（グリッド表示）へ飛べるはずです。")
