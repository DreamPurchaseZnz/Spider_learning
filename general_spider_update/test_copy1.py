# Author: Nianzu Ethan Zheng
# Place: ZheCheng County
# Date: 2019-2-23
# Copyright

from jumper import Jumper
from filter import Filter
from downloader import Downloader
from namer import Namer
# Author: Nianzu Ethan Zheng
# Place: ZheCheng County
# Date: 2019-2-23
# Copyright

from jumper import Jumper
from filter import Filter
from downloader import Downloader
from namer import Namer
from utils import make_dir, pickle_save, pickle_load
import pickle

jm = Jumper()
f = Filter()
dl = Downloader()
nm = Namer()

# Presetting
root_url= "https://www.hhav15.com/arttypehtml/9.html"
img_path = "./pic3"

# main code
number = 8
pages_url = jm.travel(represent="https://www.hhav15.com/arttypehtml/9-{}.html",
                      max_numbers=number)

# page_content = []
# for page in pages_url:
#     rs = f.screening(url=page,
#                      expression=r"(/arthtml/\d+.html)",
#                      pre = "https://www.hhav15.com/")
#     page_content.extend(rs)

# pickle_save(value=page_content, name="page_content", path_name="./pic2/test.pkl")
with open("./pic2/test.pkl", 'rb') as fg:
    page_content = pickle.load(fg)

r = page_content[0]
folder_name = nm.name(r, expression=r"<title>(.+)</title>")
print(folder_name)
file_name = make_dir(img_path, folder_name)

gs = f.search(url=r)
print(gs)
#
# for t, q in enumerate(gs):
#     dl.download(q, name="pic_{}".format(t), loc=file_name)





