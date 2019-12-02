from django.shortcuts import render,redirect
import wikipediaapi
import konlpy
import nltk
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from konlpy.tag import Okt
from konlpy.tag import Komoran
from collections import Counter

# from konlpy.tag import Mecab
# from konlpy.tag import Komoran
# Create your views here.

def index(request):
    wiki=wikipediaapi.Wikipedia('ko')
    page_py = wiki.page('조조') 
    # print("Page - Exists: %s" % page_py.exists())
    # print("Page - Title: %s" % page_py.title)
    # print("Page - Summary: %s" % page_py.summary[0:100])

    # print(type(page_py.sections))

    # wiki = wikipediaapi.Wikipedia(
    #     language='ko',
    #     extract_format=wikipediaapi.ExtractFormat.WIKI)

    # p_wiki = wiki.page("조조")
    # print(p_wiki.text)
    # with open("조조.txt", "w") as f: f.write(p_wiki.text)

    sec1 = page_py.sections[0:1][0]
    # print(type(sec1))
    # print(sec1)

    # sec1_string = " ".join(sec1)
    # print(type(sec1_string))
    # # sec1_split = sec1.split("Subsections ")
    # # print(sec1)


    wiki=wikipediaapi.Wikipedia('ko')
    page_py = wiki.page('조조') 
    
#### 여기부터 형태소분석

    # text = page_py.text
    text = page_py.summary[0:500]
    
    # print(type(text))
    text2 = str(text)
    # print(type(text2))

    okt = Okt()
    
    # print(mecab.nouns(text2))
    
    # list_1 = okt.nouns(text2)

    # print(type(list_1))

    # result = Counter(list_1)
    # print(result)

    

    komoran = Komoran()
    
    
    # 사용예시
        
    print(komoran.nouns(u'오픈소스에 관심 많은 멋진 개발자님들!'))
    
    # print(komoran.pos(text2))

    pos_list = komoran.pos(text2)
    print(type(pos_list))

    for i in pos_list :
        if i[1] == 'NNP' :
            print(i[0])
    
    # print(pos_list[1][1])
    # print(pos_list[2][1])

    context = {
        'total' : page_py.text,
        'title' : page_py.title,
        'sections_1' : page_py.sections[0:1],
        'sections_2' : page_py.sections[1:2],
        'summary': page_py.summary[0:500],

    }
    return render(request,"Ask_Wiki/index.html", context)