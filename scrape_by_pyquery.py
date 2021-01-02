from pyquery import PyQuery as pq

# select file to parse not only that you can select a URL and a text 
d = pq(filename='dp.html')

# convert relative url to absolute url with the argument
d.make_links_absolute('https://gihyo.jp/dp')

# get value of argument and then loop by values
for a in d('#listBook > li > a[itemprop="url"]'):

    # get a url
    url = d(a).attr('href')

    # get a title
    p = d(a).find('p[itemprop="name"]').eq(0)

    # convert the title to be without tags
    title = p.text()

    # output url and title
    print(url, title)
