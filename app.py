from database import Database
from models.post import Post

Database.initialize()

'''
post = Post(blog_id="123",
            title="2rd Post",
            content="3rd",
            author="me 3"
            )
post.save_to_mongo()
'''

# post = Post.from_mongo('ce7bd4d2a1aa4decb10eaf883320ae49')
# print(post)
# posts
# Database(MongoClient(host=['127.0.0.1:27017'], document_class=dict, tz_aware=False, connect=True), 'fullstack')


posts = Post.from_blog('123')
for post in posts:
    print(post)
