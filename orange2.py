from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


# project 2 Test case ID:TC_PIM_03
class Test_Orange:
    url = "https://opensource-demo.orangehrmlive.com"

    # Booting Method for running the Python Tests
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()

    def test_add(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(By.NAME, 'username', ).send_keys('admin')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]').click()
        time.sleep(5)
        self.driver.find_element(By.NAME,'firstName').send_keys('Maha')
        self.driver.find_element(By.NAME, 'middleName').send_keys('Lakshmi')
        self.driver.find_element(By.NAME, 'lastName').send_keys('Sivasubramoniam')
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()




