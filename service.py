from selenium import webdriver
from selenium.webdriver.chrome.service import Service


path=Service('C:\Program Files (x86)\selenium drivers/chromedriver.exe')

driver = webdriver.Chrome(service=path)

url = 'https://www.google.com'
driver.get(url)
