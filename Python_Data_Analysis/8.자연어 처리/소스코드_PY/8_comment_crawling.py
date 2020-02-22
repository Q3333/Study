from selenium import webdriver
import time
url = 'https://sports.news.naver.com/news.nhn?oid=477&aid=0000232510&m_view=1&sort=LIKE'

#웹 드라이버
driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(30)
driver.get(url)

#더보기 계속 클릭하기
count = 0
while True:
    try:
        더보기 = driver.find_element_by_css_selector('a.u_cbox_btn_more')
        더보기.click()
        time.sleep(1)
        count = count + 1
        if count > 100 :
            break
    except:
        break

#댓글추출
contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
text_list = []

for content in contents:
    print(content.text)
    text_list.append(content.text)