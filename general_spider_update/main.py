# Author: Nianzu Ethan Zheng
# Place: Dongguan
# Date: 2019-2-23
# Copyright

from jumper import Jumper
from filter import Filter
from downloader import Downloader
from namer import Namer
from utils import make_dir, delete_empty_dir
import pickle

jm = Jumper()
f = Filter()
dl = Downloader()
nm = Namer()

############################################ Presetting################################################
root_url= "http://neikusp.ga/?m=art-type-id-17.html"
img_path = "./pic"
_ = make_dir(img_path, "")
delete_empty_dir(img_path)


############################################## main code##############################################
# number = 8
# pages_url = jm.travel(represent="http://neikusp.ga/?m=art-type-id-17-pg-{}.html",
#                       max_numbers=number)
# print(pages_url)
#
# page_content = []
# for page in pages_url:
#     rs = f.screening(url=page,
#                      expression=r"(/\?m=art-detail-id-\d+.html)",
#                      pre = "http://neikusp.ga")
#     page_content.extend(rs)
# pickle_save(value=page_content, name="page_content", path_name=img_path + "/page.pkl")
# print(page_content)

#################### Page/Item ######################################

# with open(img_path + "/page.pkl", 'rb') as fg:
#     page_content = pickle.load(fg)
# item_content = []
# for r in page_content[1:10]:
#     folder_name = nm.name(r)
#     urls = f.search(url=r)
#     item_content.append((folder_name, urls))
# pickle_save(value=item_content, name="item_content", path_name=img_path + "/item.pkl")
# print(item_content)

################################# Item/Download #########################

with open(img_path + "/item.pkl", 'rb') as fg:
    item_content = pickle.load(fg)
print(item_content)
for fn, urls in item_content:
    file_name = make_dir(img_path, fn)
    for n, img_url in enumerate(urls):
        dl.download(img_url, name="pic_{}".format(n), loc=file_name)





