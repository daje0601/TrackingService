from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time

#우리가 원하는 사이트를 들어가서 사용자가 송장번호 입력할 수 있음 
baseUrl = 'https://th.kerryexpress.com/th/track/?track='
plusUrl = input("무엇을 검색할까요?:")


#입력된 송장번호로 검색 
url = baseUrl + quote_plus(plusUrl)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.find_element_by_class_name('ke-btn-search').click()
time.sleep(2)
current = driver.current_url
print(current)

#배송정보를 스크랩 
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
table = soup.find_all("div", {"class": "d-flex flex-column flex-sm-row flex-fill pl-3"})
times = soup.find_all("div", {"class":"text-sm-right d-flex flex-column py-2"})
for info in table:
    a = info.find("span", {"class":"header bold"})
    b = info.find("span", {"class": "text-1418 light"})
    print(a.get_text())
    print(b.get_text())

for time in times:
    c = time.find("span", {"class": "text-1418 light"})
    print(c.get_text())
driver.close()


# ##########################################################################################

# 1차 실패

# #입력된 송장번호로 검색 
# url = baseUrl + quote_plus(plusUrl)

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get(url)
# driver.find_element_by_class_name('ke-btn-search').click()
# current = driver.current_url
# print(current)

# #배송정보를 스크랩 
# request = requests.get(current)
# WebDriverWait(driver, 10)
# soup = BeautifulSoup(request.text, "html.parser")
# WebDriverWait(driver, 10)
# table = soup.find_all("div", {"class": "d-flex flex-column flex-sm-row flex-fill pl-3"})


# for info in table:
#     a = info.find("span", {"class":"text-1424"}).get_text()
#     b = info.find("span", {"class":"text-1418 light"}).get_text()
#     print(a)
#     print(b)
    
# driver.close()
##########################################################################################