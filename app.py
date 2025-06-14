import streamlit as st

# Pythonコマンドのデータ
commands = {
    "print": {
        "description": "文字列や変数の値を画面に出力します",
        "example": 'print("こんにちは世界！")\n# 出力: こんにちは世界！'
    },
    "input": {
        "description": "ユーザーからの入力を受け取ります",
        "example": 'name = input("お名前は？: ")\nprint(f"こんにちは、{name}さん！")'
    },
    "len": {
        "description": "文字列やリストの長さを取得します",
        "example": 'text = "Python"\nprint(len(text))  # 出力: 6'
    },
    "type": {
        "description": "変数の型を調べます",
        "example": 'number = 123\nprint(type(number))  # 出力: <class \'int\'>'
    },
    "range": {
        "description": "連続した数字を生成します",
        "example": 'for i in range(3):\n    print(i)\n# 出力: 0, 1, 2'
    },
    "list": {
        "description": "リスト（配列）を作成します",
        "example": 'fruits = ["りんご", "バナナ", "みかん"]\nprint(fruits[0])  # 出力: りんご'
    },
    "dict": {
        "description": "辞書（キーと値のペア）を作成します",
        "example": 'person = {"名前": "太郎", "年齢": 20}\nprint(person["名前"])  # 出力: 太郎'
    },
    "for": {
        "description": "繰り返し処理を行います",
        "example": 'for i in range(3):\n    print(f"{i}回目")'
    },
    "if": {
        "description": "条件分岐を行います",
        "example": 'score = 85\nif score >= 80:\n    print("優秀！")\nelse:\n    print("頑張ろう！")'
    },
    "open": {
        "description": "ファイルを開きます",
        "example": 'with open("test.txt", "r") as file:\n    content = file.read()\n    print(content)'
    }
}

# アプリのタイトル
st.title("🐍 Pythonコマンド検索アプリ")
st.write("初心者向けのPythonコマンド辞書だよ〜✨")

# 検索ボックス
query = st.text_input("🔍 コマンド名を入力してね（例: print, input, len）", placeholder="ここに入力...")

# 検索結果の表示
if query:
    # 部分一致で検索
    results = {
        cmd: info
        for cmd, info in commands.items()
        if query.lower() in cmd.lower()
    }
    
    if results:
        st.success(f"「{query}」で {len(results)} 件見つかったよ〜！")
        
        for cmd, info in results.items():
            with st.expander(f"📝 **{cmd}** - {info['description']}", expanded=True):
                st.write("**使い方の例：**")
                st.code(info['example'], language='python')
    else:
        st.warning(f"「{query}」に一致するコマンドが見つからなかったよ〜😅")
        st.info("💡 ヒント: print, input, len, type, range, list, dict, for, if, open などを試してみて！")

else:
    # 初期画面
    st.info("👆 上の検索ボックスに調べたいコマンド名を入力してね！")
    
    # 利用可能なコマンド一覧
    st.write("### 📚 利用可能なコマンド一覧")
    
    cols = st.columns(3)
    cmd_list = list(commands.keys())
    
    for i, cmd in enumerate(cmd_list):
        with cols[i % 3]:
            st.write(f"• **{cmd}**")

# サイドバーに使い方を表示
with st.sidebar:
    st.header("📖 使い方")
    st.write("""
    1. 上の検索ボックスにPythonコマンド名を入力
    2. 部分一致で検索できるよ！
    3. 各コマンドの説明と使用例が表示されるよ〜
    
    **例：**
    - `p` → print が見つかる
    - `in` → input が見つかる
    - `list` → list が見つかる
    """)
    
    st.header("🎯 このアプリについて")
    st.write("""
    Python初心者向けのコマンド検索アプリです。
    よく使うPythonの基本コマンドを簡単に調べられるよ〜！
    """) 