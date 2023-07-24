# def great(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# d=int(input("Enter 1st no."))
# f=int(input("Enter 2nd no."))
# g=int(input("Enter 3rd no."))
# print(great(d,f,g))

# code with harry code

def maximum(num1, num2, num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    else:
        if (num2>num3):
            return num2
        else:
            return num3
m = maximum(13, 55, 2)
print("the value of the maximum is" + str(m))