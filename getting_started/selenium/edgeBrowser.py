from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set the path of the Edge driver
driver_path = "C:\\auto\\edgedriver_win64\\msedgedriver.exe"

# Set up the Edge driver
driver = webdriver.Edge(service=Service(driver_path))

# Navigate to the URL
driver.get("https://www.naver.com/")

# 이름 속성으로 검색 상자 요소를 찾습니다
search_box = driver.find_element(By.NAME, "query")

# 검색 상자에 "엣지 자동화"를 입력합니다
search_box.send_keys("엣지 자동화")

# 검색을 제출합니다
search_box.send_keys(Keys.RETURN)