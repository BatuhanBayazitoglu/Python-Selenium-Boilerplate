from selenium import webdriver
#create hub
#java -jar selenium-server-standalone-3.9.1.jar -role hub
#create node
#java -jar selenium-server-standalone-3.9.1.jar -role node -hub 
driver = webdriver.Remote(command_executor='http://192.168.1.30:4444/wd/hub', desired_capabilities={'browserName':'chrome'})