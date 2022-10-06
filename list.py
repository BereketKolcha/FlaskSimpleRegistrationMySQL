#list ordered and changable,possible to duplicate, change data

# student = ['abebe','helina','ayele']
# student[0] = 'samuel'
# print(student)


#tuple ordered and unchangable ,possible to duplicate

# student = ('abebe','helina','ayele')
# print(student[0:2])


#set unordered and unindex ,not possible to duplicate

# student = {'abebe','helina','ayele'}
# print(student)


#dectionary have index and value,can not change order , not possible to duplicate


stud = {"fname":"abebe","lname":"abebe","age":33,"sex":"male"}
stud["email"] =3 # this is for add
# print(stud["fname"] +" "+stud["lname"]+" age :"+str(stud["age"]))
stud.pop("fname")
print(stud)
