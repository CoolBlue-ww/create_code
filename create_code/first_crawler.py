import os
import urllib.request
from lxml import etree


def create_request():
    URL = 'https://www.hongxiu.com/book/16543713804299404#Catalog'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/133.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=URL, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def get_link(content):
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@id="j-catalogWrap"]//ul/li/a/text()')
    href_list = tree.xpath('//div[@id="j-catalogWrap"]//ul/li/a/@href')
    links = []
    for i in range(len(name_list)):
        name = name_list[i]
        href = href_list[i]
        link = 'https://www.hongxiu.com' + href
        links.append((name, link))
    return links


def download_book(links):
    if not os.path.exists('./我在东京与都市传说为敌/'):
        os.makedirs('./我在东京与都市传说为敌/')
    for name, link in links:
        try:
            response = urllib.request.urlopen(link)
            content = response.read().decode('utf-8')
            tree = etree.HTML(content)
            p_list = tree.xpath('//div[contains(@class, "ywskythunderfont")]/p/text()')
            with open('./我在东京与都市传说为敌/' + name + '.txt', 'w', encoding='utf-8') as f:
                for p in p_list:
                    f.write(p + '\n')
        except Exception as e:
            print(f"Failed to download {name}: {e}")


def main():
    request = create_request()
    content = get_content(request)
    links = get_link(content)
    download_book(links)


if __name__ == '__main__':
    main()

# 第一个爬虫