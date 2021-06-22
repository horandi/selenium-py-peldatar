from selenium import webdriver

PATH = "/Users/Andi/Desktop/PM_Horváth_Andrea/Automata tesztelő/Selenium Projects/chromedriver"
URL = "http://localhost:9999/general.html"

browser = webdriver.Chrome(PATH)
browser.get(URL)

links = browser.find_elements_by_css_selector('a')

try:
    for link in links:
        link_url = link.get_attribute("href")
        link.click()
        assert(link_url == browser.current_url)
        print(browser.current_url)
        browser.back()
except AssertionError:
    print("nem egyezik az url")
finally:
    browser.quit()