import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestPythonOrg(unittest.TestCase):
    """
      Python org example test without pom
    """

    def setUp(self):
        chrome_options =  webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_TC001_py3_doc_button(self):
        self.driver.get("https://www.python.org")
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"documentation")))
        ActionChains(self.driver).move_to_element(element).perform()
        locator = "#documentation > ul > li.tier-2.super-navigation > p.download-buttons > a:nth-child(1)"
        py3button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,locator)))
        assert py3button.text == 'Python 3.x Docs'
        py3button.click()
        assert self.driver.current_url == 'https://docs.python.org/3/'

    def test_TC002_no_result_found(self):
        self.driver.get("https://www.python.org")
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"id-search-field")))
        element.send_keys('dsfesfwefwe')
        submit = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"submit")))
        submit.click()
        result_elem = self.driver.find_element_by_css_selector('#content > div > section > form > ul > p')
        assert result_elem.text == 'No results found.'

    def test_TC003_upcoming_events_check(self):
        self.driver.get("https://www.python.org/about")
        css_selector = '#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > h2'
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,css_selector)))
        assert element.text == 'Upcoming Events'
        
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
