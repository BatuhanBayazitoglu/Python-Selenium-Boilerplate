import unittest
from testAll_with_chrome import TestHome
from testAll_with_chrome import TestAbout

def suite():
    suite = unittest.TestSuite()

    #Home page tests
    suite.addTest(TestHome('test_TC001_py3_doc_button'))
    suite.addTest(TestHome('test_TC002_blahblah_search'))
    suite.addTest(TestHome('test_TC004_assert_title'))

    #About page tests
    suite.addTest(TestAbout('test_TC003_upcoming_events_check'))
    suite.addTest(TestAbout('test_TC005_assert_url'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = suite()
    runner.run(suite)
