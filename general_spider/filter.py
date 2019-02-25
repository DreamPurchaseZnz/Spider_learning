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
        return list(set(target))

    def search(self, url):
        img_url = []
        try:
            source = requests.get(url, headers=self.header, timeout=self.timeout)
            source.encoding = "utf-8"
            soup = BeautifulSoup(source.text,"lxml")
            # print(soup.prettify())
            # self-defined method
            tag_set = soup.find("div", class_="xs-details-content text-xs").find_all("img")
            img_url = [tag["src"] for tag in tag_set]
            # print(type(soup.find("div",class_="xs-details-content text-xs").find_all("img")[1]))
        except Exception as e:
            print(e)
        return img_url

    def search2(self, url):
        img_url = []
        try:
            source = requests.get(url, headers=self.header, timeout=self.timeout)
            source.encoding = "utf-8"
            soup = BeautifulSoup(source.text,"lxml")
            # print(soup.prettify())
            # self-defined method
            tag_set = soup.find("div", class_="context").find("div", id="post_content").find("p").find_all("a")
            img_url = [tag.find("img")["src"] for tag in tag_set]
            # print(type(soup.find("div",class_="xs-details-content text-xs").find_all("img")[1]))
        except Exception as e:
            print(e)
        return img_url


if __name__ == "__main__":
    f = Filter()
    # rs = f.screening(url="https://www.mzitu.com/",
    #                  expression=r"(https://www.mzitu.com/\d+)",
    #                  pre = "")
    # [print(r) for r in rs]
    #
    # rs = f.screening(url="https://www.mzitu.com/60704",
    #                  expression=r"(https://www.mzitu.com/60704/\d+)",
    #                  pre = "")
    # [print(r) for r in rs]
    """
    rs = f.search2(url="http://xinsijitv99.top/xem2wfcv.html")
    [print(r) for r in rs]
    """
    rs = f.screening(url="http://xinsijitv99.top/page/2",
                     expression=r"(http://xinsijitv99.top/\w*?.html)",
                     pre = "")
    [print(r) for r in rs]
