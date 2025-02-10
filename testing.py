from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("mugesh@gmail.com");
driver.find_element(By.XPATH,"//*[@id='pass']").send_keys("karthi");