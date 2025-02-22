import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.panpanfood.com/content/index/11'

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "PHPSESSID=mc4r3pg8pvstt9rincf4p47ca1",
    "priority": "u=0, i",
    "referer": "https://www.panpanfood.com/",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)
soup = BeautifulSoup(content, 'lxml')

name_list = soup.select('strong')
img_list = soup.select('div > ul > li > a > span > img')

for i in range(len(name_list)):
    name = name_list[i].get_text()
    src = img_list[i].get('src')
    URL = 'https://www.panpanfood.com' + src
    urllib.request.urlretrieve(url=URL, filename='./second_crawler的爬取文件/' + name + '.jpg')
