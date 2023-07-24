# to write

# f=open('another.txt','w')
# f.write('pls2 write to the file')#if we change this another.txt also gets changed
# f.close()#also if we again use write it will delete the last written thing and then write it as new

#for appending

# f=open('another.txt','a')
# f.write('bolo tara ra ra ra')#if we change this another.txt also gets changed
# f.close()

# for writing multiple time in a txt file

f=open('another.txt','w')
f.write('pls1 write to the file')#if we change this another.txt also gets changed
f.write('pls2 write to the file')
f.write('pls3 write to the file')
f.write('pls4 write to the file')
f.close()