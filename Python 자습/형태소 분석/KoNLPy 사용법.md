# KoNLPy 사용법



#### 사용법 사이트 참고 :  https://cceeddcc.tistory.com/8 

#### 공식 사이트 :  https://konlpy-ko.readthedocs.io/ko/v0.4.3/ 



### 1. 자바 설치

####  https://www.oracle.com/technetwork/java/javase/downloads/jdk13-downloads-5672538.html 



시스템,환경변수 설정은 여기 참고

 https://limkydev.tistory.com/61 



### 2. pip로 패키지 2개 설치



```
pip install jpype1
pip install konlpy
```





### 결과값 정리 사이트:

####  https://hyrama.com/?p=463 





#### 실습 결과



### 1.  Hannanum 



#### 코드 

```python
# 형태소 분석 공통코드 
text = page_py.text
    
    # print(type(text))
    text2 = str(text)
    # print(type(text2))

	# Hannanum  적용 코드
    hannanum = Hannanum() 
 
    hannanum.analyze  #구(Phrase) 분석
    hannanum.morphs   #형태소 분석
    hannanum.nouns    #명사 분석
    hannanum.pos      #형태소 분석 태깅
    
    list_1 = hannanum.nouns(text2)
  	# Hannanum  적용 코드 끝
    
    print(type(list_1))

    result = Counter(list_1)
    print(result)
    
# 형태소 분석 공통코드 끝
```







#### 결과 : 

![image-20191129151134877](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191129151134877.png)





### 2. Kkma 

#### 

#### 코드 

```python
# kkma  적용 코드
    kkma = Kkma()
 
    kkma.morphs         #형태소 분석
    kkma.nouns          #명사 분석
    kkma.pos            #형태소 분석 태깅
    kkma.sentences      #문장 분석
    
    list_1 = kkma.nouns(text2)
  	# kkma  적용 코드 끝
```





#### 결과 : 

![image-20191129151020503](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191129151020503.png)





### 3.  Okt



#### 코드 : 

```python
# okt  적용 코드
    okt = Okt()
    
    okt.morphs     #형태소 분석
    okt.nouns      #명사 분석
    okt.phrases    #구(Phrase) 분석
    okt.pos        #형태소 분석 태깅
    
    list_1 = okt.nouns(text2)
  	# okt  적용 코드 끝
```



#### 결과 : 

![image-20191129151744692](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191129151744692.png)





mecab과 코모란은 환경때문에 실습을 못 하였다.

