```python
from konlpy.tag import Kkma
kkma = Kkma()

kkma.sentences('한국어 분석을 시작합니다 문장분석중')
```




    ['한국어 분석을 시작합니다', '문장분석 중']




```python
kkma.nouns('꼬꼬마를 이용한 한국어 분석, 지금은 명사 분석')
```




    ['꼬꼬마', '이용', '한국어', '분석', '지금', '명사']




```python
kkma.pos('꼬꼬마를 이용한 한국어 분석, 이번건 형태소 분석')
```




    [('꼬꼬마', 'NNG'),
     ('를', 'JKO'),
     ('이용', 'NNG'),
     ('하', 'XSV'),
     ('ㄴ', 'ETD'),
     ('한국어', 'NNG'),
     ('분석', 'NNG'),
     (',', 'SP'),
     ('이번', 'NNG'),
     ('건', 'NNG'),
     ('형태소', 'NNG'),
     ('분석', 'NNG')]




```python

```
