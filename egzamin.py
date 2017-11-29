from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()

browser.get("https://bilety.teatr-capitol.pl")

browser.find_element_by_css_selector(".txt")

browser.find_element_by_xpath("//a[@class='next']").click()

browser.find_element_by_link_text("Kup bilet").click()

wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.ID, "5519_l"))).click()
wait.until_not(EC.visibility_of_element_located((By.ID, "loading")))

# browser.find_element_by_css_selector("#5813_l").click()
# browser.find_element_by_xpath("//text[@id='5525_l']").click()
# browser.find_element_by_id("5844_l").click()

wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Dalej >>"))).click()

#browser.find_element_by_css_selector("a.btn.btn-default.btn-nastepny.f-r").click()
#browser.find_element_by_class_name("btn.btn-default.btn-nastepny.f-r").click()

# wait = WebDriverWait(browser, 20)
wait.until(EC.title_is("Logowanie - Teatr Muzyczny Capitol"))

browser.find_element_by_id("form_login_login").send_keys("admin@admin")

browser.find_element_by_id("form_login_haslo").send_keys("admin")

browser.find_element_by_id("form_login_submit").click()
