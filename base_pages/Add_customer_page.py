import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from seleniumbase import Driver


class Add_customer_page:
    link_customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_option_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    add_new_button_xpath = "//a[@class='btn btn-primary']"
    text_email_id = "Email"
    text_password_id = "Password"
    text_first_name_id = "FirstName"
    text_last_name_id = "LastName"
    gender_male_id = "Gender_Male"
    gender_female_id = "Gender_Female"
    company_name_id = "Company"
    Is_tax_exempt_id = "IsTaxExempt"
    newsletter_xpath = "//form[@method='post']//li[1]//input[1]"
    newsletter_option_xpath = "//li[@title='nopCommerce admin demo store']"
    remove_register_option_xpath = "//span[@class='select2-selection__choice__remove']"
    customer_role_xpath = "//input[@aria-controls='select2-SelectedCustomerRoleIds-results']"
    administrators_xpath = "//li[normalize-space()='Administrators']"
    forum_moderators_xpath = "//li[normalize-space()='Forum Moderators']"
    registered_xpath = "//span[@role='presentation']"
    guests_xpath = "//li[normalize-space()='Guests']"
    vendors_xpath = "//select[@class='form-control valid']"
    dropdown_vendor_id = "VendorId"
    active_checkbox_id = "Active"
    password_change_id = "MustChangePassword"
    admin_comment_id = "AdminComment"
    save_button_name = "save"
    success_msg_xpath = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self,driver):
        self.driver = driver

    def click_customers(self):
        self.driver.find_element(By.XPATH,self.link_customer_menu_xpath).click()

    def click_customer_menu_option(self):
        self.driver.find_element(By.XPATH,self.link_customer_option_xpath).click()

    def click_add_new_button(self):
        self.driver.find_element(By.XPATH,self.add_new_button_xpath).click()

    def enter_email(self,email):
        self.driver.find_element(By.ID,self.text_email_id).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.text_password_id).send_keys(password)

    def enter_first_name(self,firstname):
        self.driver.find_element(By.ID,self.text_first_name_id).send_keys(firstname)

    def enter_lastname(self,lastname):
        self.driver.find_element(By.ID,self.text_last_name_id).send_keys(lastname)
        
    def select_gender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.gender_male_id).click()
        else:
            self.driver.find_element(By.ID,self.gender_female_id).click()

    def enter_company_name(self,company_name):
        self.driver.find_element(By.ID,self.company_name_id).send_keys(company_name)

    def select_tax_exempt_checkbox(self):
        self.driver.find_element(By.ID,self.Is_tax_exempt_id).click()

    # def select_newsletter_option(self):
    #     elements = self.driver.find_element(By.XPATH, self.newsletter_xpath).click()
    #     newsletter_field =




    def select_customer_role(self):
        self.driver.find_element(By.XPATH,self.remove_register_option_xpath).click()
        self.driver.find_element(By.XPATH,self.guests_xpath).click()
        time.sleep(2)

    def select_manager_of_vendors(self,value):
        dropdown = Select(self.driver.find_element(By.ID,self.dropdown_vendor_id))
        dropdown.select_by_visible_text(value)

    def click_active_checkbox(self):
        self.driver.find_element(By.ID,self.active_checkbox_id).click()

    def enter_admin_content(self,msg):
        self.driver.find_element(By.ID,self.admin_comment_id).send_keys(msg)

    def click_save_button(self):
        self.driver.find_element(By.NAME,self.save_button_name).click()
    

