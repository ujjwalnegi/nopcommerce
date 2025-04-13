import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.custom_logger import Log_Maker
from base_pages.login_admin_page import Login_Admin_Page
from utilities.read_properties import Read_Config


class Test_01_Admin_Login():
    admin_page_url = Read_Config.get_admin_page_url()
    valid_username = Read_Config.get_valid_username()
    valid_password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log_generator() #we are calling static method from custom logger file it will return logger and it will get stored in this logger object

    @pytest.mark.sanity
    def test_title_verification(self, setup):# first test case
        self.logger.info("************test_title_verification*************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        actual_title = self.driver.title
        expected_title = "nopCommerce demo store. Login"
        if actual_title == expected_title:
            assert True
        else:
            self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_admin_login(self, setup):
        self.logger.info("************test_admin_login*************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.valid_username)
        self.admin_lp.enter_password(self.valid_password)
        self.admin_lp.click_login()

        act_dashboard_text = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Dashboard']").text
        expected_dashboard_text = "Dashboard"
        if act_dashboard_text == "Dashboard":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            assert False

    def test_invalid_admin_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.valid_password)
        self.admin_lp.click_login()
        error_message = self.driver.find_element(By.XPATH,
                                                 "//div[@class='message-error validation-summary-errors']").text()
        if error_message == "Login was unsuccessful. Please correct the errors and try again.":
            print("Error message")
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            print("No error message")
