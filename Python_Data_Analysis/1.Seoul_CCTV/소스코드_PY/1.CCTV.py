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