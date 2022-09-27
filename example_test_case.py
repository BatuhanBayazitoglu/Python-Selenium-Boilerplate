# Test case description:
# 1. Open a browser
# 2. Go ro python.org
# 3. Web page title contains word python

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.python.org/')
assert 'python' in driver.title.lower()
driver.execute_script("document.body.style.zoom = '1.5'")

time.sleep(3)

#expilict wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#elem = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "abltut")))
elem = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "about")))

driver.save_screenshot('screen_shot/ex_1.png')
driver.close()
driver.quit()
