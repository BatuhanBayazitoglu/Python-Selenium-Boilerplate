from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.python.org")

element = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"documentation")))
ActionChains(driver).move_to_element(element).perform()
locator = "#documentation > ul > li.tier-2.super-navigation > p.download-buttons > a:nth-child(1)"
py3button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,locator)))
assert py3button.text == 'Python 3.x Docs' 

driver.quit()