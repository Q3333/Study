import matplotlib.pyplot as plt
import nltk
from wordcloud import WordCloud, STOPWORDS
from konlpy.corpus import kobill
from konlpy.tag import Twitter; t = Twitter()
import platform

#맷플롯 폰트설정
path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc
if platform.system() == "Darwin":
    rc('font', family='AppleGothic')
elif platform.system() == "Windows":
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown System... sorry~~~')
    


#KoNLPy 가 내자하고있는 법률 문서 중 하나 
files_ko = kobill.fileids()
doc_ko = kobill.open('1809890.txt').read()

# print(doc_ko)

tokens_ko = t.nouns(doc_ko)
# print(tokens_ko)

ko = nltk.Text(tokens_ko, name='대한민국 국회 의안 제 1809890호')
# print(len(ko.tokens))
# print(len(set(ko.tokens)))
# ko.vocab()

# plt.figure(figsize=(12,6))
# ko.plot(50)
# plt.show()

stop_words = ['.', '(', ')', "'", '%', '-', 'X', ').','x','의','자','에','안','번','호','을',
'이','다','만','로','가','를']

ko = [each_word for each_word in ko if each_word not in stop_words]

ko = nltk.Text(ko, name='대한민국 국회 의안 제 1809890호')

# plt.figure(figsize=(12,6))
# ko.plot(50)
# plt.show()

ko.count('초등학교')

# plt.figure(figsize=(12,6))
# ko.dispersion_plot(['육아휴직','초등학교', '공무원'])

# ko.concordance('초등학교')

# ko.collocations()

data = ko.vocab().most_common(150)

# for mac : font_path='/Library/Fonts/AplleGothic.ttf'
wordcloud = WordCloud(font_path='c:/Windows/Fonts/malgun.ttf',
                        relative_scaling = 0.2,
                        background_color='white',).generate_from_frequencies(dict(data))
plt.figure(figsize=(10,6))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()