from selenium import webdriver

def before_scenario(context, scenario):
    context.browser = webdriver.Firefox()
    context.browser.get("https://bilety.teatr-capitol.pl")

def after_scenario(context, scenario):
    context.browser.close()