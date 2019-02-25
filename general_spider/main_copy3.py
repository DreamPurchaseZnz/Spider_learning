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

############################################ Presetting################################################
root_url= "http://xinsijitv99.top/"
img_path = "./pic5"
_ = make_dir(img_path, "")


############################################## main code##############################################
# number = 8
# pages_url = jm.travel(represent="http://xinsijitv99.top/page/{}",
#                       max_numbers=number)
#
# page_content = []
# for page in pages_url:
#     rs = f.screening(url=page,
#                      expression=r"(http://xinsijitv99.top/\w*?.html)",
#                      pre = "")
#     page_content.extend(rs)
# pickle_save(value=page_content, name="page_content", path_name=img_path + "/test.pkl")

#################### Page/Item ######################################

with open(img_path + "/test.pkl", 'rb') as fg:
    page_content = pickle.load(fg)

item_content = []
for r in page_content[1:10]:
    folder_name = nm.name(r)
    urls = f.search2(url=r)
    item_content.append((folder_name, urls))
pickle_save(value=item_content, name="item_content", path_name=img_path + "/test_item.pkl")

################################# Item/Download #########################
with open(img_path + "/test_item.pkl", 'rb') as fg:
    item_content = pickle.load(fg)

for fn, urls in item_content:
    file_name = make_dir(img_path, fn)
    for n, img_url in enumerate(urls):
        dl.download(img_url, name="pic_{}".format(n), loc=file_name)





