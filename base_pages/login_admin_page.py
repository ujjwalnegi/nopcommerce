# this is base page for login admin page
# we will add locators and action methods in this page

from selenium.webdriver.common.by import By
from seleniumbase import Driver

from seleniumbase import BaseCase

 # SeleniumBase method to handle CAPTCHAs
class Login_Admin_Page:
    textbox_username_id = "Email"  # locator
    textbox_password_id = "Password"  # locator
    login_button_xpath = "//button[@type='submit']"  # locator
    logout_link_xpath = "//a[@href='/logout']"

    def __init__(self, driver):  # we are sending driver as parameter in the constructor of login admin base class
        self.driver = driver  # we can use it to access all class variables and methods, self keyword means it belongs to the class
        Driver(uc=True)

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()  # actionmethod
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)  # actionmethod

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()  # actionmethod
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)  # actionmethod

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()  # actionmethod

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.logout_link_xpath).click()