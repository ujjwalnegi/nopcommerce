import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.login_admin_page import Login_Admin_Page
from utilities.custom_logger import Log_Maker
from base_pages.Add_customer_page import Add_customer_page
from utilities.read_properties import Read_Config
from base_pages.Search_customers import Search_Customers


class Test_04_Search_Customer():
    admin_page_url = Read_Config.get_admin_page_url()
    valid_username = Read_Config.get_valid_username()
    valid_password = Read_Config.get_password()
    logger = Log_Maker.log_generator()

    @pytest.mark.sanity
    def test_search_customer(self, setup):
        self.logger.info("*************Test_03_Add_New_Customer started**********")
        self.driver = setup  # we have created setup fixture in conftest it will initialize the browser
        self.driver.implicitly_wait(20)  # page load might take time so we are using this
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(
            self.driver)  # already created all the login in test_admin_login.py we are reusing this here
        self.admin_lp.enter_username(self.valid_username)
        self.admin_lp.enter_password(self.valid_password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("*********Login Completed**********")
        self.logger.info("************Navigating to Customer Search Page***********")
        self.add_customer = Add_customer_page(
            self.driver)  # we have created object -> add_customer of class Add_customer_page #
        self.add_customer.click_customers()
        self.add_customer.click_customer_menu_option()
        self.logger.info("***********Search for Customer***********")
        self.search_customer = Search_Customers(self.driver)
        self.search_customer.enter_search_email("arthur_holmes@nopCommerce.com")
        self.search_customer.click_search_button()
        time.sleep(3)
        is_email_present = self.search_customer.search_customer_by_email("arthur_holmes@nopCommerce.com")
        if is_email_present == True:
            assert True
            self.driver.close()
        else:
            self.logger.info("*******Email didn't match********")
            self.driver.save_screenshot(".\\screenshots\\test_search_customer")
            self.driver.close()
            assert False



