#cd /usr/local/bin/ geckodriver içine koy
from selenium import webdriver
opts = webdriver.FirefoxOptions()
opts.set_headless()
# opts.headless = True
# opts.add_argument('headless')
driver = webdriver.Firefox(options=opts)

driver.get('http://python.org')
print(driver.title)
