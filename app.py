with category[2]:
    st.subheader("📡 CS放送 (専門チャンネル)")
    
    # 緒方さんの指定チャンネルリスト（修正版）
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
            <div class="channel-card" style="border-left: 5px solid #FF8C00; min-height: 150px;">
                <h3 style="color: #FF8C00; margin-bottom: 5px;">{cs['CH']}ch</h3>
                <p style="font-size: 16px;"><strong>{cs['局名']}</strong></p>
                <a href="{cs['URL']}" target="_blank" style="text-decoration: none; color: #005A9C;">📅 番組表を見る</a>
            </div>
            """, unsafe_allow_html=True)
            st.write("")

    st.info("💡 **ディスカバリー**や**ナシジオ**は、現場仕事のヒントになるようなドキュメンタリーも多いので、このアプリでチェックしておくと録画忘れがなくなりますね。")
