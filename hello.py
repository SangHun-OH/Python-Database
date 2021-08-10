import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 브라우저에서 요청한 것 처럼 변경해줌
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


#Ajax와 같은 기능
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
 

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    
    a_tag = tr.select_one('td.title > div > a')
    if a_tag is not None:
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        title = a_tag.text
        star = tr.select_one('td.point').text

        #DB에 넣을 doc를 생성해줌
        doc = {
            'rank':rank,
            'title':title,
            'star':star
        }
        
        
        
       
       
       
       
       
       
       
       
    
        
        
      
        

        #Collection 정보를 movies 로 할당해줌
        db.movies.insert_one(doc)
        
        
