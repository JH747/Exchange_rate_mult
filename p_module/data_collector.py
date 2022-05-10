import requests
import time
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/exchangeList.nhn"

while True:
    time.sleep(5)

    req = requests.get(url)

    soup = BeautifulSoup(req.text, "html.parser")

    found_result = soup.find("div", attrs = {"class", "tbl_area"}).get_text()

    file1 = open("D:\\oh\\programming\\python_JAVA_multi\\data\\confirm.txt", 'w')
    file1.write(found_result)
    file1.close()

    file2 = open("D:\\oh\\programming\\python_JAVA_multi\\data\\analyzer_r.txt", 'r')

    for i in range(0, 5):
        line = file2.readline()
        print(line)
    file2.close()
