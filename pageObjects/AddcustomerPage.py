import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnEditCustomerDetail_xpath = "//tbody/tr[1]/td[7]/a[1][1]/i[1]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    btnChangePassword = "//button[@name='changepassword']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element("xpath", self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element("xpath", self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element("xpath", self.btnAddnew_xpath).click()

    def clickOnEditCustomerDetails(self):
        self.driver.find_element("xpath", self.btnEditCustomerDetail_xpath).click()

    def setEmail(self,email):
        self.driver.find_element("xpath", self.txtEmail_xpath).clear()
        self.driver.find_element("xpath", self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element("xpath", self.txtPassword_xpath).clear()
        self.driver.find_element("xpath", self.txtPassword_xpath).send_keys(password)

    def changePassword(self):
        self.driver.find_element("xpath",self.btnChangePassword).click()

    def setFirstName(self, fname):
        self.driver.find_element("xpath", self.txtFirstName_xpath).clear()
        self.driver.find_element("xpath", self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element("xpath", self.txtLastName_xpath).clear()
        self.driver.find_element("xpath", self.txtLastName_xpath).send_keys(lname)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element("id", self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element("id", self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element("id", self.rdMaleGender_id).click()



    def setDob(self, dob):
        self.driver.find_element("xpath", self.txtDob_xpath).clear()
        self.driver.find_element("xpath", self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element("xpath", self.txtCompanyName_xpath).clear()
        self.driver.find_element("xpath", self.txtCompanyName_xpath).send_keys(comname)

    def setCustomerRoles(self,role):
        self.driver.find_element("xpath", self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element("xpath", self.lstitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element("xpath", self.lstitemAdministrators_xpath)
        elif role=='Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element("xpath", "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element("xpath", self.lstitemGuests_xpath)
        elif role=='Registered':
            self.listitem = self.driver.find_element("xpath", self.lstitemRegistered_xpath)
        elif role=='Vendors':
            self.listitem = self.driver.find_element("xpath", self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element("xpath", self.lstitemGuests_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element("xpath", self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)



    def setAdminContent(self, content):
        self.driver.find_element("xpath", self.txtAdminContent_xpath).clear()
        self.driver.find_element("xpath", self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element("xpath", self.btnSave_xpath).click()

