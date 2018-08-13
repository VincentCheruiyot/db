from peewee import *
db = MySQLDatabase("matatu_data", user="root",password="",host="localhost")

class User(Model):
    names=CharField()
    age =IntegerField()
    height=FloatField()
    desc=TextField()
    class Meta:
        database=db
        db_table="users"

# User.create_table()
# User.create(names="Philip", age=19, height=5.5, desc="Slim short male")
# User.create(names="John Paul", age=29, height=6.1, desc="Dark tall male")
# User.create(names="David", age=39, height=5.9, desc="Dark short male")
# User.create(names="Peter", age=20, height=6.0, desc="Dark male")
# User.create(names="Paul", age=20, height=5.2, desc="Chocolate short male")

# users=User.select()
# for user in users:
#     print(user.names)

users=User.select().where(User.age==20)
for user in users:
   print(user.names, user.age,user.desc,user.height)

# user=User.select().where(User.age==20).get()
# print(user.names)