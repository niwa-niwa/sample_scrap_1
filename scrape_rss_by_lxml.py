import lxml.etree

# select what you want to parse a file
tree = lxml.etree.parse('rss2.xml')

# get an element of XML
root = tree.getroot()

# get an element of item that is a part of article
for item in root.xpath('channel/item'):

    # get title
    title = item.xpath('title')[0].text

    # get url
    url = item.xpath('link')[0].text

    # output title and url
    print(url, title)
