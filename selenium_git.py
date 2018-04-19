
# using selenium login to facebook 
# setting up system to use selenium with python
# selenium module may not be available with package, so install using below command
# pip install selenium

# need to use real account info to login to facebook, please edit this script
# with your facebook account login information

import selenium
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from time import sleep
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

# create a new Firefox session
# firefox may need geckodriver, refer to readme file 

driver = webdriver.Firefox()
driver.get("http://facebook.com")
time.sleep(5)

login_username = driver.find_element_by_id("email")
login_password = driver.find_element_by_id("pass")

# need to use real account info to login to facebook
# else facebook login error will be shown
login_username.send_keys("type username")
login_password.send_keys("type password")

login_button = driver.find_element_by_id("loginbutton")
login_button.click()
time.sleep(5)
