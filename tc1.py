from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

driver = webdriver.Chrome()

def login_test(id, password, output_file):
    try:
        # 브라우저 전체 화면 모드로 설정
        driver.maximize_window()
        
        # 로그인 페이지 열기
        driver.get("https://www.kurly.com/member/login")
        
        # 사용자 이름과 비밀번호 입력
        username_field = driver.find_element(By.NAME, "id")
        password_field = driver.find_element(By.NAME, "password")
        username_field.send_keys(id)
        password_field.send_keys(password)
        
        # 로그인 버튼 클릭
        login_button = driver.find_element(By.CLASS_NAME, "e4nu7ef3")
        login_button.click()
        
        # 결과 확인
        try:
            # 로그인 성공 확인 (예: 대시보드 페이지로 이동 확인)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "eo7pjfk1"))  # 로그인 후 이동할 페이지의 요소
            )
            result = "Login successful: Dashboard page loaded."
        except:
            # 로그인 실패 확인 (예: 오류 메시지 확인)
            error_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "swal2-html-container"))
            )
            result = "정상 로그인 되었습니다."
    
    except Exception as e:
        # 예외 발생 시 오류 메시지 출력
        result = f"An error occurred: {e}"
    
    finally:
        # 브라우저 종료
        driver.quit()
       # 결과를 파일에 기록
        with open(output_file, 'a') as f:
            f.write(f"결과 :\n{result}\n\n")

# 현재 날짜와 시간을 가져와 파일명으로 설정
now = datetime.datetime.now()
output_file = now.strftime("%Y.%m.%d %H-%M-%S") + '.txt'

# 테스트 실행
login_test("ssss8784", "testtest00", output_file)  # 올바른 자격 증명