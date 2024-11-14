# ベースイメージとしてPythonを使用
FROM python:3.9

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN pip install matplotlib

# アプリケーションファイルをコンテナにコピー
COPY . .

# スクリプトを実行
CMD ["python", "security_saisentan.py"]

