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
    'Referer': 'http://scis.scichina.com/letter.html'
}

DIR_PATH = r"C:\Users\CYD\Desktop\Science China Letter"      # THE PATH


def get_urls():
    """
    """
    page_url = "http://scis.scichina.com/letter.html"
    print("Please wait for second ...")
    result = []
    try:
        bs = BeautifulSoup(
            requests.get(page_url, headers=HEADERS, timeout=10).text,
            'lxml')
        print(bs.prettify())
        result = re.findall(r'<a href="(\S+)" target="_blank">', str(bs))      # 匹配所有 urls
        print(result)
    except Exception as e:
        print(e)
    return set(result)    # 利用 set 去重 urls

lock = threading.Lock()     # 全局资源锁


def urls_crawler(url):
    """ 爬虫入口，主要爬取操作
    """
    try:
        with lock:
            print(url)
            name = url.split('/')[-1]
            print("{} is downloading".format(name))
            save_pic(url, name)
    except Exception as e:
        print(e)


def save_pic(pic_src, pic_nme):
    """ 保存图片到本地
    """
    try:
        img = requests.get(pic_src, headers=HEADERS, timeout=10)
        imgname = "article_{}".format(pic_nme)
        with open(imgname, 'ab') as f:
            f.write(img.content)
            print(imgname)
    except Exception as e:
        print(e)


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
    urls = get_urls()
    pool = Pool(processes=cpu_count())
    try:
        delete_empty_dir(DIR_PATH)
        pool.map(urls_crawler, urls)
    except Exception as e:
        time.sleep(30)
        delete_empty_dir(DIR_PATH)
        pool.map(urls_crawler, urls)
