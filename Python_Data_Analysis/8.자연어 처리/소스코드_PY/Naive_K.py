from nltk.tokenize import word_tokenize
import nltk
from konlpy.tag import Twitter

pos_tagger = Twitter()

train = [('메리가 좋아', 'pos'),
         ('고양이도 좋아', 'pos'),
         ('난 수업이 지루해', 'neg'),
         ('메리는 이쁜 고양이야', 'pos'),
         ('난 마치고 메리랑 놀거야','pos')]

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

test_sentence2 = '난 수업이 마치면 메리랑 놀거야'

tokenize(test_sentence2)
test_docs2 = tokenize(test_sentence2)

def term_exists(doc):
    return {word: (word in set(doc)) for word in tokens}

term_exists(test_docs2)

test_sent_features2 = term_exists(test_docs2)
classifier.classify(test_sent_features2)

### 테스트 3

test_sentence3 = '난 고양이가 좋아'

test_docs3 = tokenize(test_sentence3)

test_sent_features3 = term_exists(test_docs3)
classifier.classify(test_sent_features3)

test_sent_features3