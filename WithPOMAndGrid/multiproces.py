from testAll_with_chrome import TestHome as TestHomeChrome
from testAll_with_chrome import TestAbout as TestAboutChrome
from testAll_with_firefox import TestHome as TestHomeFirefox
from testAll_with_firefox import TestAbout as TestAboutFirefox
import unittest
from multiprocessing import Pool
import time

def run_test(test_to_run):
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_to_run)

tests = [TestHomeChrome('test_TC001_py3_doc_button'),
        TestHomeFirefox('test_TC001_py3_doc_button'),
        TestHomeChrome('test_TC002_blahblah_search'),
        TestHomeFirefox('test_TC002_blahblah_search'),
        TestHomeChrome('test_TC004_assert_title'),
        TestHomeFirefox('test_TC004_assert_title'),
        TestAboutChrome('test_TC003_upcoming_events_check'),
        TestAboutFirefox('test_TC003_upcoming_events_check'),
        TestAboutChrome('test_TC005_assert_url'),
        TestAboutFirefox('test_TC005_assert_url')]

if __name__ == '__main__':
  #to see how much time we save running test in parallel
  start_time = time.time()
  runner = unittest.TextTestRunner(verbosity=2)
  with Pool(10) as p:
      p.map(run_test, tests)
  runtime_in_s = time.time() - start_time
  print('\n-------------------------------------')
  print('Total run time: {:.2f}s'.format(runtime_in_s))