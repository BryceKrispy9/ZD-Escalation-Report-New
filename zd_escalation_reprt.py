from selenium import webdriver as wd
import chromedriver_binary

import random
import time

wd = wd.Chrome()
wd.implicitly_wait(10)

wd.get("https://uniphore.zendesk.com/agent/filters/5767299080717")

random_wait_time = random.randrange(1.0, 3.0)
print(random_wait_time)
time.sleep(random_wait_time)

actions_select_button = wd.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/section/div[1]/div/div/div[2]/header/div[2]/button[1]')
actions_select_button.click()

random_wait_time = random.randrange(1.0, 3.0)
print(random_wait_time)
time.sleep(random_wait_time)

export_as_csv_button = wd.find_element_by_xpath('//*[@id="downshift-3-menu"]')