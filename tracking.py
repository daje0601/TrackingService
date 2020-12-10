from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import requests

#우리가 원하는 사이트를 들어가서 사용자가 송장번호 입력할 수 있음 
baseUrl = 'https://th.kerryexpress.com/th/track/?track='
plusUrl = "sly2000312465"
# input("무엇을 검색할까요?:")

#입력된 송장번호로 검색 
url = baseUrl + quote_plus(plusUrl)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.find_element_by_class_name('ke-btn-search').click()
current_url = driver.current_url
print(current_url)

#배송정보를 스크랩 
# request = requests.get(url)
# soup = BeautifulSoup(request.text, "html.parser")

# tracking_table = soup.find("div", {"class": "d-flex flex-column"})
# print(tracking_table)

# driver.close()
# # for row in tracking_table:
# #     columns = row.find("span", {"class": "text-1632"})
# #     print(columns)
