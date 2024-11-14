# 使用方法

* ①pythonファイルを作成
* ②Docker file を編集
  * →中身のファイル実行コマンドを、作成したpythonファイルに書き換える
* ③ビルド
`docker build -t my-python-app_ファイル名 .`
* ④runコマンド実行
`docker run -it --rm -v $(pwd):/app my-python-app`
