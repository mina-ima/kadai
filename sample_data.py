%%writefile sample_data.py
commands = {
    "print": {
        "description": "文字列や変数の値を出力します。",
        "example": 'print("こんにちは")  # => こんにちは'
    },
    "input": {
        "description": "ユーザーからの入力を受け取ります。",
        "example": 'name = input("名前を入力してください: ")'
    },
    "len": {
        "description": "リストや文字列などの長さを返します。",
        "example": 'len("Hello")  # => 5'
    },
    "list": {
        "description": "リストを作成します。",
        "example": 'my_list = list(range(3))  # => [0, 1, 2]'
    },
    "dict": {
        "description": "辞書（キーと値のペア）を作成します。",
        "example": 'my_dict = {"名前": "太郎", "年齢": 25}'
    },
    "range": {
        "description": "指定した範囲の連番を生成します。",
        "example": 'list(range(5))  # => [0, 1, 2, 3, 4]'
    },
    "type": {
        "description": "オブジェクトの型を返します。",
        "example": 'type(123)  # => <class \'int\'>'
    },
}