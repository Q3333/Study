```python
from konlpy.tag import Hannanum
hannanum = Hannanum()
```


```python
hannanum.nouns('한나눔을 이용한 한국어 분석 지금은 명사 분석중')
```




    ['한나눔', '이용', '한국어', '분석', '지금', '명사', '분석중']




```python
hannanum.morphs('한나눔을 이용한 한국어 분석 지금은 형태소 추출')
```




    ['한나눔', '을', '이용', '하', 'ㄴ', '한국어', '분석', '지금', '은', '형태소', '추출']




```python
hannanum.pos('한나눔을 이용한 한국어 분석, 지금은 품사 부착 형태소')
```




    [('한나눔', 'N'),
     ('을', 'J'),
     ('이용', 'N'),
     ('하', 'X'),
     ('ㄴ', 'E'),
     ('한국어', 'N'),
     ('분석', 'N'),
     (',', 'S'),
     ('지금', 'N'),
     ('은', 'J'),
     ('품사', 'N'),
     ('부착', 'N'),
     ('형태소', 'N')]




```python

```
