from selenium import webdriver

browser = webdriver.Firefox()

browser.get("https://bilety.teatr-capitol.pl")

browser.find_element_by_css_selector(".next").click()

browser.find_element_by_link_text("Makbet").click()

browser.find_element_by_link_text("Kup bilet onlie").click()

browser.find_element_by_link_text("Kup bilet").click()