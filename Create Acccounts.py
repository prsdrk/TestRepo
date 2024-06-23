#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

random_wait_time_list = range(2,9)
random_wait_time = random.choice(random_wait_time_list)

#Open Google Account Page

#options = webdriver.ChromeOptions()
#options.add_argument("--disable-blink-features=AutomationControlled")
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

options = uc.ChromeOptions()
options.add_argument('--blink-settings=imagesEnabled=false')
uc.TARGET_VERSION = 85
driver = uc.Chrome(options=options)
time.sleep(random_wait_time)
driver.get("https://account.google.com")



time.sleep(random_wait_time)

#Click Create account

create_account = driver.find_element(By.XPATH,"/html/body/header/div[1]/div[5]/ul/li[1]/a")
create_account.click()

time.sleep(random_wait_time)

#Enter FirstName

first_name = driver.find_element(By.ID,"firstName")
first_name.click()

time.sleep(random_wait_time)
first_name.send_keys("Sreelaxmi")

#Enter Last Name

first_name = driver.find_element(By.ID,"lastName")
first_name.click()

time.sleep(random_wait_time)
first_name.send_keys("Nair")


#Click Next

time.sleep(random_wait_time)
first_name = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button/span")
first_name.click()


#Select Month

time.sleep(random_wait_time)
month = Select(driver.find_element(By.ID,"month"))
time.sleep(random_wait_time)
month.select_by_visible_text("May")

#Enter Day

time.sleep(random_wait_time)
day = driver.find_element(By.ID,"day")
day.click()
time.sleep(random_wait_time)
day.send_keys("20")

#Enter Year

time.sleep(random_wait_time)
day = driver.find_element(By.ID,"year")
day.click()
time.sleep(random_wait_time)
day.send_keys("1990")

#Select Gender

time.sleep(random_wait_time)
gender = Select(driver.find_element(By.ID,"gender"))
time.sleep(random_wait_time)
gender.select_by_visible_text("Female")

#Click Next

time.sleep(random_wait_time)
next = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button/span")
next.click()


#Click Option Create your own Gmail Address

time.sleep(random_wait_time)
create_own_address = driver.find_element(By.ID,"selectionc2")
create_own_address.click()

#Click new gmail id textbox

time.sleep(random_wait_time)
new_gmail_id_textbox = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input')
new_gmail_id_textbox.click()

#Enter new Gmail ID

time.sleep(random_wait_time)
new_gmail_id_textbox.send_keys("sreelaxminair03")

#Click Next

time.sleep(random_wait_time)
next = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
next.click()

#Click Password Textbox

time.sleep(random_wait_time)
password_textbox = driver.find_element(By.NAME,"Passwd")
password_textbox.click()

#Enter Password

time.sleep(random_wait_time)
password_textbox.send_keys("Laxmi@2023")


#Click Confirm Password Textbox

time.sleep(random_wait_time)
password_again_textbox = driver.find_element(By.NAME,"PasswdAgain")
password_again_textbox.click()

#Enter Password

time.sleep(random_wait_time)
password_again_textbox.send_keys("Laxmi@2023")


#Click Next

time.sleep(random_wait_time)
next = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button/span")
next.click()

time.sleep(60)


#Click Mobile Number Textbox

# time.sleep(random_wait_time)

# mobile_text = driver.find_element(By.ID,"phoneNumberId")
# driver.implicitly_wait(10)
# ActionChains(driver).move_to_element(mobile_text).click(mobile_text)

# #Enter Mobile Number

# time.sleep(1)
# mobile_text.send_keys("9819184791")

# #Click Next

# time.sleep(1)
# next = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button/span")
# next.click()




