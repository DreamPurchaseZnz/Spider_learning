# Author: Nianzu Ethan Zheng
# Place: ZheCheng County
# Date: 2019-2-23
# Copyright

from accesser import Accessor
import re

class Jumper(Accessor):
    def get_maximum(self, url, expression):
        numbers = []
        try:
            bs = self.access(url)
            numbers = re.findall(expression, str(bs))
        except Exception as e:
            print(e)
        return max([int(num) for num in numbers])

    def travel(self, represent, max_numbers):
        urls = [represent.format(num) for num in range(2, max_numbers)]
        return urls

if __name__ == "__main__":
    j = Jumper()
    number = j.get_maximum(url="https://www.mzitu.com/page/2/",
                           expression=r"https://www.mzitu.com/page/(\d+)")
    print(number)
    urls = j.travel(represent="https://www.mzitu.com/page/{}/", max_numbers=number)
    print(urls)



