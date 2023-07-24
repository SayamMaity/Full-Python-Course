#creating an empty set
b=set()
print(type(b))

#adding values to an empty set
b.add(4)
b.add(5)
b.add(5)#adding a value repeatedly does npot changes a set

# b.add([4,5,7])#we cannot add list in set as list is mutable

#accessing Elements
b.add((3,6,8))
b.add(11)#we can add tuple as tuple is immutable
# b.add({0,4,2})#we cannot add dictionary in set as dictionary is mutable
print(b)

#length of te set
print(len(b))#prints the length of this set

b.remove(5)#removes 5 from set b
# b.remove(10)#throws an error while trying to remove 10 which is not present in the set
print(b)

print(b.pop())#pops a random value
print(b)

# print(b.clear())#clears the whole set
# print(b)
print(b.union({8,11}))
print(b.intersection({8,11}))#throws set() as there is nothing common
print(b.intersection({4,11}))#throws {4} as 4 is there.. in both