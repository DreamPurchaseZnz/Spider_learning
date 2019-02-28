# Author: Nianzu Ethan Zheng
# Place: ZheCheng County
# Date: 2019-2-23
# Copyright
import re
from accesser import Accessor

class Filter(Accessor):
    def screening(self, url,expression, pre):
        mains = []
        try:
            mains = re.findall(expression, str(self.access(url)))
        except Exception as e:
            print(e)

        target = []
        for m in mains:
            target.append(pre + m)
        return list(set(target))

    def search(self, url):
        img_url = []
        try:
            soup = self.access(url)
            tag_set = soup.find("div", class_="context").find("div", id="post_content").find("p").find_all("a")
            img_url = [tag.find("img")["src"] for tag in tag_set]
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
