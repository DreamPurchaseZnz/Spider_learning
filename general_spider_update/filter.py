# Author: Nianzu Ethan Zheng
# Place: ZheCheng County
# Date: 2019-2-23
# Copyright
import re
from accesser import Accessor
import os

class Filter(Accessor):
    def screening(self, url,expression, pre):
        mains = []
        try:
            mains = re.findall(expression, str(self.access(url)))
        except Exception as e:
            print(e)

        target = []
        for m in mains:
            target.append(pre+ m)
        return list(set(target))

    def search(self, url):
        img_url = []
        try:
            soup = self.access(url)
            tag_set = soup.find("div", class_="box pic_text").\
                find("div", class_="novelContent").\
                find("p").\
                find_all("img")
            img_url = [tag["src"] for tag in tag_set]
        except Exception as e:
            print(e)
        return img_url


if __name__ == "__main__":
    f = Filter()

    # rs = f.screening(url="http://neikusp.ga/?m=art-type-id-17-pg-2.html",
    #                  expression=r"(/\?m=art-detail-id-\d+.html)",
    #                  pre="http://neikusp.ga/")
    # [print(r) for r in rs]

    rs = f.search(url="http://neikusp.ga/?m=art-detail-id-10636.html")
    [print(r) for r in rs]
