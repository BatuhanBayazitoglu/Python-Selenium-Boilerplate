#java -jar selenium-server-standalone-3.9.1.jar -role hub -timeout 30
#java -jar selenium-server-standalone-3.9.1.jar  -role node -hub http://10.0.1.123:4444/wd/hub -timeout 30 -maxSession 5
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.set_headless()
driver = webdriver.Remote(command_executor = 'http://10.0.1.123:4444/wd/hub', desired_capabilities = opts.to_capabilities())
driver.get('http://python.org')
assert driver.title == 'Welcome to Python.org' 
print(driver.title)