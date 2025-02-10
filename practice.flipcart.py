from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()        
driver.get("https://www.flipkart.com/account/login?ret=/")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys("watch")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click();
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a/div[1]/div/div/div/img").click();
time.sleep(2)
# Scroll down by 200 pixels smoothly
driver.execute_script("window.scrollBy({top: 200, left: 0, behavior: 'smooth'});")
time.sleep(2)  # Pause to observe the scroll
driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button").click();
time.sleep(2)

