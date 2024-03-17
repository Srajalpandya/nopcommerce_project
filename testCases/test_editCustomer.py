import pytest
import time
import string
import random
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By

class Test_004_EditCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_editCustomer(self, setup):
        self.logger.info("************* Test_003_editCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Edit Customer Test **********")
        time.sleep(2)
        self.addcust = AddCustomer(self.driver)
        time.sleep(2)
        self.addcust.clickOnCustomersMenu()
        time.sleep(2)
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(2)

        self.addcust.clickOnEditCustomerDetails()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test12345")
        self.addcust.changePassword()
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 1")
        self.addcust.setGender("Female")
        self.addcust.setFirstName("Tina")
        self.addcust.setLastName("Kumari")
        self.addcust.setDob("7/05/1990")  # Format: D / MM / YYY
        self.addcust.setCompanyName("ToobusyQA")
        self.addcust.setAdminContent("This is for edit page testing.........")
        self.addcust.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Edit customer validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'The customer has been updated successfully.' in self.msg:
            assert True
            self.logger.info("********* Edit customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_EditCustomer_scr.png")  # Screenshot
            self.logger.error("********* Edit customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Edit customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
