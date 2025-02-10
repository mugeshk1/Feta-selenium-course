from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")

    main_window = driver.current_window_handle

    driver.execute_script("window.open('https://www.flipkart.com/', '_blank');")
    time.sleep(2)

    handles = driver.window_handles
    for handle in handles:
        if handle != main_window:
            driver.switch_to.window(handle)

    driver.get("https://www.bing.com")

    driver.close()

    driver.switch_to.window(main_window)

finally:
    driver.quit()


