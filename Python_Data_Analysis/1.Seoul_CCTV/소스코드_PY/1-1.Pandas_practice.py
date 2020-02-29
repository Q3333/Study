import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan,6,8])
s

dates = pd.date_range('20200229', periods=7)
dates

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A','B','C','D'])

df

df.head(3)

df.index

df.columns

df.values

df.info()


df.describe()

df.sort_values(by='B', ascebdubg-False)

df

df['A']

df[0:3]

df['2020-03-03':'2020-03-05']


df.loc[dates[0]]

df.loc[:,['A','B']]


df.loc['2020-03-03':,['A','B']]

df.loc['20200302':'20200305',['C','D']]

df.loc['20200303','A']

df.loc['2020-03-01',['A','D']]

df.loc['2020-03-01','A':'D']

df.loc['2020-03-01']

df.loc['2020-03-01':'2020-03-03']



#iloc

df.iloc[3]

df.iloc[:,3]

df['D']

df.iloc[3:5,0:2]

df.iloc[[1,2,4,],[0,1]]


df.iloc[1:3,:]

df.iloc[:,1:3]



df

df[df.A>0]

df[df > 0]


df2 = df.copy()

df2['E'] = ['one', 'one','two','three','four','three']

df2['E'].isin(['two','four'])

df2[df2['E'].isin(['two','four'])]



df.apply(np.cumsum)

df.apply(lambda x: x.max() - x.min())