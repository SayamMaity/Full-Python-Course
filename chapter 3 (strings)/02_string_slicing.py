# #concatination

# # greeting ='good morning '
# # name='sayam'
# # # print(type(name))
# # # print(greeting + name)
# # c=greeting + name
# # print(c)

# #string slicing
name='sayamIsGood'
# print(name[1:5])#-->always 5-1
# print(name[0:])#-->similar to name[0:5]
# print(name[:4])#-->similar to name[0:4]

# #negative slicing
# print(name[-5:-1])#-->similar to name[0:4]
# print(name[:-1])#-->similar to name[0:10] 0r name[-11:-1]
# print(name[-5:])#-->for printing -5 to-1
# print(name[-11:])#-->for printing full string

# d=name[0:5:1]#-->har phele character ko print karo
# d=name[0:5:3]#-->har thisreh character ko print karo
# print(d)
d=name[1::3]#-->similar to name[1:11:3]
print(d)