



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options

# import time




# # ChromeDriver를 자동으로 다운로드 및 설정
# driver = webdriver.Chrome(ChromeDriverManager().install())

# options = Options()  ## Create a ChromeOptions object
# driver = webdriver.Chrome(options=options)  ## Pass options to the Chrome driver

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#동작(동적 웹크롤링)
from selenium.webdriver import ActionChains

#ㅁ몰ㄹ루
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Chrome 드라이버 경로 (다운로드한 ChromeDriver 경로로 수정)
chrome_driver_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

# Chrome 드라이버 설정
driver = Chrome(options=chrome_options)

# 드라이버에 동작을 실행시키는 명령어를 act로 지정
act = ActionChains(driver)


try:
    while True:
        # element1 = act.find_element_by_css_select('.box')
        # act.send_keys('\n')
        # print("새로고침")
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.box'))
        )

        element.click()


    
    # while True:
    #     driver.refresh()  # 새로고침 실행
    #     print("새로고침")
        
except KeyboardInterrupt:
    # 사용자가 프로그램을 중지했을 때 처리
    print("프로그램 종료")
finally:
    # 웹 드라이버 종료
    driver.quit()
