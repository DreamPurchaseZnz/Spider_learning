
"""
Addition: IpPool methods
"""
import re
import os
import time
import threading
from multiprocessing import Pool, cpu_count

import requests
from bs4 import BeautifulSoup

HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'http://www.mzitu.com'
}

DIR_PATH = r"E:\gif"      # 下载图片保存路径


def get_urls():
    """ 获取 mzitu 网站下所有图的 url
    """
    page_urls = [''.format(cnt=cnt)
                 for cnt in range(2, 3)]
    print("Please wait for second ...")
    img_urls = []
    for page_url in page_urls:
        try:
            # print(bs.prettify())
            bs = BeautifulSoup(
                requests.get(page_url, headers=HEADERS, timeout=10).text, 'lxml')
            result = re.findall(r"((?<=<img src=)\S+)/>", str(bs))      # 匹配所有 urls
            img_url = [url.replace('"', "") for url in result]
            for url in img_url:
                if r"mp4" in url:
                    img_urls.append(url)
        except Exception as e:
            print(e)
    return set(img_urls)    # 利用 set 去重 urls


lock = threading.Lock()     # 全局资源锁


def urls_crawler(img_url):
    """ 爬虫入口，主要爬取操作
    """
    try:
        title = re.findall(r"https://pic.171vod.com/Uploads/vod/(\S+).mp4", string=str(img_url))
        title = title[0].replace('/', '-')
        if title is None:
            title = "unknown"
        with lock:
            if make_dir(title):
                save_pic(img_url, 1)
    except Exception as e:
        print(e)


def save_pic(pic_src, pic_cnt):
    """ 保存图片到本地
    """
    try:
        img = requests.get(pic_src, headers=HEADERS, timeout=10)
        imgname = "pic_cnt_{}.gif".format(pic_cnt + 1)
        with open(imgname, 'ab') as f:
            f.write(img.content)
            print(imgname)
    except Exception as e:
        print(e)


def make_dir(folder_name):
    """ 新建文件夹并切换到该目录下
    """
    path = os.path.join(DIR_PATH, folder_name)
    # 如果目录已经存在就不用再次爬取了，去重，提高效率。存在返回 False，否则反之
    if not os.path.exists(path):
        os.makedirs(path)
        print(path)
        os.chdir(path)
        return True
    print("Folder has existed!")
    return False


def delete_empty_dir(dir):
    """ 如果程序半路中断的话，可能存在已经新建好文件夹但是仍没有下载的图片的情况
    但此时文件夹已经存在所以会忽略该套图的下载，此时要删除空文件夹
    """
    if os.path.exists(dir):
        if os.path.isdir(dir):
            for d in os.listdir(dir):
                path = os.path.join(dir, d)     # 组装下一级地址
                if os.path.isdir(path):
                    delete_empty_dir(path)      # 递归删除空文件夹
        if not os.listdir(dir):
            os.rmdir(dir)
            print("remove the empty dir: {}".format(dir))
    else:
        print("Please start your performance!")     # 请开始你的表演


if __name__ == "__main__":
    # https://www.313sp.com/Html/60/index-{cnt}.html
    urls = get_urls()
    pool = Pool(processes=cpu_count())
    try:
        delete_empty_dir(DIR_PATH)
        pool.map(urls_crawler, urls)
    except Exception as e:
        time.sleep(30)
        delete_empty_dir(DIR_PATH)
        pool.map(urls_crawler, urls)
