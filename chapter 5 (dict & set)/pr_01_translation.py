mydict= {
    'panka':'fan',
    'daba':'box',
    'vastu':'item'
}
print('options are',mydict.keys())
a=input('enter the hindi word\n')
# print("the meaning of your word is:",mydict[a])
#below line will not throw an error msg if the key is not present in the dictionary;
print('the meaning of your word is:',mydict.get(a))