from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstNumber = browser.find_element_by_id("num1").text
    secondNumber = browser.find_element_by_id("num2").text
    
    sum = int(firstNumber) + int(secondNumber)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(sum))
 
    browser.find_element_by_class_name("btn").click()
    

finally:
    time.sleep(30)
    browser.quit()
