検索 = input("検索したい頭文字を入力して下さい")
if 検索 == "p" or 検索 == "P" :
    print("""***  print()  ***\nprintは画面に文字を出力します\n使用例　print(f"{変数名}が表示されます")""")
elif 検索 == "i" or 検索 == "I" :
    print("""***  input()  ***\ninputはユーザーからの入力を受け取ります\n使用例  input("何を検索しますか")\n\n
***  if, elif, else  ***\nifは条件分岐に使用します\n使用例　\nif score > 80:\nprint("Good")\nelif  score > 60:\nprint("You can do it!")\nelse\nprint("bad")\n\n
***  import  ***\nimportはモジュール読み込みに使用します\n使用例　\nimport math""")
elif 検索 == "l" or 検索 == "L" :
    print("""***  .lower()  ***\nlowerは文字を小文字に変換します\n使用例　"HELLO".lower()\n出力　hello\n\n***  .len()  ***\nlenは文字列やリストの長さを取得します\n使用例　len("python")\n出力　6""")
elif 検索 == "u" or 検索 == "U" :
    print("""***  .upper()  ***\nupperは文字を大文字に変換します\n使用例　"hello".upper()\n出力　HELLO""")
elif 検索 == "r" or 検索 == "R" :
    print("""***  .replace()  ***\nreplaceは文字を置換します\n使用例　"cold".replace("c","g")\n出力　gold""")
elif 検索 == "t" or 検索 == "T" :
    print("""***  type()  ***\ntypeはオブジェクトの型を返します\n使用例　type(123)""")
elif 検索 == "f" or 検索 == "F" :
    print("""***  for  ***\nforは繰返し実行に使用します\n使用例　\nfor i in range(5):\nprint(i)""")
elif 検索 == "o" or 検索 == "O" :
    print("""***  open()  ***\nopenはファイルを開く時に使用します\n使用例　f = open("data.txt","r")""")
else :
    print("まだそのコマンドは登録されていません")
