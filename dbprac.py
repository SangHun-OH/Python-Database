from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


#insert
doc = {'name':'Dubo','age':21}
db.users.insert_one(doc)

#find
#id는 false로 지정해야 id값을 불러오지 않음 #60c617a 이런 값
same_ages = list(db.users.find({'age': 21},{'_id':False}))
print(same_ages)

same_ages = list(db.users.find({},{'_id':False}))

for p in same_ages:
    print(p)

#find_one
user = db.users.find_one({'name':'bobby'})
print(user)
print(user['age'])

#update
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
db.users.update_many({'name':'bobby'},{'$set':{'age':19}})

#delete
db.users.delete_one({'name':'bobby'})