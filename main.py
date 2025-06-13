from pyngrok import ngrok

# 一度ポート閉じておく（エラー回避用）
!pkill streamlit

# Streamlit アプリ起動
!streamlit run app.py &>/dev/null &

# ngrok 公開
# public_url = ngrok.connect(port=8501)
public_url = ngrok.connect(addr="8501", proto="http")
print("🔗 アプリにアクセス:", public_url)

