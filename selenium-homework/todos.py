from selenium import webdriver

PATH = "/Users/Andi/Desktop/PM_Horváth_Andrea/Automata tesztelő/Selenium Projects/chromedriver"
URL = "http://localhost:9999/todo.html"

browser = webdriver.Chrome(PATH)
browser.get(URL)

todos = browser.find_elements_by_css_selector("li")

for todo in todos:
    print(todo.text)

browser.quit()