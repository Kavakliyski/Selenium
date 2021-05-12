from selenium import webdriver
import time
import unittest

class Logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='..\chromedriver\chromedriver.exe')

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')

        # login
        self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        self.driver.find_element_by_id('txtPassword').send_keys('admin123')

        self.driver.find_element_by_id('btnLogin').click()
        time.sleep(2)

        # logout
        self.driver.find_element_by_id('welcome').click()
        self.driver.find_element_by_link_text('Logout').click()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print('Done')

if __name__ == '__main__':
    unittest.main()
