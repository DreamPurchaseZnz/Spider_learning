# Author: Nianzu Ethan Zheng
# Place: DongGuan
# Date: 2019-2-28
# Copyright

from bs4 import BeautifulSoup
import requests

class Accessor:
    def __init__(self):
        self.header = {'X-Requested-With': 'XMLHttpRequest',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                        'Referer': 'http://www.mzitu.com'}
        self.timeout = 10

    def access(self, url):
        source = requests.get(url, headers=self.header, timeout=self.timeout)
        source.encoding = "utf-8"
        soup = BeautifulSoup(source.text,"lxml")
        # print(soup.prettify())
        return soup

