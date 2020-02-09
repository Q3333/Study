```python
from konlpy.tag import Twitter
t = Twitter()
```


```python
t.nouns('트위터를 이용한 한국어 분석, 지금은 명사 분석')
```




    ['트위터', '이용', '한국어', '분석', '지금', '명사', '분석']




```python
t.morphs('트위터를 이용한 한국어 분석, 지금은 형태소 추출')
```




    ['트위터', '를', '이용', '한', '한국어', '분석', ',', '지금', '은', '형태소', '추출']




```python
t.pos('트위터를 이용한 한국어 분석, 지금은 품사 부착 추출')
```




    [('트위터', 'Noun'),
     ('를', 'Josa'),
     ('이용', 'Noun'),
     ('한', 'Josa'),
     ('한국어', 'Noun'),
     ('분석', 'Noun'),
     (',', 'Punctuation'),
     ('지금', 'Noun'),
     ('은', 'Josa'),
     ('품사', 'Noun'),
     ('부착', 'Noun'),
     ('추출', 'Noun')]




```python
type(t.morphs)
type(t.nouns)
```




    method




```python
a = t.nouns('트위터를 이용한 한국어 분석, 지금은 명사 분석')
```


```python
type(a)
```




    list




```python
b = t.pos('트위터를 이용한 한국어 분석, 지금은 품사 부착 추출')
type(b)
```




    list




```python
type(b[0])
```




    tuple




```python

```
