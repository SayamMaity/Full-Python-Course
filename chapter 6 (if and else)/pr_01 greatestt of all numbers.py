#code with harry code

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
if(num1>num4):
     f1 = num1
else:
     f1 = num4
if(num2>num3):
     f2 = num2
else:
     f2 = num3
if(f1>f2):
     print(str (f1) + " is greatest")
else:
    print(str(f2) + " is greatest")

# # my code
# a=int(input("enter number\n"))
# b=int(input("enter number\n"))
# c=int(input("enter number\n"))
# d=int(input("enter number\n"))
# if(a>b and a>c and a>d):
#     print("a is greatest of all four no.",a)
# elif(b>a and b>c and b>d):
#     print("b is greatest of all four no.",b)
# elif(c>a and c>b and c>d):
#     print("c is greatest of all four no.",c)
# else:
#     print("d is greatest of all four no.",d)