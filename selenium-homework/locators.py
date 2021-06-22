from selenium import webdriver

PATH = "/Users/Andi/Desktop/PM_Horváth_Andrea/Automata tesztelő/Selenium Projects/chromedriver"
URL = "http://localhost:9999/kitchensink.html"

browser = webdriver.Chrome(PATH)
browser.get(URL)

checkbox = browser.find_element_by_id("checkbox-example")
print(checkbox.text)

enter_name_input = browser.find_element_by_css_selector('input[name="enter-name"]')
print(enter_name_input.get_attribute("class"))

another_btn = browser.find_element_by_xpath('//input[@value="Another button"]')
print(another_btn.get_attribute("value"))

browser.quit()