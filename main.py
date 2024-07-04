from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

KEYWORD = 'how crawling'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
service = webdriver.ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.get('http://google.com')

search_bar = browser.find_element(By.CLASS_NAME, "gLFyf")
search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

elements_to_screenshot = []
try:
    search_results1 = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "srKDX")))
    for index, search_result in enumerate(search_results1):
            search_result.screenshot(f"screenshots/{KEYWORD}({index}).png")
except TimeoutException:
     print('Timeout occured')
finally:
    search_results2 = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "MjjYud")))
    for index, search_result in enumerate(search_results2):
        try: # 관련 질문박스 제외
            except_result = search_result.find_element(By.CLASS_NAME, "cUnQKe")
            continue
        except NoSuchElementException:
             pass
        try: # 관련 검색어박스 제외
            except_result2 = search_result.find_element(By.CSS_SELECTOR, '[data-abe]')
            continue
        except NoSuchElementException:
             pass
        try: # 동영상박스 제외
            except_result3 = search_result.find_element(By.CLASS_NAME, 'uVMCKf')
            continue
        except NoSuchElementException:
             pass
        elements_to_screenshot.append(search_result)
    for index, element in enumerate(elements_to_screenshot):
        element.screenshot(f"screenshots/{KEYWORD}({index}).png")
while True:
    pass

browser.quit()