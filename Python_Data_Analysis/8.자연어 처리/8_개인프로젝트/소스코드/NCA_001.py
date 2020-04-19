from nltk.tokenize import word_tokenize
import nltk
from konlpy.tag import Twitter
from selenium import webdriver
import time


URL = input("네이버 뉴스 기사 댓글창의 URL을 복사해서 입력해주세요")

#https://sports.news.naver.com/news.nhn?oid=477&aid=0000232510&m_view=1&sort=LIKE - 손흥민, 긍정이 많음

train_number = input("원하는 학습 데이터의 개수를 입력해 주세요")

print(URL,train_number)




#웹 드라이버
driver = webdriver.Chrome('./chromedriver.exe') 
driver.implicitly_wait(30)
driver.get(URL)

#더보기 계속 클릭하기
more_count = 0
while True:
    try:
        더보기 = driver.find_element_by_css_selector('a.u_cbox_btn_more')
        더보기.click()
        time.sleep(1)
        more_count = more_count + 1
        if more_count > 10 :
            break
    except:
        break



#댓글추출
contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
text_list = []

for content in contents:
    #print(content.text) #추후 삭제
    text_list.append(content.text)


total_length = len(text_list)
print("추출한 댓글의 갯수는 " + str(total_length) + "개 입니다.")



#학습 데이터 추출
train_count = 0
train_number = int(train_number)
train_list=[]


while train_count < train_number :
    print(str(train_count) + "번째 train data 입니다. 남은 학습 수 : " +str(train_number-train_count))
    print(text_list[train_count])
    text = text_list[train_count]
    #(텍스트, 긍부정여부) 튜플에 넣을 text 데이터
    
    print("학습 데이터의 긍부정 여부를 입력해 주세요 ")
    NB = input("긍정 : 1 , 부정 : 2, 중립 :3 : ") # Naive Bayes classification
    NB = int(NB) #형변환
    
    if(NB is 1) :
        print("긍정입니다")
        NB = "pos"
        
    elif (NB is 2) :
        print("부정입니다.")
        NB = "neg"
        
    else :
        print("pass")
        train_count = train_count + 1
        continue
    
    train_list.append((text,NB))
    train_count = train_count + 1
    print("")
    
    
print(train_list)




# 분석 모델 작성

pos_tagger = Twitter()

def tokenize(doc):
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]
    #형태소 분석된 결과에 태그를 붙여주는 과정.

train_docs = [(tokenize(row[0]), row[1]) for row in train_list]
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





# 위에서 만든 모델에 전체 text data를 넣어 분석
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
    
    #if text_count == 100 :
    #    break






print("pos 표현의 갯수는 " + str(pos_count) + "개 이며, 약 " + str(round(pos_count/total_length*100,2)) + "%입니다.")
print("neg 표현의 갯수는 " + str(neg_count) + "개 이며, 약 " + str(round(neg_count/total_length*100,2)) + "%입니다.")
