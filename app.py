import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="個人用番組表", layout="wide")

# カスタムCSS
st.markdown("""
<style>
.channel-card { background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 5px solid #005A9C; min-height: 100px; margin-bottom: 15px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); }
.channel-card a { text-decoration: none; color: #005A9C; font-weight: bold; display: block; margin-top: 10px; }
.channel-card a:hover { color: #ff4b4b; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="text-align: right; font-size: 12px; color: #666;">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("📺 個人用テレビ番組情報ハブ")
st.write(f"本日の日付: {datetime.now().strftime('%Y年%m月%d日')}")

# --- サイドバー ---
st.sidebar.header("🌐 番組表提供先：Gガイド")
st.sidebar.info("Yahoo!テレビ終了に伴い、Gガイド公式へ切り替えました。")
st.sidebar.markdown("[Gガイド 公式TOP](https://bangumi.org/)")

# --- タブの作成 ---
category = st.tabs(["地上波 (大阪・枚方)", "BSデジタル", "CS (専門チャンネル)"])

# 1. 地上波タブ（Gガイド 大阪版）
with category[0]:
    st.subheader("📡 地上波 主要チャンネル")
    # 大阪エリアの各局番組表への直リンク
    ch_data = [
        {"CH": "1", "局名": "NHK総合1・大阪", "ID": "25"},
        {"CH": "2", "局名": "NHK Eテレ1・大阪", "ID": "26"},
        {"CH": "4", "局名": "毎日放送 (MBS)", "ID": "27"},
        {"CH": "6", "局名": "朝日放送テレビ (ABC)", "ID": "28"},
        {"CH": "7", "局名": "テレビ大阪 (TVO)", "ID": "31"},
        {"CH": "8", "局名": "関西テレビ (KTV)", "ID": "29"},
        {"CH": "10", "局名": "読売テレビ (YTV)", "ID": "30"},
    ]
    cols = st.columns(4)
    for i, ch in enumerate(ch_data):
        with cols[i % 4]:
            url = f"https://bangumi.org/lives/setup?area_code={ch['ID']}" # 簡易的に番組一覧へ
            # より詳細な個別リンクとしてGガイドの地域別URLを指定
            st.markdown(f"""
            <div class="channel-card">
                <h3 style="margin:0;">{ch['CH']}ch</h3>
                <p style="margin:5px 0;">{ch['局名']}</p>
                <a href="https://bangumi.org/tfb/area_codes/27" target="_blank">大阪の番組表を表示</a>
            </div>
            """, unsafe_allow_html=True)

# 2. BSタブ
with category[1]:
    st.subheader("🛰️ BSデジタル 番組表")
    st.markdown("""
    <div class="channel-card">
        <p>BS日テレ、BS朝日、BS-TBS、BSテレ東、BSフジ、NHK BSなど全てのBS番組を確認できます。</p>
        <a href="https://bangumi.org/tfb/area_codes/bs" target="_blank">👉 BS番組表(Gガイド)を開く</a>
    </div>
    """, unsafe_allow_html=True)

# 3. CSタブ (緒方さんの指定チャンネル)
with category[2]:
    st.subheader("📡 CS放送 (専門チャンネル)")
    # CSはGガイドの検索機能やチャンネル別表示が優秀です
    cs_channels = [
        {"CH": "310", "局名": "スーパー! ドラマTV", "KW": "スーパー!ドラマTV"},
        {"CH": "340", "局名": "ディスカバリーチャンネル", "KW": "ディスカバリー"},
        {"CH": "342", "局名": "ヒストリーチャンネル", "KW": "ヒストリーチャンネル"},
        {"CH": "343", "局名": "ナショナル ジオグラフィック", "KW": "ナショナル+ジオグラフィック"},
        {"CH": "349", "局名": "日テレNEWS24", "KW": "日テレNEWS24"},
    ]
    
    cs_cols = st.columns(3)
    for j, cs in enumerate(cs_channels):
        with cs_cols[j % 3]:
            # Gガイドの検索URLを利用して、その局の番組をすぐ出せるように工夫
            search_url = f"https://bangumi.org/tfb/search?q={cs['KW']}"
            st.markdown(f"""
            <div class="channel-card" style="border-left: 5px solid #FF8C00;">
                <h3 style="color: #FF8C00; margin:0;">{cs['CH']}ch</h3>
                <p style="margin:5px 0;"><strong>{cs['局名']}</strong></p>
                <a href="{search_url}" target="_blank">🔍 番組を確認</a>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.caption("※「Gガイド」のデータを利用して表示します。リンク先で詳細な時間帯を確認してください。")
