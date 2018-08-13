from peewee import *
db = MySQLDatabase("caleb", user="root",password="",host="localhost")

class ENVI(Model):
        names = CharField()
        operator = CharField()
        location = CharField()

        class Meta:
            database = db
            db_table = "salons"

salons = Salons.select().order_by(Salons.names)
# print()
# file = open("data3.csv", "w")
# for mat in mats:
#         file.write(mat.driver + "," + mat.route + "\n")
#
# file.close()