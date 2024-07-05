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

class GoogleKeywordScreenshooter:
  
  def __init__(self, keyword, screenshots_dir):
    self.chrome_options = webdriver.ChromeOptions()
    self.chrome_options.add_experimental_option("detach", True)
    self.service = webdriver.ChromeService(ChromeDriverManager().install())
    self.browser = webdriver.Chrome(service=self.service, options=self.chrome_options)
    self.keyword = keyword
    self.screenshots_dir = screenshots_dir

  def start(self):
    self.browser.get('http://google.com')
    search_bar = self.browser.find_element(By.CLASS_NAME, "gLFyf")
    search_bar.send_keys(self.keyword)
    search_bar.send_keys(Keys.ENTER)

    elements_to_screenshot = []
    try:
        search_results1 = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "srKDX")))
        for index, search_result in enumerate(search_results1):
                search_result.screenshot(f"{self.screenshots_dir}/{self.keyword}({index}).png")
    except TimeoutException:
        print('Timeout occured')
    finally:
        search_results2 = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "MjjYud")))
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
            element.screenshot(f"{self.screenshots_dir}/{self.keyword}({index}).png")

  def finish(self):
    self.browser.quit()


sandwich_competitors = GoogleKeywordScreenshooter('buy large capacy tissue', 'screenshots')
sandwich_competitors.start()
sandwich_competitors.finish()