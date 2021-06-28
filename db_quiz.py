from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

#(1) 영화제목 '매트릭스'의 평점을 가져오기
movie = db.movies.find_one({'title':'매트릭스'})
target_star = movie['star']

#(2) '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기
target_movies = list(db.movies.find({'star': target_star},{'_id':False}))

for target in target_movies:
    print(target['title'])

#(3) 매트릭스 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})
#DB의 STAR 값들이 문자열로 삽입되었기에 0도 문자열로 삽입해준다.
