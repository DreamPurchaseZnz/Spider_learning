# Author: Nianzu Ethan Zheng
# Place: ZheCheng County
# Date: 2019-2-23
# Copyright

from bs4 import BeautifulSoup
import requests
import re

class Jumper:
    def __init__(self):
        self.header = {'X-Requested-With': 'XMLHttpRequest',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                        'Referer': 'http://www.mzitu.com'}
        self.timeout = 10

    def get_maximum(self, url, expression):
        numbers = []
        try:
            bs = BeautifulSoup(
                requests.get(url, headers=self.header, timeout=self.timeout).text,
                "lxml"
            )
            numbers = re.findall(expression, str(bs))
        except Exception as e:
            print(e)
        return max([int(num) for num in numbers])

    def travel(self, represent, max_numbers):
        urls = [represent.format(num) for num in range(1, max_numbers)]
        return urls

if __name__ == "__main__":
    j = Jumper()
    number = j.get_maximum(url="https://www.mzitu.com/page/2/",
                           expression=r"https://www.mzitu.com/page/(\d+)")
    print(number)
    urls = j.travel(represent="https://www.mzitu.com/page/{}/", max_numbers=number)
    print(urls)



