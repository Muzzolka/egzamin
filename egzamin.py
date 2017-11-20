from selenium import webdriver

browser = webdriver.Firefox()

browser.get("https://bilety.teatr-capitol.pl")

browser.find_element_by_css_selector(".txt")