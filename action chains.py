# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

# import time
# driver = webdriver.Chrome()
# browser=driver.get("https://www.facebook.com/")
# element = driver.find_element(By.XPATH,"//input[@id='email']")
# actions = ActionChains(browser)
# time.sleep(3)
# actions.move_to_element(element).click().send_keys("mugesh@gmail.com").perform()
# actions.perform()
# driver.find_element(By.XPATH,"//input[@id='email']").send_keys("mugesh@gmail.com");
# driver.find_element(By.XPATH,"//*[@id='pass']").send_keys("karthi");

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

element = driver.find_element(By.XPATH, "//input[@id='email']")

time.sleep(3)
actions = ActionChains(driver)
actions.move_to_element(element).click().send_keys("mugesh@gmail.com").perform()
time.sleep(5)
driver.quit()
