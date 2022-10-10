import os
# os.rmdir('data.txt')

# #this is to read  R for ead W for write A for append X for delete
# f = open('data.txt','r')
# print(f.read())


# f = open('data.txt','r')
# print(f.read(2))


f = open('data.txt','w')
f.write('\nmati')
f = open('data.txt','r')
print(f.read())

