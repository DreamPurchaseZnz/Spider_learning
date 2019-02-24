# Author: Nianzu Ethan Zheng
# Place: ZheCheng County
# Date: 2019-2-23
# Copyright
from bs4 import BeautifulSoup
import requests
import re
from utils import pickle_load, pickle_save, check_dir


class Namer:
    def __init__(self):
        self.header = {'X-Requested-With': 'XMLHttpRequest',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                        'Referer': 'http://www.mzitu.com'}
        self.timeout = 10

    def name(self, url,expression):
        names = []
        try:
            bs = BeautifulSoup(
                requests.get(url, headers=self.header, timeout=self.timeout).text,
                "lxml"
            )
            names = re.findall(expression, str(bs))
        except Exception as e:
            print(e)
        return names[0]

if __name__ == "__main__":
    d = Namer()
    name = d.name(url="https://www.mzitu.com/166728", expression=r"<title>(.+)</title>")
    print(name)
