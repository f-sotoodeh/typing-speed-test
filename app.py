from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


URL = 'https://typing-speed-test.aoeu.eu/'

browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
wait = WebDriverWait(browser, 10)

browser.get(URL)

sleep(5)
word_count = len(browser.find_elements(By.CLASS_NAME, 'nextword')) + 1
input_box = browser.find_element(By.ID, 'input')
input_box.click()

for _ in range(word_count):
    word = wait.until(EC.visibility_of_element_located((By.ID, 'currentword')))
    input_box.send_keys(word.text)
    input_box.send_keys(Keys.SPACE)
    sleep(.5)
