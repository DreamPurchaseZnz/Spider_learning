# Comment
> the code is not completely, there are several obstacles in the way: download ts, and convert all the ts to mp4.

```
import re
import os
import time
import threading
from multiprocessing import Pool, cpu_count
import logging

import requests
from bs4 import BeautifulSoup

logging.basicConfig(filename='learning-spider.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')

HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'http://www.mzitu.com'
}

DIR_PATH = r"E:\mp4"      # 下载图片保存路径


def get_urls():
    """ 获取 mzitu 网站下所有图的 url
    """
    page_urls = ['http://www.jpiik.com/index.php?m=vod-type-id-5-pg-{cnt}.html'.format(cnt=cnt)
                 for cnt in range(2, 5)]
    print("Please wait for second ...")
    img_urls = []
    # page_url = page_urls[0]
    for page_url in page_urls:
        try:
            # print(bs.prettify())
            bs = BeautifulSoup(
                requests.get(page_url, headers=HEADERS, timeout=10).text,
                'lxml')
            result = re.findall(r"(?<=href=)\S+", str(bs))      # 匹配所有 urls
            img_url = [url.replace('"', "") for url in result]
            img_urlc = []
            for url in img_url:
                if "src" in url:
                    img_urlc.append(url)
            img_urlr = [url.replace("/index", 'http://www.jpiik.com/index') for url in img_urlc]
            img_urls.extend(img_urlr)
        except Exception as e:
            print(e)
    return set(img_urls)    # 利用 set 去重 urls


lock = threading.Lock()     # 全局资源锁


def urls_crawler(url):
    """ 爬虫入口，主要爬取操作
    """
    try:
        # url = img_urlr[0]
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.encoding = 'utf-8'
        folder_name = BeautifulSoup(r.text, 'lxml').title.contents[0]
        # print(folder_name.prettify())
        with lock:
            if make_dir(folder_name):
                # 套图里图片张数
                ps = BeautifulSoup(r.text, 'lxml').find_all("script")
                result = re.findall(r"(?<=mac_url=unescape)\S+", str(ps))  # 匹配所有 urls
                img_urls = [url.replace(r"'", "") for url in result]
                img_urls = [url.replace(r"(", "") for url in img_urls]
                img_urls = [url.replace(r");", "") for url in img_urls]
                img_urls = [url.replace(r'%3A', ":") for url in img_urls]
                img_urls = [url.replace(r'%2F', "/") for url in img_urls]
                all_url = img_urls[0].split('/')
                url_pre = '/'.join(all_url[:-1]) + '/'
                url_next = all_url[-1]
                # 获取m3u8文件
                m3u8_txt = requests.get(img_urls[0], headers={'Connection': 'close'})
                with open(url_next, 'wb') as m3u8_content:
                    m3u8_content.write(m3u8_txt.content)
                # 提取ts视频的url
                movies_url = []
                _urls = open(url_next, 'rb')
                for line in _urls.readlines():
                    if '.ts' in str(line.strip().decode('utf-8')):
                        movies_url.append(url_pre)
                    else:
                        continue
                urls_crawler_mp4(movies_url, folder_name)

    except Exception as e:
        print(e)


def urls_crawler_mp4(url, folder_name):
    """ 爬虫入口，主要爬取操作
    """
    try:
        with lock:
            if make_dir(folder_name):
                # 套图里图片张数
                download_movie(url, './')
    except Exception as e:
        print(e)


# 爬取ts视频
def download_movie(movie_url, _path):
    os.chdir(_path)
    print('>>>[+] downloading...')
    print('-' * 60)
    error_get = []

    for _url in movie_url:
        # ts视频的名称
        movie_name = _url.split('/')[-1][-6:]

        try:
            # 'Connection':'close' 防止请求端口占用
            # timeout=30    防止请求时间超长连接
            movie = requests.get(_url, headers = {'Connection':'close'}, timeout=60)
            with open(movie_name, 'wb') as movie_content:
                movie_content.writelines(movie)
            print ('>>>[+] File ' + movie_name + ' done')
        # 捕获异常，记录失败请求
        except:
            error_get.append(_url)
            continue
    # 如果没有不成功的请求就结束
    if error_get:
        print (u'共有%d个请求失败' % len(error_get))
        print ('-' * 60)
        download_movie(error_get, _path)
    else:
        print ('>>>[+] Download successfully!!!')


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
