import lxml.html


# ファイルを読み込む URLを直接読み込むこともできるがURLからだと解析の制限があるらしい
tree = lxml.html.parse('dp.html')

# html要素を抽出
html = tree.getroot()

# すべてのa要素のURLを引数のURLの絶対パスにする
html.make_links_absolute('https://gihyo.jp/')

# ID=listBook配下のliのitemprop="url"がついているaをループで回す
for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
    
    # URLを取得
    url = a.get('href')

    # 書籍タイトルを取得
    p = a.cssselect('p[itemprop="name"]')[0]

    #テキストを取得
    title = p.text_content()

    # 標準出力
    print(url, title)
