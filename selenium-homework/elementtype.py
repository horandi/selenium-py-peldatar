from selenium import webdriver

PATH = "/Users/Andi/Desktop/PM_Horváth_Andrea/Automata tesztelő/Selenium Projects/chromedriver"
URL = "http://localhost:9999/trickyelements.html"

browser = webdriver.Chrome(PATH)
browser.get(URL)

buttons = browser.find_elements_by_xpath('//button')
buttons[0].click()
result_text = browser.find_element_by_id("result")

assert(result_text.text == f"{buttons[0].text} was clicked")