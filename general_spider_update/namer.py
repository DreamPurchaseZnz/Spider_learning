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

    def name(self, url):
        tl = []
        try:
            source = requests.get(url, headers=self.header, timeout=self.timeout)
            source.encoding = "utf-8"
            bs = BeautifulSoup(source.text,"lxml")
            tl = bs.find("title").get_text()
            tl = re.sub('[\/:*?"<>|]','-',tl)
        except Exception as e:
            print(e)
        if tl is None:
            tl = "others"
        return tl

if __name__ == "__main__":
    d = Namer()
    name = d.name(url="http://xinsijitv99.top/xem2wfcv.html")
    print(name)