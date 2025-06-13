# app.py
import streamlit as st
from sample_data import commands

st.title("🐍 Pythonコマンド検索アプリ")

query = st.text_input("コマンド名を入力してください（例: p）")

if query:
    results = {
        cmd: info
        for cmd, info in commands.items()
        if cmd.startswith(query)
    }

    if results:
        st.write("### 🔍 検索結果")
        for cmd, info in results.items():
            st.markdown(f"#### 🧩 `{cmd}`")
            st.write(f"**説明**: {info['description']}")
            st.code(info['example'], language='python')
    else:
        st.warning("一致するコマンドが見つかりませんでした。")
else:
    st.info("検索したいコマンドの頭文字を入力してください。")