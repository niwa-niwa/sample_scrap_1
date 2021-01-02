import feedparser

# obtain rss feed
d = feedparser.parse('http://b.hatena.ne.jp/hotentry/it.rss')

# output url and title
for entry in d.entries:
    print(entry.link, entry.title)
    