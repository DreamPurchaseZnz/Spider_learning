import re
import os
import time
import threading
from multiprocessing import Pool, cpu_count

import requests
from bs4 import BeautifulSoup
import random

_re_ip = re.compile(r'^\d{1,3}(\.\d{1,3}){3}$')

User_Agents = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) "
    "Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",]


class IpPool(object):
    def __init__(self, target_url, ip_number=4, foreign=True):
        if foreign:
            self.url = "http://www.xicidaili.com/wn/"
        else:
            self.url = "http://www.xicidaili.com/nn/"

        self.headers = {'User-Agent': User_Agents[0]}
        if "http" not in target_url:
            target_url = "http://" + target_url
        self.target_url = target_url
        self.ip_number = ip_number
        self.new_ip = self.get_ip()
        self.valid_ip = self.filter_ip()

    def ip_list(self):
        return self.valid_ip

    def get_ip(self):
        print("Start to obtain IPs")
        host_list = []
        port_list = []
        html = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(html.text, "lxml")
        for i in soup.find_all(string=_re_ip):
            host_list.append(i)
            port_list.append(i.parent.next_sibling.next_sibling.string)
        ip = ["%s%s"%(host, port) for host, port in zip(host_list, port_list)]
        return ip

    def filter_ip(self):
        valid_ip = []
        for ip in self.new_ip:
            try:
                header = {"User-Agent": random.choice(User_Agents)}
                proxy = {"http": "http://"+ ip}
                page = requests.get(self.target_url, allow_redirects=False, timeout=3,proxies=proxy, headers=header)
                print(ip)
                valid_ip.append("http://"+ip)
                if len(valid_ip) >= self.ip_number:
                    break
            except:
                print("[%s] not work.... check another one"%ip)
        return valid_ip

if __name__ == '__main__':
    pools = IpPool("https://www.baidu.com/?tn=81041078_1_hao_pg", ip_number=4, foreign=True).ip_list()
    print(pools)
