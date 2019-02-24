# Author: Nianzu Ethan Zheng
# Place: ZheCheng County
# Date: 2019-2-23
# Copyright

from jumper import Jumper
from filter import Filter
from downloader import Downloader
from namer import Namer
from utils import make_dir


jm = Jumper()
f = Filter()
dl = Downloader()
nm = Namer()

# Presetting
root_url= "https://www.mzitu.com/"
img_path = "./pic2"

# main code
number = jm.get_maximum(url="https://www.mzitu.com/page/2/",
                        expression=r"https://www.mzitu.com/page/(\d+)")
pages_url = jm.travel(represent="https://www.mzitu.com/page/{}/",
                      max_numbers=number)

for page in pages_url:
    rs = f.screening(url="https://www.mzitu.com/",
                     expression=r"(https://www.mzitu.com/\d+)",
                     pre = "")
    print(rs)
    for r in rs:
        path = nm.name(r, expression=r"<title>(.+)</title>")
        pn = make_dir(img_path, path)

        pu = jm.get_maximum(r, expression= r + "/(\d+)")
        pl = jm.travel(represent=r+"/{}", max_numbers=pu)
        for t, q in enumerate(pl):
            img = f.search(q)
            dl.download(img, name="pic_{}".format(t), loc=pn)





