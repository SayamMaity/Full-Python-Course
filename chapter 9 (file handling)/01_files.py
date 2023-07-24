#use open function to read the content of a file!
# f=open('sample.txt','r')
f=open('sample.txt')#by default itopens the file in read mode
# data=f.read()
data=f.read(5)
print(data)
f.close()