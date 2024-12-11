from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome 드라이버 경로 설정
chrome_driver_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

# Chrome 옵션 설정 (디버깅 모드 활성화)
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Chrome 드라이버 시작
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

try:
    # 웹 페이지 열기 (실제 URL로 변경)
    driver.get("https://www.example.com")

    # 특정 요소 클릭 (CSS 선택자 예시)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#GradeDetail > div > ul > li > a"))
    )
    element.click()

    # 원하는 동작 수행 (예: 다른 페이지로 이동, 데이터 추출 등)
    # ...

except KeyboardInterrupt:
    print("프로그램을 종료합니다.")
except Exception as e:
    print(f"오류 발생: {e}")
finally:
    driver.quit()