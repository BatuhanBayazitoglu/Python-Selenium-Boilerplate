from selenium import webdriver
driver = webdriver.Chrome()

driver.get("http://localhost")
try:
    assert '404 Not Found' not in driver.page_source
except AssertionError:
    print('Error 404 Not Found')

driver.quit