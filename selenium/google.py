from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://th.kerryexpress.com/th/track/?track=")
elem = driver.find_element_by_css_selector("form-control tracking-input ke-placeholder-color")
elem.send_keys("sly2000312465")

# assert "Python" in driver.title

# elem.clear()

# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
