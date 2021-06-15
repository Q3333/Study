# Pandas 강의 4 - Grouping and Sorting



## Grouping 



Pandas에서 제공하는 `groupby()` operation을 사용하면 예전에 배웠던 `value_counts()` 함수와 같은 기능을 수행할 수 있다.

```python
reviews.groupby('points').points.count()
```

```
points
80     397
81     692
      ... 
99      33
100     19
Name: points, Length: 21, dtype: int64
```





같은 기능을 수행하지만 `value_counts`()은  `groupby()`의 shortcut 같은 느낌이고, **groupby**는 더 다양한 방식으로 사용할 수 있다.

예를 들면 단순 count가 아닌, point별로 그룹을 나눈 뒤 다른 컬럼의 최소 값을 구할 수 있다.

```python
reviews.groupby('points').price.min()
```

```
points
80      5.0
81      5.0
       ... 
99     44.0
100    80.0
Name: price, Length: 21, dtype: float64
```



전에 배웠던 apply를 활용해서 복잡한 selection 구문을 활용할 수도 있다.

```python
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
```

```
winery
1+1=3                          1+1=3 NV Rosé Sparkling (Cava)
10 Knots                 10 Knots 2010 Viognier (Paso Robles)
                                  ...                        
àMaurice    àMaurice 2013 Fred Estate Syrah (Walla Walla V...
Štoka                         Štoka 2009 Izbrani Teran (Kras)
Length: 16757, dtype: object
```



위의 구문 이해를 돕기 위한 winery의 groupby 형태

```python
reviews.groupby('winery').country.count()
```

```
winery
1+1=3                   6
10 Knots                4
100 Percent Wine        3
1000 Stories            2
1070 Green              1
                       ..
Órale                   1
Öko                     2
Ökonomierat Rebholz     4
àMaurice               40
Štoka                   3
Name: country, Length: 16757, dtype: int64
```



아래 사진처럼 winery의 이름 대로 그룹핑을 하면 이런 식으로 묶인다.

![1623765061376](assets/1623765061376.png)







groupby는 한 컬럼 이상에서도 사용할 수 있다.

```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

![1623765174980](assets/1623765174980.png)



#### groupby - egg

groupby는 egg라는 함수를 가지고 있는데, egg 안에 적용하는 함수를 각각 다른 경우의 수로 시뮬레이션을 하는 기능을 가지고 있다.



예를들면

```python
reviews.groupby(['country']).price.agg([len, min, max])
```

![1623765469042](assets/1623765469042.png)



### Multi-index

DF나 Series는 single index를 가지지만, groupby의 경우에는 operation에 따라 multi index가 생긴다.



```python
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed
```

![1623767875227](assets/1623767875227.png)

위와 같은 groupby 구문에서 

```python
mi = countries_reviewed.index
type(mi)
```

```
pandas.core.indexes.multi.MultiIndex
```



index의 type을 확인해보면 MultiIndex로 변한 것을 확인할 수 있다.

@참고 

실제 mi는 이렇게 생김

![1623767934023](assets/1623767934023.png)

##### country와 province 두가지를 가지고 있는 index라서 multi index이다.



만약 multi index를 보통의 index로 바꾸고 싶다면?

`reset_index()`구문을 사용하면 된다.

```python
countries_reviewed.reset_index()
```

![1623768087445](assets/1623768087445.png)



```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

```
points
80     397
81     692
      ... 
99      33
100     19
Name: points, Length: 21, dtype: int64
```





```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

```
points
80     397
81     692
      ... 
99      33
100     19
Name: points, Length: 21, dtype: int64
```





```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

```
points
80     397
81     692
      ... 
99      33
100     19
Name: points, Length: 21, dtype: int64
```





```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

```
points
80     397
81     692
      ... 
99      33
100     19
Name: points, Length: 21, dtype: int64
```





```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

```
points
80     397
81     692
      ... 
99      33
100     19
Name: points, Length: 21, dtype: int64
```





```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

```
points
80     397
81     692
      ... 
99      33
100     19
Name: points, Length: 21, dtype: int64
```

