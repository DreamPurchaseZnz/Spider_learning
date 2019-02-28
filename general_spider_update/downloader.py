# Author: Nianzu Ethan Zheng
# Place: ZheCheng County
# Date: 2019-2-23
# Copyright
import requests
import os
import time

class Downloader:
    def __init__(self):
        self.header = {'X-Requested-With': 'XMLHttpRequest',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                                     '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                       'Referer': 'http://www.mzitu.com'}

    def download(self, url, name, loc):
        try:
            time.sleep(0.01)
            img = requests.get(url, headers=self.header, timeout=10)
            img_name = "{}.jpg".format(name)
            with open(os.path.join(loc, img_name), 'ab') as f:
                f.write(img.content)
                print("Img {} have been saved".format(img_name))
        except Exception as e:
            print(e)

if __name__ == "__main__":
    d = Downloader()
    d.download(url="https://i.meizitu.net/2019/01/15a02.jpg", name="test", loc="./")