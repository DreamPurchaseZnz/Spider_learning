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

root_url= "https://www.mzitu.com/"
number = jm.get_maximum(url="https://www.mzitu.com/page/2/",
                        expression=r"https://www.mzitu.com/page/(\d+)")
pages_url = jm.travel(represent="https://www.mzitu.com/page/{}/",
                      max_numbers=number)

page = 1
rs = f.screening(url="https://www.mzitu.com/",
                     expression=r"(https://www.mzitu.com/\d+)",
                     pre = "")
print(rs)
# for r in rs:
r = rs[1]
path = nm.name(r, expression=r"<title>(.+)</title>")
path_name = make_dir("./pictu", path)
print(path_name)
#
pu = jm.get_maximum(r, expression= r + "/(\d+)")
pl = jm.travel(represent=r+"/{}", max_numbers=pu)
for t, q in enumerate(pl):
    img = f.search(q)
    print(img)
    print(path_name)
    dl.download(img, name="pic_{}".format(t), loc=path_name)





