letter='''Dear <|NAME|>,
Greeting from sayam.I'm happy to tell u about ur selection
You are selected!

Date:<|DATE|>
'''
a=input("enter name:\n")
b=input("enter date:\n")
# print(letter.replace('<|NAME|>',a))
# print(letter.replace('<|DATE|>',b))
letter=letter.replace('<|NAME|>',a)
letter=letter.replace('<|DATE|>',b)
print(letter)