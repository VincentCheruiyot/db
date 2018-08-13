from peewee import *
db = MySQLDatabase('students',user="root",password="",host="localhost")

class Student(Model):
    username = CharField(max_length=255, unique =True)
    points = IntegerField(default=0)

    class Meta:
        database = db
students = [
    {'username':'vin','points':396},
    {'username':'jeff','points':342},
    {'username':'lao','points':298},
    {'username':'churui','points':317},
    {'username':'jacky','points':350},

]
def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                          points=student['points'])
        except IntegrityError:
            student_record=Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()

def top_student():
        student = Student.select().order_by(Student.points.desc()).get()
        return student


if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print(("Our top student right now is: {0.username}.".format(top_student)))
