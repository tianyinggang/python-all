'''
selenium


'''

from selenium import webdriver
import time

browser = webdriver.Chrome('./webdriver/chromedriver')

try:
    browser.get('http://localhost/demo.html')

    buttons = browser.find_elements_by_class_name('mybutton')
    i = 0
    while True:
        buttons[i].click()
        time.sleep(1)
        i += 1
        if i == len(buttons):
            i = 0


except Exception as e:
    print(e)
    browser.close()