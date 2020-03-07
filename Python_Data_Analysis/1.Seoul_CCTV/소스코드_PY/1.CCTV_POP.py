import pandas as pandas

CCTV_Seoul = pd.read_csv("../../data/01. CCTV_in_Seoul.csv", encoding='utf-8')

CCTV_Seoul.head()

CCTV_Seoul.columns

CCTV_Seoul.columns[0]


CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
CCTV_Seoul.head()

pop_Seoul = pd.read_excel('../../data/01. population_in_Seoul.xls', encoding='utf-8')
pop_Seoul.head()


pop_Seoul = pd.read_excel('../../data/01. population_in_Seoul.xls', 
                          header = 2,
                          usecols = 'B, D, G, J, N',
                          encoding='utf-8')
pop_Seoul.head()


pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별',
                          pop_Seoul.columns[1] : '인구수',
                          pop_Seoul.columns[2] : '한국인',
                          pop_Seoul.columns[3] : '외국인',
                          pop_Seoul.columns[4] : '고령자'}, inplace=True)
pop_Seoul.head()




CCTV_Seoul.head()


CCTV_Seoul.sort_values(by='소계', ascending=True).head(5)

CCTV_Seoul.sort_values(by='소계', ascending=False).head(5)

CCTV_Seoul['최근증가율'] = (CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] + 
    CCTV_Seoul['2014년']) / CCTV_Seoul['2013년도 이전'] * 100

CCTV_Seoul.sort_values(by='최근증가율', ascending=False).head(5)


pop_Seoul.head()

pop_Seoul.drop([0], inplace=True)
pop_Seoul.head()


pop_Seoul['구별'].unique()

pop_Seoul[pop_Seoul['구별'].isnull()]

pop_Seoul.drop([26],inplace=True)


pop_Seoul['외국인비율'] = pop_Seoul['외국인'] / pop_Seoul['인구수'] * 100
pop_Seoul['고령자비율'] = pop_Seoul['고령자'] / pop_Seoul['인구수'] * 100


pop_Seoul.sort_values(by='인구수', ascending=False).head(5)

pop_Seoul.sort_values(by='외국인', ascending=False).head(5)

pop_Seoul.sort_values(by='외국인비율', ascending=False).head(5)

pop_Seoul.sort_values(by='고령자', ascending=False).head(5)

pop_Seoul.sort_values(by='고령자비율', ascending=False).head(5)