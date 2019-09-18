from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("trollface")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    xElement = browser.find_element_by_id("input_value")
    x = xElement.text
    y = str(math.log(abs(12*math.sin(int(x)))))
    answerField = browser.find_element_by_id("answer")
    answerField.send_keys(y)
    submit = browser.find_element_by_class_name("btn")
    submit.click()
        
finally:
    time.sleep(30)
    browser.quit()
