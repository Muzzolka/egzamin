from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()

browser.get("https://bilety.teatr-capitol.pl")

browser.find_element_by_css_selector(".txt")

browser.find_element_by_xpath("//a[@class='next']").click()

browser.find_element_by_link_text("Kup bilet").click()

#wait = WebDriverWait(browser, 10)
#wait.until(browser, EC.presence_of_element_located((By.ID, "5800_l")))

browser.find_element_by_css_selector("#5801_l").click()
browser.find_element_by_xpath("//text[@id_miejsca='5800']").click()
browser.find_element_by_id("5802_1").click()