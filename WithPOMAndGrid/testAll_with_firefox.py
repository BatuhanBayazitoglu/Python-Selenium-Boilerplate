import unittest
from selenium import webdriver
from page import HomePage
from page import AboutPage
from locators import CommonPageLocators
from locators import AboutPageLocators

class TestPyOrgBase(unittest.TestCase):
    """
    TBD
    """
    #her test case biz browser açıyoruz (Time Consuming)
    def setUp(self):
        opts = webdriver.FirefoxOptions()
        opts.add_argument('headless')
        self.driver = webdriver.Remote(command_executor = 'http://10.0.1.123:4444/wd/hub', 
                        desired_capabilities = opts.to_capabilities())

    def tearDown(self):
        self.driver.quit()
        self.driver.stop_client()

class TestHome(TestPyOrgBase):
    """
    TBD
    """
    def setUp(self):
        #parentdan browser set up çekiyor
        super().setUp()
        #Home page e gideceğini veriyor
        self.home = HomePage(self.driver)

    @unittest.skip('skip this test for example')
    def test_TC001_py3_doc_button(self):
        self.home.hover_to(CommonPageLocators.DOC)
        self.home.assert_elem_text(CommonPageLocators.PY3_DOC_BUTTON, 'Python 3.x Docs')
        self.home.click(CommonPageLocators.PY3_DOC_BUTTON)
        assert self.driver.current_url == 'https://docs.python.org/3/'

    def test_TC002_blahblah_search(self):
        self.home.search_for('blahblah')
        self.home.assert_elem_text(CommonPageLocators.SEARCH_RESULT_LIST, 'No results found.')

    #with unit test
    def test_TC004_assert_title(self):
        self.assertEqual(self.home.driver.title, "Welcome to Python.org")

class TestAbout(TestPyOrgBase):
    """
    TBD
    """
    def setUp(self):
        super().setUp()
        self.about = AboutPage(self.driver)
    def test_TC003_upcoming_events_check(self):
        self.about.assert_elem_text(AboutPageLocators.UPCOMING_EVENTS, 'Upcoming Events')

    def test_TC005_assert_url(self):
        self.assertTrue('about' in self.about.driver.current_url)
    
if __name__ == '__main__':
    unittest.main()

