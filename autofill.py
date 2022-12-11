#import webdriver from selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#now open the form in firefox
web = webdriver.Firefox()
web.get("https://docs.google.com/forms/d/e/1FAIpQLSc1fODvhmwFa84nJJmjx5t2SzYPduS6RIe1tTZ9hqGIq-hdQw/viewform?vc=0&c=0&w=1&flr=0")
time.sleep(20)
#fill the form
first_name = 'Arfan'
first_name_url = web.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
first_name_url.send_keys(first_name)
