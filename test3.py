from database import Database

Database.initialize()




foundit = Database.find_one('posts',{'blog_id':'123'})

print(foundit)
print(type(foundit))