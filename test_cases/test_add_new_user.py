import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.login_admin_page import Login_Admin_Page
from utilities.custom_logger import Log_Maker
from base_pages.Add_customer_page import Add_customer_page
from utilities.read_properties import Read_Config


class Test_03_Add_New_Customer():
    admin_page_url = Read_Config.get_admin_page_url()
    valid_username = Read_Config.get_valid_username()
    valid_password = Read_Config.get_password()
    logger = Log_Maker.log_generator()

    def test_add_new_customer(self, setup):
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

        self.add_customer = Add_customer_page(
            self.driver)  # we have created object -> add_customer of class Add_customer_page #
        self.add_customer.click_customers()  # now using the object we can call all the methods we have created in base page
        self.add_customer.click_customer_menu_option()
        self.add_customer.click_add_new_button()
        self.logger.info("************* Providing Customer Info ***************")
        email = generate_random_email()
        self.add_customer.enter_email(email)
        self.add_customer.enter_password("Test@123")
        self.add_customer.enter_first_name("Ujjwal")
        self.add_customer.enter_lastname("Negi")
        self.add_customer.select_gender("Female")
        self.add_customer.enter_company_name("XYZ")
        self.add_customer.select_tax_exempt_checkbox()
        # self.add_customer.select_newsletter_option()
        self.add_customer.select_customer_role()
        self.add_customer.select_manager_of_vendors("Vendor 1")
        self.add_customer.click_active_checkbox()
        self.add_customer.enter_admin_content("Hi My name is Ujjwal")
        self.add_customer.click_save_button()

        customer_add_success_msg = "The new customer has been added successfully."
        success_text = self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissable']").text

        if customer_add_success_msg in success_text:
            assert True
            print("Customer has been added successfully")
            self.logger.info("*************Customer added successfully**********")
            self.driver.close()
        else:
            self.logger.info("********Customer not added successfully**********")
            print("Customer not added")
            self.driver.save_screenshot(".\\screenshots\\test_add_new_user.png")
            self.driver.close()
            assert False
def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(['gmail.com', 'yahoo.com'])
    return f'{username}@{domain}'
