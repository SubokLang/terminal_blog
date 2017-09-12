from database import Database
from models.post import Post

Database.initialize()

post = Post(blog_id="123",
            title="First Post",
            content="FIRST",
            author="me"
            )

# post.save_to_mongo()

# post = Post.from_mongo('')


posts = Post.from_blog('123')
for post in posts:
    print(post)
