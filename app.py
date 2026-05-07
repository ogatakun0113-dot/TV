import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="個人用番組表", layout="wide")

# 現在の日付を「YYYYMMDD」形式で自動取得
today_str = datetime.now().strftime("%Y%m%d")

# カスタムCSS
st.markdown("""
<style>
.main-link { 
    background-color: #005A9C; 
    color: white !important; 
    padding: 20px; 
    border-radius: 10px; 
    text-align: center; 
    text-decoration: none; 
    display: block; 
    font-size: 20px; 
    font-weight: bold;
    margin-bottom: 20px;
}
.channel-card { background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 5px solid #FF8C00; margin-bottom: 15px; }
.channel-card a { text-decoration: none; color: #005A9C; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="text-align: right; font-size: 12px; color: #666;">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("📺 個人用テレビ番組情報ハブ")
st.write(f"📅 本日の日付: **{datetime.now().strftime('%Y年%m月%d日')}**")

# 最も確実な「今日の番組表ページ（大阪）」へのメインボタン
st.markdown(f'<a href="https://bangumi.org/epg/td?area_code=27&broad_cast_date={today_str}" target="_blank" class="main-link">➔ 大阪の今日の番組表を直接開く</a>', unsafe_allow_html=True)

st.info("💡 下のタブから、各放送波の「今日の番組表」へ1クリックでジャンプできます。")

# --- タブの作成 ---
category = st.tabs(["📡 地上波 (大阪)", "🛰️ BSデジタル", "🎬 CS (専門ch)"])

with category[0]:
    st.subheader("大阪エリアの放送局")
    # 地上波のダイレクトリンク
    td_url = f"https://bangumi.org/epg/td?area_code=27&broad_cast_date={today_str}"
    st.markdown(f'<div class="channel-card"><strong>地上波（大阪全域）</strong><br><a href="{td_url}" target="_blank">今日の番組表（格子表示）を表示</a></div>', unsafe_allow_html=True)

with category[1]:
    st.subheader("BS放送")
    # BSのダイレクトリンク
    bs_url = f"https://bangumi.org/epg/bs?broad_cast_date={today_str}"
    st.markdown(f'<div class="channel-card"><strong>BSデジタル</strong><br><a href="{bs_url}" target="_blank">今日のBS番組表（格子表示）を表示</a></div>', unsafe_allow_html=True)

with category[2]:
    st.subheader("緒方さんお気に入りCS局")
    # CSのダイレクトリンク
    cs_url = f"https://bangumi.org/epg/cs?broad_cast_date={today_str}"
    st.markdown(f'<div class="channel-card"><strong>CS放送 全局</strong><br><a href="{cs_url}" target="_blank">今日のCS番組表（格子表示）を表示</a></div>', unsafe_allow_html=True)
    
    st.write("---")
    st.write("各局ごとの詳細・検索（File Not Found対策用）")
    cs_channels = [
        {"CH": "310", "局名": "スーパー! ドラマTV", "KW": "スーパー!ドラマTV"},
        {"CH": "340", "局名": "ディスカバリーチャンネル", "KW": "ディスカバリー"},
        {"CH": "342", "局名": "ヒストリーチャンネル", "KW": "ヒストリーチャンネル"},
        {"CH": "343", "局名": "ナショナル ジオグラフィック", "KW": "ナショナル+ジオグラフィック"},
        {"CH": "349", "局名": "日テレNEWS24", "KW": "日テレNEWS24"},
    ]
    cs_cols = st.columns(2)
    for j, cs in enumerate(cs_channels):
        with cs_cols[j % 2]:
            search_url = f"https://bangumi.org/tfb/search?q={cs['KW']}"
            st.markdown(f"""
            <div class="channel-card">
                <h4 style="margin:0;">{cs['CH']}ch</h4>
                <p><strong>{cs['局名']}</strong></p>
                <a href="{search_url}" target="_blank">🔍 放送予定を確認</a>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.caption(f"※{today_str}付けのデータを取得するように設定されています。")
