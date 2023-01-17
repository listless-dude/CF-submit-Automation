from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver_path = 'SeleniumDrivers/chromedriver.exe'
service = Service(driver_path)
options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)
browser.get('https://codeforces.com/enter')

email = browser.find_element(By.ID, "handleOrEmail")
email.send_keys("your-cf-email")
password = browser.find_element(By.ID, "password")
password.send_keys("your-cf-password")
button = browser.find_element(By.CLASS_NAME, "submit")
button.submit()
browser.implicitly_wait(1)
browser.get('https://codeforces.com/contest/1782/problem/A')
choose = browser.find_element(By.NAME, "sourceFile")
choose.send_keys(r'{absolute_path}\problem.cpp')
choose = browser.find_element(By.CLASS_NAME, "submit")
choose.submit()