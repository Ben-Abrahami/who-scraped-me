import requests
import cloudscraper
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import json
from IPython.display import clear_output, display
import csv
import concurrent.futures

from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://free-proxy-list.net'
test = 'http://httpbin.org/ip'


def proxy_bitch():
    proxy_page = requests.get(URL).content
    soup = BeautifulSoup(proxy_page, 'html.parser')
    # print(soup.prettify())
    proxies = []
    for row in soup.find('table').find_all('tr')[1:]:
        tds = row.find_all('td')
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxies.append(str(ip) + ':' + str(port))
        except:
            continue
    print(proxies)
    return proxies

proxies = []


def test_proxies(proxy):
        try:
            response = requests.get(test, proxies={'http': proxy, 'https': proxy})
            print(response.json(), '- working')
            proxies.append(proxy)

        except:
            print('nope')
        return proxy


def testing(proxy):
    PROXY_STR = '194.233.73.108'

    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % PROXY_STR)

    service = Service(executable_path=ChromeDriverManager().install())

    chrome = webdriver.Chrome(options=options, service=service)
    chrome.implicitly_wait(20)
    chrome.get("https://www.whosampled.com/Eminem/My-Name-Is/")
    time.sleep(5)

if __name__ == '__main__':
    # proxy_lst = proxy_bitch()
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     executor.map(test_proxies, proxy_lst)

    testing(True)