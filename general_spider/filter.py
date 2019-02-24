# Author: Nianzu Ethan Zheng
# Place: ZheCheng County
# Date: 2019-2-23
# Copyright
from bs4 import BeautifulSoup
import requests
import re
from utils import pickle_load, pickle_save, check_dir


class Filter:
    def __init__(self):
        self.header = {'X-Requested-With': 'XMLHttpRequest',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                        'Referer': 'http://www.mzitu.com'}
        self.timeout = 10

    def screening(self, url,expression, pre):
        mains = []
        try:
            bs = BeautifulSoup(
                requests.get(url, headers=self.header, timeout=self.timeout).text,
                "lxml"
            )
            mains = re.findall(expression, str(bs))
        except Exception as e:
            print(e)

        target = []
        for m in mains:
            target.append(pre + m)
        return set(target)

    def search(self, url):
        img_url = []
        try:
            img_url = BeautifulSoup(
                requests.get(url, headers=self.header, timeout=self.timeout).text,
                "lxml"
            ).find('div', class_="main-image").find('p').find('a').find('img')['src']
        except Exception as e:
            print(e)
        return img_url


if __name__ == "__main__":
    f = Filter()
    rs = f.screening(url="https://www.mzitu.com/",
                     expression=r"(https://www.mzitu.com/\d+)",
                     pre = "")
    [print(r) for r in rs]

    rs = f.screening(url="https://www.mzitu.com/60704",
                     expression=r"(https://www.mzitu.com/60704/\d+)",
                     pre = "")
    [print(r) for r in rs]
