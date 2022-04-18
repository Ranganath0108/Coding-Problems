from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
# Replace below path with the absolute path
browser = webdriver.Chrome('chromedriver.exe')
phone = "9591091911"
message = "Hii am Ranganath From KIT \n How was your coding round what are the question ,They asked??"
url = "https//:wa.me/91{phone}"
# Load Whatsapp Web page
browser.get(url)
# Wait for the page be loaded
time.sleep(10)
enter_action = ActionChains(browser)
enter_action.send_keys(Keys.ENTER)
# Send message
enter_action.perform()
# Close browser
browser.close()