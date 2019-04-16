import pandas as pd 

code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]

code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)

codes = code_df[['회사명', '종목코드']]

codes = codes.rename(columns={'회사명': 'name', '종목코드':'code'})

#print top 5
codes.head()
314710096
def get_url(item_name, code_df):
    code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)
    print("Request...: " + url)
    return url 

name = '삼성전자'
url = get_url(name, codes)

days = pd.DataFrame() 

for p in range(1, 21):
    pg_url = '{url}&page={page}'.format(url=url, page=p)
    days = days.append(pd.read_html(pg_url, header=0)[0], ignore_index=True) 

days = days.dropna()

days = days.rename(columns= {'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'})
df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int) 
df['date'] = pd.to_datetime(df['date']) 
df = df.sort_values(by=['date'], ascending=True) 
days.head()

