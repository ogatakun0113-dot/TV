import streamlit as st

# ページ設定（番組表を見やすくするためにワイドモードに固定）
st.set_page_config(page_title="緒方専用・番組ハブ", layout="wide")

st.markdown("""
<style>
.stTabs [data-baseweb="tab-list"] { gap: 24px; }
.stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; font-weight: bold; }
iframe { border: 2px solid #005A9C; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.title("📺 緒方専用・番組情報ハブ")
st.caption("※下のタブを切り替えると、アプリ内で直接番組表が表示されます。")

# --- タブの作成 ---
# 確実に表示される「Gガイド」の地域別・カテゴリ別ページを埋め込みます
tab1, tab2, tab3 = st.tabs(["📡 地上波 (大阪)", "🛰️ BSデジタル", "🎬 CS (専門チャンネル)"])

with tab1:
    st.subheader("大阪・地上波 番組表")
    # iframeを使って、Streamlitの中に番組表を埋め込みます
    # URLは最も安定しているGガイドの地域ページ
    st.components.v1.iframe("https://bangumi.org/tfb/area_codes/27", height=800, scrolling=True)

with tab2:
    st.subheader("BSデジタル 番組表")
    st.components.v1.iframe("https://bangumi.org/tfb/area_codes/bs", height=800, scrolling=True)

with tab3:
    st.subheader("CS 専門チャンネル案内")
    st.write("CSは局数が多いため、検索画面を表示します。")
    # CSは検索窓があるページを埋め込み、そこで「ディスカバリー」等を入力してもらう形が確実です
    st.components.v1.iframe("https://bangumi.org/tfb/search", height=800, scrolling=True)

st.markdown("---")
st.info("💡 アプリ内の画面でそのままスクロールやクリック操作が可能です。")
