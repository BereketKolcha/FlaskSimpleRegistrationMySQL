# # class
# class student:
#     def first(self):
#         print("it works")

# s1 = student()
# s1.first()


# # class only use self
# class student:
#     def first(self):
#         print("it works " + self.fname)

# s1 = student()
# s1.fname = "ayele"
# s1.first()


# class in constructor
class student:
    def __init__(self,fname,lname):
        self.fn = fname
        self.ln = lname
    def first(self):
        print("it works"+ self.fn + self.ln)
    def ethiopia(self):
        print("Ethiopia: "+ self.fn + self.ln)
    def india(self):
        print("Indian: "+ self.ln + self.fn)

s1 = student("bobe","bereket")
s1.first()
s1.ethiopia()
s1.india()



# # class
# class student:
#     def first(self):
#         print("it works")

# s1 = student()
# s1.first()