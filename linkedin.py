from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from selenium.webdriver.common.keys import Keys
#create a session
client = requests.Session()

# Creating a webdriver instance
driver = webdriver.Chrome("C:/Users/yashj/Desktop/NIT/chromedriver")
# This instance will be used to log into LinkedIn

# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")

# waiting for the page to load
time.sleep(1)

# entering username
username = driver.find_element_by_id("username")

# In case of an error, try changing the element
# tag used here.

# Enter Your Email Address
username.send_keys("enter_email")

# entering password
pword = driver.find_element_by_id("password")
# In case of an error, try changing the element
# tag used here.

# Enter Your Password
if True:
    pword.send_keys("enter_password")	

# waiting for the user to enter password	
time.sleep(4)
# Clicking on the log in button
driver.find_element_by_xpath("//button[@type='submit']").click()

time.sleep(10)
my_mail = input('Enter the email id to search: ')
time.sleep(1)

username = my_mail.split("@")[0]
name = ''

for i in username:
    if i.isalpha():
        name +=i
    else :
        name += " "   
print(name) 

# for fetching first_name & last_name
first_name = []
last_name = []
for i in range(3):
    first_name.append(name[:4+i])
    last_name.append(name[4+i:])

print(first_name, last_name)
flag2 = 0
for i in range(3):
    driver.get("https://www.linkedin.com/search/results/people/?keywords={}%20{}&origin=CLUSTER_EXPANSION".format(first_name[i], last_name[i]))

    src = driver.page_source

    # Now using beautiful soup
    arr = []
    soup = BeautifulSoup(src, 'lxml')
    for i in soup.find_all('span', class_='entity-result__title-text') :
        x = i.find_all('a')
        arr.append(x[0].get('href'))

    flag = 0
    email = ""
    for i in range(len(arr)):
        time.sleep(1)
        driver.get(arr[i].split("?")[0] + "/overlay/contact-info/")
        time.sleep(2)
        src = driver.page_source
        soup = BeautifulSoup(src , "lxml")
        head = soup.find_all('a', class_='pv-contact-info__contact-link')
        for j in head:
            if '@' in str(j):
                email = j.get('href').split(":")[1]
                which_profile = i
                flag = 1
                break
        if flag:
            break
    if email == my_mail :
        print("Its a MATCH ")
        print(arr[which_profile])
        flag2 = 1
        break
    email = ""
    time.sleep(2)
    if flag2:
        break