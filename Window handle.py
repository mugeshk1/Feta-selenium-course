from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
    
# try:
    
driver.get("https://www.google.com")
main_window = driver.current_window_handle
print('main_window',main_window)
   
driver.execute_script("window.open('', '_blank', 'width=800,height=600');")
time.sleep(2)

handles = driver.window_handles
print(handles)
for handle in handles:e
    if handle != main_window:
        driver.switch_to.window(handle)

driver.get("https://www.flipkart.com/")
# driver.close()
driver.switch_to.window(main_window)

# finally:
    
    
#     driver.quit()
    