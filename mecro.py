from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# 새로고침할 웹사이트 URL
url = 'https://srobot.sen.hs.kr/'

# ChromeDriver를 자동으로 다운로드 및 설정
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # 지정된 URL 열기
    driver.get(url)
    
    # 새로고침 주기를 설정 (초 단위)
    refresh_interval = 10  # 10초 간격으로 새로고침
    
    while True:
        time.sleep(refresh_interval)
        driver.refresh()  # 새로고침 실행
        print(f"웹사이트를 새로고침했습니다: {url}")
        
except KeyboardInterrupt:
    # 사용자가 프로그램을 중지했을 때 처리
    print("프로그램 종료")
finally:
    # 웹 드라이버 종료
    driver.quit()
