import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="個人用番組表", layout="wide")

# カスタムCSS
st.markdown("""
<style>
.channel-card { background-color: #f0f2f6; padding: 15px; border-radius: 10px; border-left: 5px solid #005A9C; min-height: 120px; margin-bottom: 15px; }
.channel-card a { text-decoration: none; color: #005A9C; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="text-align: right; font-size: 12px; color: #666;">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("📺 個人用テレビ番組情報ハブ")
st.write(f"本日の日付: {datetime.now().strftime('%Y年%m月%d日')}")

# --- サイドバー ---
st.sidebar.header("🌐 番組表サイト（大阪）")
st.sidebar.markdown("[Yahoo!テレビ（大阪）](https://tv.yahoo.co.jp/listings/24/)")
st.sidebar.markdown("[Gガイド 番組表](https://bangumi.org/)")

# --- タブの作成 (ここでcategoryを定義しています) ---
category = st.tabs(["地上波 (枚方エリア)", "BSデジタル", "CS (専門チャンネル)"])

# 1. 地上波タブ
with category[0]:
    st.subheader("📡 地上波 主要チャンネル")
    ch_data = [
        {"CH": "1", "局名": "NHK総合", "URL": "https://tv.yahoo.co.jp/listings/24/?s=1"},
        {"CH": "2", "局名": "NHK Eテレ", "URL": "https://tv.yahoo.co.jp/listings/24/?s=2"},
        {"CH": "4", "局名": "毎日放送 (MBS)", "URL": "https://tv.yahoo.co.jp/listings/24/?s=4"},
        {"CH": "6", "局名": "朝日放送 (ABC)", "URL": "https://tv.yahoo.co.jp/listings/24/?s=6"},
        {"CH": "7", "局名": "テレビ大阪 (TVO)", "URL": "https://tv.yahoo.co.jp/listings/24/?s=7"},
        {"CH": "8", "局名": "関西テレビ (KTV)", "URL": "https://tv.yahoo.co.jp/listings/24/?s=8"},
        {"CH": "10", "局名": "読売テレビ (YTV)", "URL": "https://tv.yahoo.co.jp/listings/24/?s=10"},
    ]
    cols = st.columns(4)
    for i, ch in enumerate(ch_data):
        with cols[i % 4]:
            st.markdown(f'<div class="channel-card"><h3>{ch["CH"]}ch</h3><p>{ch["局名"]}</p><a href="{ch["URL"]}" target="_blank">番組表を開く</a></div>', unsafe_allow_html=True)

# 2. BSタブ
with category[1]:
    st.subheader("🛰️ BSデジタル注目局")
    st.info("BS日テレ / BS朝日 / BS-TBS / BSテレ東 / BSフジ / NHK BS 等")
    st.markdown("[BS放送の番組表全体を見る (Yahoo!)](https://tv.yahoo.co.jp/listings/bs/)")

# 3. CSタブ (緒方さんの指定チャンネル)
with category[2]:
    st.subheader("📡 CS放送 (専門チャンネル)")
    cs_channels = [
        {"CH": "310", "局名": "スーパー! ドラマTV", "URL": "https://tv.yahoo.co.jp/listings/34/?s=310"},
        {"CH": "340", "局名": "ディスカバリーチャンネル", "URL": "https://tv.yahoo.co.jp/listings/34/?s=340"},
        {"CH": "342", "局名": "ヒストリーチャンネル", "URL": "https://tv.yahoo.co.jp/listings/34/?s=342"},
        {"CH": "343", "局名": "ナショナル ジオグラフィック", "URL": "https://tv.yahoo.co.jp/listings/34/?s=343"},
        {"CH": "349", "局名": "日テレNEWS24", "URL": "https://tv.yahoo.co.jp/listings/34/?s=349"},
    ]
    cs_cols = st.columns(3)
    for j, cs in enumerate(cs_channels):
        with cs_cols[j % 3]:
            st.markdown(f"""
            <div class="channel-card" style="border-left: 5px solid #FF8C00;">
                <h3 style="color: #FF8C00;">{cs['CH']}ch</h3>
                <p><strong>{cs['局名']}</strong></p>
                <a href="{cs['URL']}" target="_blank">番組表を見る</a>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.caption("※番組表は外部サイト（Yahoo!テレビ）にジャンプします。")
