from nltk.tokenize import word_tokenize
import nltk
from konlpy.tag import Twitter

#분석에 사용한 기사 : https://sports.news.naver.com/news.nhn?oid=477&aid=0000232510&m_view=1&sort=LIKE
# "[현장 REVIEW] ‘손흥민 극장골’ 토트넘, A.빌라에 3-2 역전승"

pos_tagger = Twitter()

train = [('손흥민 지렸다', 'pos'),
         ('레이나 야신모드에 놀라고 손흥민 극장골에 놀랐다', 'pos'),
         ('손까들이 암만욕해도 결국 에이스는 손흥민이다', 'pos'),
         ('손흥민 마지막 극장골 멋있었다', 'pos'),
         ('첫 5경기 연속골에 오늘 멀티골 충분히 잘했다','pos'),
         ('오늘진짜 토트넘 이길경기력은 아니었는데 손흥민도 폼다안올라왔고 근데이걸 전.후반 추가시간에 넣고 이기네 이게 에이스지','pos'),
         ('이러니까 무리뉴가 중간에 손흥민을 못빼지!!! 극장골 소름!!!!','pos'),
         ('승리 후 하회탈 세러머니 지렸다!!','pos'),
         ('대박ㅋㅋ 무리뉴가 손을 못 빼는 이유... 사랑하는 이유네','pos'),
         ('손흥민은 월클이다','pos'),
         ('형아 사랑해','pos'),
         ('결정력 부족이 아니라 그냥 못하는거야 슈팅하나로 놀고먹던 애가 이제는 슈팅까지 못하네... 스피드도 그렇고 움직임도 개별로던데 그리고 최악인건 볼터치. epl탑급 1티어라는 애가 볼터치를 그렇게 하는건 처음봤네 슈팅도 다 정면으로 가던데 그냥 폼이 점점 떨어지는듯... 손흥민보다 평 더 안좋은 애들도 볼터치는 그렇게 안함 걍 막판 골은 수비자책으로 인한 운좋은 골이었음','neg'),
         ('손징징 십자인대 파열 1년 쉬다 오자','neg'),
         ('솔직히 너무 못해요 같은 한국인으로써 부끄럽네요','neg'),
         ('골없었으면 최악의 평점','neg'),
         ('뽀록으로 겨우이겨놓고 좋댄다 참나 ㅋㅋㅋㅋ','neg'),
         ('잘해도 지랄 못해도 지랄 패배자놈들','neg'),
         ('닭집 매수 똥 또 쳐 먹었넹손징징 주서 먹기의 끝판 찌끄레기죠','neg'),
         ('명색이 우레이 라이벌 무관민인데 강등따리 상대로 줏어먹기도 못하면 그게 사람새기냐? ^무^','neg'),
         ('다좋은데pk좀연습하자','neg'),
         ('pk를 지저분하게 차지마라 좀','neg'),
         ('두 골을 넣긴 했지만.. 요즘 폼이 너무 안좋아 보인다','neg'),
         ('토트넘 수비좀 어케해봐라 멱살잡고 흥민이가 끌고가네답답하다 전체적으로 탐욕들만 넘쳐나 특히 모우라알리는 몇개를 날려먹는거냐 골결정력도 마니 부족하다전반적으로 밸런스도 안맞고','neg'),
         ('손흥민은 PK 방식 바꿔야된다 다 읽힌다 ㅋㅋㅋㅋ 중간에 멈추면 당연히 발방향 다 틀키는데 ㅋㅋ','neg'),
         ('혹시나 했지만 역시나 강등권팀이네 내가 이래서 느그흥을 못끊는다','neg'),
         ('손까들 ㅂㄷㅂㄷ 손까들 손흥민보다 축구못하면 가만히있자','neg'),
         ('손까 멸망ㅋㅋㅋ멍청이들','neg'),
         ('ㄴㄱㅎ 웬일이냐','neg'),
         ('무관민 (30, 광저우 헝다)','neg'),
         ('패널티킥은 차지마라 폼도 엉망이구 공부위를 못맞춘다','neg'),
         ('상대방수비실책 줏어먹기 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ안창피하나','neg'),
         ('느그흥 볼터치 십망ㅋㅋㅋㅋㅋㅋ','neg'),
         ('첼시가 지난 경기 3대0으로 개털어먹긴 했어도 뤼디거 복수한다고 이번주 경기 개벼르고 있을텐데 느그흥 이제 어떡하냐 손맘충년들아ㅋㅋㅋㅋㅋㅋ엌ㅋㅋㅋㅋㅋ','neg'),
         ('솔직히 나였어도 넣었다. 운은 하여간 오지게 좋음. 실력은 우레이급인데 우레이가 빡칠만 함. 게나가 나였으면 패널도 성공임','neg'),
         ("어차피 다음경기 첼시한테 또 양학 당할텐데 뭐ㅋㅋ'무관민, 2대0으로 끌려가던 후반 82분경 뤼디거에게 2차 태클로 퇴장. 퇴장도르 수상 청신호'",'neg'),
         ('역시 딱 양학용 ㅋㅋㅋㅋ','neg'),
         ('페널티 봉산탈춤 졸웃김 ㅋㅋㅋ 공격수 맞음? 오늘도 여전히 못했지만 상대 수비수 실책으로 세탁성공','neg'),
         ('느그흥 팔골절 의심됨 ㅡㅡ','neg'),
         ('무관민새기 또 강등따리팀 패고 손맘충년들 희망고문하는 거 보소 잔인한 새기ㅜㅜ','neg'),
         ('오늘도 못했는데 상대수비수 실책으로 세탁','neg'),
         ]

