from database import Database
from models.post import Post

Database.initialize()

uri="mongodb://192.168.11.23:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

'''
students = collection.find({})

for student in students:
    print(student)
'''

'''
students = [student for student in collection.find({})]
print(students)
students = [student['mark'] for student in collection.find({})]
print(students)
students = [student['mark'] for student in collection.find({}) if student['mark']==100]
print(students)
'''

post = Post()
post2 = Post()
post2.content = "another content"
print(post.content)
print(post2.content)