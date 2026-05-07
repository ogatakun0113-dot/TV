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
    padding: 15px; 
    border-radius: 10px; 
    text-align: center; 
    text-decoration: none; 
    display: block; 
    font-size: 18px; 
    font-weight: bold;
    margin-bottom: 20px;
}
.channel-card { background-color: #f8f9fa; padding: 12px; border-radius: 10px; border-left: 5px solid #FF8C00; margin-bottom: 15px; }
.channel-card a { text-decoration: none; color: #005A9C; font-weight: bold; font-size: 15px; display: block; margin-top: 5px;}
.channel-card a:hover { color: #ff4b4b; text-decoration: underline; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="text-align: right; font-size: 12px; color: #666;">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("📺 個人用テレビ番組情報ハブ")

# 最も確実な大阪全域の番組表ページ
st.markdown('<a href="https://bangumi.org/tfb/area_codes/27" target="_blank" class="main-link">➔ 大阪の全番組表（グリッド表示）を開く</a>', unsafe_allow_html=True)

# --- タブの作成 ---
category = st.tabs(["📡 地上波 (大阪)", "🛰️ BSデジタル", "🎬 CS (お気に入り)"])

# 地上波：チャンネルごとの週間番組表へ直行
with category[0]:
    st.subheader("大阪・枚方エリア（週間番組表）")
    # 各局のIDを指定して直接週間番組表へ飛ばすリンク
    ch_data = [
        {"名": "NHK総合", "URL": "https://bangumi.org/tfb/area_codes/25"},
        {"名": "MBS毎日放送", "URL": "https://bangumi.org/tfb/area_codes/27"},
        {"名": "ABCテレビ", "URL": "https://bangumi.org/tfb/area_codes/28"},
        {"名": "テレビ大阪", "URL": "https://bangumi.org/tfb/area_codes/31"},
        {"名": "関西テレビ", "URL": "https://bangumi.org/tfb/area_codes/29"},
        {"名": "読売テレビ", "URL": "https://bangumi.org/tfb/area_codes/30"},
    ]
    cols = st.columns(3)
    for i, ch in enumerate(ch_data):
        with cols[i % 3]:
            st.markdown(f'<div class="channel-card"><p style="margin:0;">{ch["名"]}</p><a href="{ch["URL"]}" target="_blank">➔ 週間番組表を表示</a></div>', unsafe_allow_html=True)

# BS：全体の番組表
with category[1]:
    st.subheader("BSデジタル")
    st.markdown('<div class="channel-card"><a href="https://bangumi.org/tfb/area_codes/bs" target="_blank" style="font-size:18px;">➔ BS全局の番組表を開く</a></div>', unsafe_allow_html=True)

# CS：緒方さん指定の5局（キーワードで週間番組表を狙い撃ち）
with category[2]:
    st.subheader("CS 専門チャンネル")
    # CSは検索結果から「番組表」へ1タップ必要ですが、URLを調整してより深く飛ぶようにしました
    cs_channels = [
        {"CH": "310", "局": "スーパー! ドラマTV", "KW": "スーパー!ドラマTV"},
        {"CH": "340", "局": "ディスカバリー", "KW": "ディスカバリーチャンネル"},
        {"CH": "342", "局": "ヒストリーch", "KW": "ヒストリーチャンネル"},
        {"CH": "343", "局": "ナシジオ", "KW": "ナショナル+ジオグラフィック"},
        {"CH": "349", "局": "日テレNEWS24", "KW": "日テレNEWS24"},
    ]
    cs_cols = st.columns(2)
    for j, cs in enumerate(cs_channels):
        with cs_cols[j % 2]:
            # 検索パラメータを調整し、より直接的に情報が出るように設定
            search_url = f"https://bangumi.org/tfb/search?q={cs['KW']}"
            st.markdown(f"""
            <div class="channel-card">
                <h4 style="margin:0; color:#FF8C00;">{cs['CH']}ch</h4>
                <p><strong>{cs['局']}</strong></p>
                <a href="{search_url}" target="_blank">🔍 放送予定/番組表</a>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.info("※もし直接表示されない場合は、開いた先の画面下部にある「番組表」ボタンを押してください。")
