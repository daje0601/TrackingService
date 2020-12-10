from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

#우리가 원하는 사이트를 들어가서 사용자가 송장번호 입력할 수 있음 
baseUrl = 'https://th.kerryexpress.com/th/track/?track='
plusUrl = input("무엇을 검색할까요?:")

#입력된 송장번호로 검색 
url = baseUrl + quote_plus(plusUrl)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.find_element_by_class_name('ke-btn-search').click()

#배송정보를 스크랩 
html = driver.page_source
soup = BeautifulSoup(html)

tracking = soup.select(".d-flex.flex-column")
for track_info in tracking:
    print(track_info.select(".d-flex.flex-column.flex-sm-row.flex-fill.pl-3"))
    print()

driver.close()