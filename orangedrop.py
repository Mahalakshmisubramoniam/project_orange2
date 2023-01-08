from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.common.action_chains import ActionChains

# project 2 Test case ID:TC_PIM_02

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
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
        time.sleep(5)
        user_management = self.driver.find_element(By.XPATH,' //*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span')
        action = ActionChains(self.driver)
        action.click(on_element=user_management)
        action.perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span').click()
        user_role = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]')
        action = ActionChains(self.driver)
        action.click(on_element=user_role)
        action.perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div').click()
        status = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div')
        action = ActionChains(self.driver)
        action.click(on_element=status)
        action.perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div').click()




