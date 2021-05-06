import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class shave_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_shave(self):
        # Set the user and pwd to the default test profile
        user_email = "dayshaveinc@gmail.com"

        # Open Chrome window, maximize, and set to default URL
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")
        time.sleep(5)

        # Click on the Login button
        driver.find_element_by_xpath("//*[@id=\"navbarSupportedContent\"]/ul[2]/li[3]/a").click()
        time.sleep(3)

        # Click on ForgotPassword button
        driver.find_element_by_xpath("/html/body/div/div/div/form/div[3]/a").click()
        time.sleep(3)

        # Enter Email Address Into Forgot Email Block
        elem = driver.find_element_by_id("id_email")
        elem.send_keys(user_email)
        time.sleep(2)

        # Hit enter in order to enter your email for password reset
        elem.send_keys(Keys.RETURN)

        # Click on the checkout button. If the checkout button can be clicked,login was successful.
        try:
            driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/a").click()
            time.sleep(3)
            print("Forgot Password Link Worked!")
            assert True

        # If the checkout button is not found, it means the user is not logged in (only shown to users)
        except NoSuchElementException:
            self.fail("Login Failed - Something must be terribly wrong!")
            assert False

def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()
