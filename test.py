import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
db = client['fullstack']
collection = db['posts']
print(db)
foundit = collection.find_one({'id':'ce7bd4d2a1aa4decb10eaf883320ae49'})
query = {'blog_id':'123'}
print(type(query))
foundit = db['posts'].find_one(query)

print(foundit)
print(type(foundit))