train
# 학습 데이터 생성

def tokenize(doc):
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]
    #형태소 분석된 결과에 태그를 붙여주는 과정.

train_docs = [(tokenize(row[0]), row[1]) for row in train]
train_docs
# 학습 데이터를 형태소 분석

tokens = [t for d in train_docs for t in d[0]]
tokens
# 형태소 분석한 학습데이터들을 기반으로 단어뭉치 생성

def term_exists(doc):
    return {word: (word in set(doc)) for word in tokens}
#해당 문장에 단어뭉치 속 단어가 존재하는지 판단하는 함수.

train_xy = [(term_exists(d), c) for d,c in train_docs]
train_xy
# 학습 문장 속 단어와 단어 뭉치 속 단어를 비교.


classifier = nltk.NaiveBayesClassifier.train(train_xy)
classifier.show_most_informative_features()
#비교한 값을 학습 데이터로 하여 분석기 완성


#### 테스트 과정

def term_exists(doc):
    return {word: (word in set(doc)) for word in tokens}

### 테스트 1

test_sentence1 = '이것이 바로 공격수의 능력이다 멋있다 손흥민!! 최고!! ^^'

test_docs1 = tokenize(test_sentence1)

test_sent_features1 = term_exists(test_docs1)
classifier.classify(test_sent_features1)

#test_sent_features1

### 테스트 2

test_sentence2 = '두 골을 넣긴 했지만.. 요즘 폼이 너무 안좋아 보인다'

test_docs2 = tokenize(test_sentence2)

test_sent_features2 = term_exists(test_docs2)
classifier.classify(test_sent_features2)

#test_sent_features2


### 테스트 3

test_sentence3 = 'pk를 지저분하게 차지마라 좀'

test_docs3 = tokenize(test_sentence3)

test_sent_features3 = term_exists(test_docs3)
classifier.classify(test_sent_features3)

#test_sent_features3


### 테스트 4

test_sentence4 = '졸라 못하다가 막판에 한 건 ㅋㅋㅋ'

test_docs4 = tokenize(test_sentence4)

test_sent_features4 = term_exists(test_docs4)
classifier.classify(test_sent_features4)

#test_sent_features4


### 테스트 5

test_sentence5 = '오늘 진짜 대박!!!!!'

test_docs5 = tokenize(test_sentence5)

test_sent_features5 = term_exists(test_docs5)
classifier.classify(test_sent_features5)

#test_sent_features5




############ 크롤링 하는 과정

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

#갯수 확인
print(len(text_list))

#리스트 확인
print(text_list[0])

#판정 결과 확인

text_count = 0
pos_count = 0
neg_count = 0
for i in text_list :
    for_test_sentence = "'" + i + "'" 

    for_test_docs = tokenize(for_test_sentence)

    for_test_sent_features = term_exists(for_test_docs)
    
    print("'" + i + "' 의 긍부정 판정 결과는 " + classifier.classify(for_test_sent_features) + "입니다.")
      
    if classifier.classify(for_test_sent_features) == 'neg' :
        neg_count = neg_count + 1
    else :
        pos_count = pos_count + 1
        
    text_count = text_count + 1
    if text_count > 100 :
        break

#판정 결과 정리
print("neg 표현의 갯수는 " + str(neg_count) + "개 입니다.")
print("pos 표현의 갯수는 " + str(pos_count) + "개 입니다.")