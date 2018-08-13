from peewee import *
db = MySQLDatabase("matatu_data", user="root", password="",host="localhost")

class Matatu(Model):
    number_plate=CharField()
    driver=CharField()
    route= CharField()
    class Meta:
        database=db
        db_table= "matatu_routes"

mats = Matatu.select().order_by(Matatu.driver)
# print()
file =open("data3.csv","w")
for mat in mats:
    file.write(mat.driver+","+mat.route+"\n")

file.close()


# peewee update


# peewee delete

