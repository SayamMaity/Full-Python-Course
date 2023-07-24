myDict={
   "Fast":"In a Quick Manner",
   "sayam": "A Coder",
    'marks':[1,2,3,4],
    'anotherdict':{'sayam':'player'},
    1:2
}
# print((myDict.items()))#prints the (key,values)for all contents of the dictionary
# print(type(myDict.items()))#displays the type of the items

# print(myDict.keys())#displays the key
# print(type(myDict.keys()))#displays the type of the keys

# print(myDict.values())#displays the values
# print(type(myDict.values()))#displays the type of the values

print(list(myDict.values()))#convert it into list
print(list(myDict.keys()))#convert it into list

# print(myDict)

# updatedict={
#     'hlo':'world',
#     'google':'sayam',
#     'jk':'frk',
#     'sayam':'actor'#if already present like sayam is already present so it will automatically change it
# }
# myDict.update(updatedict)# updates the dictionary by adding key-value pairs from updatedict
# print(myDict)

# print(myDict.get('sayam'))#prints the value associated with the key 'sayam'
# print(myDict['sayam'])#prints the value associated with the key 'sayam'

# # #the diffference between .get and [] syntax in dictionary
# print(myDict.get('sayam2'))# returns NONE as sayam2 is not present in the dictionary
# # print(myDict['sayam2'])#throws an error as sayam2 is not present in the dictionary