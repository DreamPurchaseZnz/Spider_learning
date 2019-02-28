# Author: Nianzu Ethan Zheng
# Place: ZheCheng County
# Date: 2019-2-23
# Copyright
from accesser import Accessor
import re


class Namer(Accessor):
    def name(self, url):
        tl = []
        try:
            bs = self.access(url)
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