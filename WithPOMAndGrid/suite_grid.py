import unittest
import suite_all_tests_with_chrome
import suite_all_tests_with_firefox

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = unittest.TestSuite()
    suite_chrome = suite_all_tests_with_chrome.suite()
    suite_firefox = suite_all_tests_with_firefox.suite()
    suite.addTests(suite_chrome)
    suite.addTests(suite_firefox)
    runner.run(suite)