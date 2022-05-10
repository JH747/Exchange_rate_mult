from os import remove
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/exchangeList.nhn"

req = requests.get(url)

soup = BeautifulSoup(req.text, "html.parser")

#print(soup)

found_result = soup.find("div", attrs = {"class", "tbl_area"}).get_text()


tmp_list = found_result.split("\n")

tmp_list = list(filter(None, tmp_list))

tmp_list2 = []

for s in tmp_list:
    s = s.strip()
    if '\t' not in s:
        tmp_list2.append(s)

tmp_list2 = list(filter(None, tmp_list2))
print(tmp_list2)




