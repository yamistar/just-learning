from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome 웹드라이버 객체 생성
driver = webdriver.Chrome()

# 지정된 URL로 이동
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# 암묵적 대기 설정 (5초)
driver.implicitly_wait(5)

# 텍스트 박스와 제출 버튼 요소 찾기
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# 텍스트 박스에 "Selenium" 입력
text_box.send_keys("Selenium")
# 제출 버튼 클릭
submit_button.click()

# 메시지 요소 찾기
message = driver.find_element(by=By.ID, value="message")
# 메시지 텍스트 가져오기
message_text = message.text


# 웹드라이버 종료를 주석 처리하여 브라우저가 닫히지 않도록 함
# driver.quit()
