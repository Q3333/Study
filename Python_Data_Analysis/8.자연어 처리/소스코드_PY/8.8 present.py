import pandas as pandas
import numpy as np

import platform
import matplotlib.pyplot as plt

%matplotlib inline

path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')    

plt.rcParams['axes.unicode_minus'] = False

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import time


tmp1 = 'https://search.naver.com/search.naver?where=kin'
html = tmp1 + '&sm=tab_jum&ie=utf8&query={key_word}&start={num}'

response = urlopen(html.format(num=1, key_word=urllib.parse.quote('여친 선물')))

soup = BeautifulSoup(response, "html.parser")

tmp = soup.find_all('dl')


tmp_list = []
for line in tmp:
    tmp_list.append(line.text)
    
tmp_list


from tqdm import tqdm_notebook

present_candi_text = []

for n in tqdm_notebook(range(1,1000,10)): #원랜 만개, but 컴이 느려서 1000개로 줄임
    response = urlopen(html.format(num=n,
                                        key_word=urllib,parse.quote('여자친구 선물')))

    soup = BeautifulSoup(response, "html.parser")

    tmp = soup.find_all('dl')

    for line in tmp:
        present_candi_text.append(line.text)

    time.sleep(0.1)
    #원랜 0.5인데 컴이 느려서 0.1로 빠르게 실행


present_candi_text


import nltk
from konlpy.tag import Twitter; t = Twitter()


present_text = ''

for each_line in present_candi_text[:1000]:
    present_text = present_text + each_line + '\n'

tokens_ko = t.morphs(presnt_text)
tokens_ko


ko = nltk.Text(tokens_ko, name='여자친구 선물')
print(len(ko.tokens))
print(len(set(ko.tokens)))


ko = nltk.Text(tokens_ko, name='여자친구 선물')
ko.vocab().most_common(100)


stop_words = ['.','가','요','답변','...','을','수','에','질문','제','를','이','도',
                      '좋','1','는','로','으로','2','것','은','다',',','니다','대','들',
                      '2020.01','들','데','..','의','때','겠','고','게','네요','한','일','할',
                      '10','?','하는','05','주','려고','인데','거','좀','는데','~','ㅎㅎ',
                      '하나','이상','20','뭐','까','있는','잘','습니다','다면','했','주려',
                      '지','있','못','후','중','줄','6','과','어떤','기본','!!',
                      '단어','선물해','라고','중요한','합','가요','....','보이','네','무지',
                      '****','닉네임','하고','검색','저','걸','이런','나','입력','합니다','해서','해','연관검색어',
                      '된','됩니다','!','께서']

tokens_ko = [each_word for each_word in tokens_ko 
                                                         if each_word not in stop_words]

ko = nltk.Text(tokens_ko, name='여자 친구 선물')
ko.vocab().most_common(50)



plt.figure(figsize=(15,6))
ko.plot(50)
plt.show()


### 2일차
from wordcloud import WordCloud, STOPWORDS
from PIL import Image


data = ko.vocab().most_common(300)

wordcloud = WordCloud(font_path='c:/Windows/Fonts/malgun.ttf',
                      relative_scaling = 0.2,
                      #stopwords=STOPWORDS,
                      background_color='white',
                      ).generate_from_frequencies(dict(data))
plt.figure(figsize=(16,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


mask = np.array(Image.open('../../data/09. heart.jpg'))

from wordcloud import ImageColorGenerator

image_colors = ImageColorGenerator(mask)



data = ko.vocab().most_common(300)

wordcloud = WordCloud(font_path='c:/Windows/Fonts/malgun.ttf',
                      relative_scaling = 0.1,
                      mask=mask,
                      background_color='white',
                      min_font_size=1,
                      max_font_size=100
                      ).generate_from_frequencies(dict(data))

default_colors = wordcloud.to_array()

plt.figure(figsize=(12,12))
plt.imshow(wordcloud.recolor(color_func=image_colors),interpolation="bilinear")
plt.axis("off")
plt.show()
