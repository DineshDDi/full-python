'''
from selenium import webdriver

c = webdriver.Chrome('./Chromedriver')

c.get('http://DineshDD.pythonanywhere.com')

c.maximize_window()

c.close()
'''


'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

site = webdriver.Chrome('./Chromedriver')
site.get("http://www.python.org")

assert "Python" in site.title

ele = site.find_element_by_name("q")
'''


'''
# basic commands
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./Chromedriver')
driver.get("http://dineshDD.pythonanywhere.com")

print(driver.title)     # show the title of the page
print(driver.current_url)   # show the current url of webside
driver.find_element_by_xpath("//*[@id='navbar-collapse']/ul/li[2]/a").click() # find the elements by xpath views
time.sleep(10)
#driver.close() # close only one window
driver.quit() # close all the window
'''


'''
# navigation commands
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./Chromedriver')
driver.get("http://dineshDD.pythonanywhere.com")
time.sleep(10)
print(driver.title)

driver.get("https://www.python.org")
time.sleep(10)
print(driver.title)

driver.back()
time.sleep(10)
print(driver.title)

driver.forward()
time.sleep(10)
print(driver.title)

driver.quit()
'''


'''
# conditional commands (is_displayed, is_enabled)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./Chromedriver')
driver.get("http://dineshDD.pythonanywhere.com/contact.html")

email_ele = driver.find_element_by_name("email")
print(email_ele.is_displayed())
print(email_ele.is_enabled())

sub_ele = driver.find_element_by_name("subject")
print(sub_ele.is_displayed())
print(sub_ele.is_enabled())

driver.close()
'''


'''
# conditional commands (is_selected)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./Chromedriver')
driver.get("https://www.facebook.com/campaign/landing.php?campaign_id=1653993517&extra_1=s%7Cc%7C355887219776%7Ce%7Cfacebook%7C&placement=&creative=355887219776&keyword=facebook&partner_id=googlesem&extra_2=campaignid%3D1653993517%26adgroupid%3D63066387003%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-541132862%26loc_physical_ms%3D9061943%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=CjwKCAjwn9v7BRBqEiwAbq1Ey5IxcR3FH0Wr3b9pZALhPiRaw_gC-rIU1a4PlzRyXm7g2hJy4EloMRoCFnAQAvD_BwE")

select = driver.find_element_by_css_selector("input[value='2']")
print(select.is_selected())

driver.close()
'''


'''
# checking login, sign button
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./Chromedriver')
driver.get("http://dineshDD.pythonanywhere.com/contact.html")

email_ele = driver.find_element_by_name("email")
print(email_ele.is_displayed())
subj_ele = driver.find_element_by_name("subject")
print(subj_ele.is_displayed())
mess_ele = driver.find_element_by_name("message")
print(mess_ele.is_displayed())


email_ele.send_keys("testing@gmail.com")
subj_ele.send_keys("selenium testing")
mess_ele.send_keys("everything is clear")

driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[2]/div/form/div/div[1]/button").click()

time.sleep(20)

driver.close()
'''


'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./Chromedriver')
driver.get("http://dineshDD.pythonanywhere.com/contact.html")

driver.implicitly_wait(10)

email_ele = driver.find_element_by_name("email") # end of the code you also use .is_displayed and .is_enabled
print(email_ele.is_displayed())
subj_ele = driver.find_element_by_name("subject")
print(subj_ele.is_displayed())
mess_ele = driver.find_element_by_name("message")
print(mess_ele.is_displayed())


email_ele.send_keys("testing@gmail.com")
subj_ele.send_keys("selenium testing")
mess_ele.send_keys("everything is clear")

driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[2]/div/form/div/div[1]/button").click()


driver.close()
'''


'''
# check input box

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./Chromedriver')
driver.get("http://dineshDD.pythonanywhere.com/contact.html")

input_box = driver.find_elements(By.CLASS_NAME,'form-group')
print(len(input_box))

for input in input_box:
    print(input.text)

driver.close()
'''


'''
# check radio button
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./Chromedriver')
driver.get("http://dineshDD.pythonanywhere.com/contact.html")

radio_button = driver.find_element_by_id("").is_selected()
print(radio_button) # False

driver.find_element_by_id("").click()
radio_button = driver.find_element_by_id("").is_selected()
print(radio_button) # True
'''


'''
# find number of links in webpage
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./Chromedriver')
driver.get("http://dineshDD.pythonanywhere.com/contact.html")

links = driver.find_elements(By.TAG_NAME,"a")
print("number of links in my page", len(links))

for link in links:
    print(link.text)

driver.close()
'''


'''
from selenium import webdriver

c = webdriver.Chrome('./Chromedriver')

c.get('http://127.0.0.1:8000/')

c.maximize_window()

c.close()
'''

