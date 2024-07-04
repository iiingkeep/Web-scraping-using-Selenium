from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_experimental_option("detach", True)
service = webdriver.ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.get('http://google.com')

search_bar = browser.find_element(By.CLASS_NAME, "gLFyf")
search_bar.send_keys('dog')
search_bar.send_keys(Keys.ENTER)

search_results = WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "srKDX")))
print(search_results)

while True:
    pass

browser.quit()