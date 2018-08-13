from peewee import *
db = MySQLDatabase("caleb", user="root",password="",host="localhost")

class Salon(Model):
    names=CharField()
    style =CharField()
    height=FloatField()
    desc=TextField()
    payment=IntegerField()
    class Meta:
        database=db
        db_table="customers"

# Salon.create_table()
# Salon.create(names="Phillip", style="jordan", height=5.5, desc="Slim short male", payment = 50)
# Salon.create(names="Willord", style="slope", height=5.5, desc="Tall short male", payment =100)
# Salon.create(names="Eli", style="mohawk", height=5.5, desc="Slim male", payment=100)
# Salon.create(names="Vin", style="normal", height=6.5, desc="Dark tall male", payment=75)
# Salon.create(names="Maureen", style="cornrow", height=4.5, desc="Slim short female",payment=700)

#===============select=================
# customers=Salon.select()
# for customer in customers:
#     print(customer.names,customer.style)
#
# # =========update=====================
# customers=Salon.delete()
# for customer in customers:
#     print()

#=============delete====================

sql_Delete_query = """Delete from customers where id = 23"""
print("\nRecord Deleted Successfully ")