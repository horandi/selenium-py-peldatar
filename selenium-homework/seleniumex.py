from selenium import webdriver

PATH = "/Users/Andi/Desktop/PM_Horváth_Andrea/Automata tesztelő/Selenium Projects/chromedriver"
URL = "https://google.com"

browser = webdriver.Chrome(PATH)

try:
    browser.get("URL")
    keresett_div = browser.find_element_by_id("nemletezik")
    print("megtaláltam")
except:
    print("nem található")
finally:
    browser.quit()


