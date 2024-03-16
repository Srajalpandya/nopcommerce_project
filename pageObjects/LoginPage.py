from selenium import webdriver
class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver = driver


    def setUserName(self,username):
        self.driver.find_element("id", self.textbox_username_id).clear()
        self.driver.find_element("id", self.textbox_username_id).send_keys(username)


    def setPassword(self,password):
        self.driver.find_element("id", self.textbox_password_id).clear()
        self.driver.find_element("id", self.textbox_password_id).send_keys(password)


    def clickLogin(self):
        self.driver.find_element("xpath", self.button_login_xpath).click()


    def clickLogout(self):
        self.driver.find_element("link text", self.link_logout_linktext).click()