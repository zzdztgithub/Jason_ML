# -*- coding: utf-8 -*-
# 可以下载网站的sitemap
import re
from downloader import Downloader  # downloader的作用是下载网页内容

D = Downloader()

file1 = open('sitemaps.txt', 'a')
file2 = open('htmls.txt', 'a')


def crawl_sitemap(url):
    # download sitemap file
    sitemap = D(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        file1.write(link)
        file1.write('\n')
        html = D(link)
        file2.write(html)
        file2.write('\n')


crawl_sitemap('https://www.bloomberg.com/feeds/gadfly/sitemap_index.xml')  # 上面四个红色的sitemap，这里就放了一个，没有写到一起。

file1.close()
file2.close()