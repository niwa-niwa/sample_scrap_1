import sys
import requests


# シェルから引数を受ける URLを期待している
url = sys.argv[1]

# URLで指定したWebページを取得する
r = requests.get(url)

# エンコーディングを標準エラー出力する
print(f'encoding: {r.encoding}', file=sys.stderr)

# デコードしたボディを標準出力
print(r.text)
