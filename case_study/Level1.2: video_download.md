```
import re
import os
import time
import threading
from multiprocessing import Pool, cpu_count
import random

import requests
from bs4 import BeautifulSoup

HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'http://91porn.com'
}

DIR_PATH = r"E:\mp4"      # 下载图片保存路径


def download_mp4(mp_src):
    """
    download videos
    """
    try:
        req = requests.get(url=mp_src)
        filename = './1.mp4'
        with open(filename, 'wb') as f:
            f.write(req.content)
            print(filename)
    except Exception as e:
        print(e)


def save_pic(pic_src):
    """
    save pictures
    """
    try:
        img = requests.get(pic_src, headers=HEADERS, timeout=10)
        imgname = "pic_cnt_{}.jpg".format(1)
        with open(imgname, 'ab') as f:
            f.write(img.content)
            print(imgname)
    except Exception as e:
        print(e)


def random_ip():
    a = random.randint(1, 255)
    b = random.randint(1, 255)
    c = random.randint(1, 255)
    d = random.randint(1, 255)
    return (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))


def get_urls():
    """
    Get all the page urls
    """
    base_url = 'http://91porn.com/view_video.php?viewkey='
    page_urls = ['http://91porn.com/v.php?next=watch&page={cnt}'.format(cnt=cnt)
                 for cnt in range(1, 2)]
    print("Please wait for second ...")
    img_urls = []
    # page_url = page_urls[0]
    for page_url in page_urls:
        try:
            # print(bs.prettify())
            bs = BeautifulSoup(
                requests.get(page_url, headers=HEADERS, timeout=10).content,
                'lxml')
            result = re.findall(r'<a href="http://91porn.com/view_video.php\?viewkey=(.*)&amp;page=.*&amp;'
                                r'viewtype=basic&amp;category=.*?">', str(bs))
            img_url = [base_url + url for url in result]
            img_urls.extend(img_url)
        except Exception as e:
            print(e)
    return set(img_urls)


lock = threading.Lock()     # 全局资源锁


def urls_crawler(url):
    """ 爬虫入口，主要爬取操作
    """
    try:
        # url = img_url[0]
        HEADERS = {'Accept-Language': 'zh-CN,zh;q=0.9',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/51.0.2704.106 Safari/537.36',
                   'X-Forwarded-For': random_ip(), 'referer': url,
                   'Content-Type': 'multipart/form-data; session_language=cn_CN'}
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.encoding = 'utf-8'
        tittle = re.findall(r'<div id="viewvideo-title">(.*?)</div>', str(r.content, 'utf-8', errors='ignore'), re.S)
        try:
            t = tittle[0]
            tittle[0] = t.replace('\n', '')
            tittle = tittle[0].replace(' ', '')
        except IndexError:
            pass
        img_url = re.findall(r'poster="(.*?)"', str(r.content, 'utf-8', errors='ignore'))[0]
        video_url = re.findall(r'<source src="(.*?)" type=\'video/mp4\'>',
                               str(r.content, 'utf-8', errors='ignore'))[0]
        # print(folder_name.prettify())
        with lock:
            if make_dir(tittle):
                download_mp4(video_url)
                save_pic(img_url)

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
    urls = get_urls()
    pool = Pool(processes=cpu_count())
    try:
        delete_empty_dir(DIR_PATH)
        pool.map(urls_crawler, urls)
    except Exception as e:
        time.sleep(30)
        delete_empty_dir(DIR_PATH)
        pool.map(urls_crawler, urls)

```
