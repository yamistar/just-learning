# 제목: Selenium 웹 자동화 예제
# 작성자: qa-ya
# 날짜: 2024-09-25

from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome 웹드라이버 객체 생성
driver = webdriver.Chrome()

# 지정된 URL로 이동
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# 페이지 제목 가져오기
title = driver.title

# 암묵적 대기 설정 (0.5초)
driver.implicitly_wait(0.5)

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
text = message.text

# 웹드라이버 종료
driver.quit()
