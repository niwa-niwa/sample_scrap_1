from urllib.parse import urljoin
from bs4 import BeautifulSoup


# ファイルを開いてHTMLファイルとして解析
with open('dp.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

# ファイル内の抽出したい要素をselectの引数で渡す
for a in soup.select('#listBook > li > a[itemprop="url"]'):

    # hrefにURLを突っくけて絶対パスにする
    url = urljoin('https://gihyo.jp/dp', a.get('href'))

    # get a title
    p = a.select('p[itemprop="name"]')[0]

    # put title without tags in variable
    title = p.text

    # output the url and the title
    print(url, title)
