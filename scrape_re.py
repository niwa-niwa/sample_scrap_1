import re
from html import unescape
from urllib.parse import urljoin


# ファイルから解析を行う

# ファイルを開きhtml変数に格納する
with open('dp.html') as f:
    html = f.read()

# 第二引数の文字列内で第一引数にヒットする要素をfindallで配列にする。それをfor文でループさせる
for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html, re.DOTALL):

    # urlを取得する
    url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html).group(1)

    # ルートドメインにくっつける
    url = urljoin('https://gihyo.jp/', url)

    # タイトルを取得
    title = re.search(r'<p itemprop="name".*?</p>', partial_html).group(0)

    # 改行を削除
    title = title.replace('<br/>','')

    # 余計なHTMLタグがある場合は削除
    title = re.sub(r'<.*?>','', title)

    # 文字参照をUnicode文字に変換
    title = unescape(title)

    # 標準出力
    print(url, title)
    