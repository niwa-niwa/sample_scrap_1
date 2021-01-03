import re
import time
from typing import Iterator
import requests
import lxml.html
import sqlite3


def main():

    # start session
    session = requests.Session()

    # scrape a index-page
    response = session.get('https://gihyo.jp/dp')

    # connect sqlite
    conn = sqlite3.connect('books.db')

    # ger a cursor
    c = conn.cursor()

    # if exist books table it would be deleted
    c.execute('DROP TABLE IF EXISTS books')

    # create table
    c.execute("""
        create table books (
            url text,
            title text,
            price text
        )
    """)

    # get detail pages from the index-page
    urls = scrape_list_page(response)

    # get a detail-page and then insert data to db
    for index, url in enumerate(urls):
        time.sleep(1)
        response = session.get(url)
        ebook = scrape_detail_page(response)
        print(index)
        c.execute('insert into books values (:url, :title, :price)', ebook)

    # commit to db
    conn.commit()

    # select table and columns
    c.execute('select * from books')

    # output columns
    for row in c.fetchall():
        print(row)

    conn.close


def scrape_list_page(response: requests.Response) -> Iterator[str]:
    """
        create genarator that has a detail-page
    """
    html = lxml.html.fromstring(response.text)
    html.make_links_absolute(response.url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        url = a.get('href')
        yield url


def scrape_detail_page(response: requests.Response) -> dict:
    """
        parse a detail-page
    """
    html = lxml.html.fromstring(response.text)

    ebook={
        'url':response.url,
        'title':html.cssselect('#bookTitle')[0].text_content(),
        'price':html.cssselect('.buy')[0].text.strip(),
        # 'content':[normalize_spaces(h3.text_content()) for h3 in html.cssselect('#content > h3')],
    }

    return ebook


def normalize_spaces(s: str) -> str:
    """
        delete necessary spaces
    """
    return re.sub(r'\s+', '', s).strip()


if __name__=='__main__':
    main()
