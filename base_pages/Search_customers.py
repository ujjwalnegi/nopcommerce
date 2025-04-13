import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from seleniumbase import Driver


class Search_Customers:
    search_email_id = "SearchEmail"
    search_first_name_id = "SearchFirstName"
    search_last_name_id = "SearchLastName"
    search_button_id = "search-customers"
    search_company_id = "SearchCompany"
    table_rows_xpath = "//table[@id='customers-grid']/tbody//tr"
    table_column_xpath = "//table[@id='customers-grid']/tbody//tr/td"

    def __init__(self, driver):
        self.driver = driver

    def enter_search_email(self,email):
        self.driver.find_element(By.ID, self.search_email_id).send_keys(email)

    # def enter_customer_first_name(self,firstname):
    #     self.driver.find_element(By.ID,self.search_first_name_id).send_keys(firstname)
    #
    # # def enter_customer_last_name(self,lastname):
    # #     self.driver.find_element(By.ID,self.search_last_name_id).send_keys(lastname)
    # #
    # # def enter_company_name(self,company_name):
    # #     self.driver.find_element(By.ID,self.search_company_id).send_keys(company_name)
    #
    def click_search_button(self):
        self.driver.find_element(By.ID,self.search_button_id).click()

    def get_results_table_row(self):
        rows = self.driver.find_elements(By.XPATH, self.table_rows_xpath)
        return len(rows)

    def get_results_table_column(self):
        rows = self.driver.find_elements(By.XPATH,self.table_column_xpath)
        return len(rows)

    def search_customer_by_email(self,email):
        email_present_flag = False
        for r in range(1,self.get_results_table_row()+1):
            customer_email = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody//tr["+str(r)+"]/td[2]").text
            if customer_email == email:
                email_present_flag = True
                break
        return email_present_flag


