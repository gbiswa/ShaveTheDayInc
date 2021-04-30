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
        fname = "Days"
        lname = "Shaver"
        phoneo = "5558456547"
        email = "dayshaver@gmail.com"
        pword = "ISQA3900"

        # Open Chrome window, maximize, and set to default URL
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")
        time.sleep(3)

        # Click on the Signup button
        driver.find_element_by_xpath("//*[@id=\"navbarSupportedContent\"]/ul[2]/li[2]/a").click()
        time.sleep(3)

        # Enter First Name in the First Name field
        elem = driver.find_element_by_id("fname_id")
        elem.send_keys(fname)
        time.sleep(3)

        # Enter Last Name in the Last Name field
        elem = driver.find_element_by_id("lname_id")
        elem.send_keys(lname)
        time.sleep(3)

        # Enter Phone Number in the Phone Number field
        elem = driver.find_element_by_id("phone_no")
        elem.send_keys(phoneo)
        time.sleep(3)

        # Enter email in the email field
        elem = driver.find_element_by_id("email_id")
        elem.send_keys(email)
        time.sleep(3)

        # Enter password in the password field
        elem = driver.find_element_by_id("pword_id")
        elem.send_keys(pword)
        time.sleep(3)

        # Hit the return key to enter information
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

        # Click on the Login button
        driver.find_element_by_xpath("//*[@id=\"navbarSupportedContent\"]/ul[2]/li[3]/a").click()

        # Enter the user Email in the login screen
        elem = driver.find_element_by_id("email_form")
        elem.send_keys(email)
        time.sleep(3)

        # Enter the user Password in the login screen
        elem = driver.find_element_by_id("pword_form")
        elem.send_keys(pword)
        time.sleep(3)

        # Hit the enter key to login, which defaults to the homepage
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

        # Click on the Cart
        driver.find_element_by_xpath("//*[@id=\"navbarSupportedContent\"]/ul[2]/li[1]/a").click()
        time.sleep(3)

        # Click on the checkout button. If the checkout button can be clicked,login was successful.
        try:
            driver.find_element_by_xpath("/html/body/div/div/div/a")
            time.sleep(3)
            assert True

        # If the checkout button is not found, it means the user is not logged in (only shown to users)
        except NoSuchElementException:
            self.fail("User exists already?! We forgot to clean it up before testing, Oh noes!")
            assert False

def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()