# Headless 

## Chrome 

Install chromedriver: http://chromedriver.chromium.org/downloads

```python
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.set_headless()
# opts.headless = True
# opts.add_argument('headless')
driver = webdriver.Chrome(options=opts)
```

## Firefox 

Install geckodriver: https://github.com/mozilla/geckodriver/releases

```python
from selenium import webdriver
opts = webdriver.FirefoxOptions()
opts.set_headless()
# opts.headless = True
# opts.add_argument('headless')
driver = webdriver.Firefox(options=opts)
```



