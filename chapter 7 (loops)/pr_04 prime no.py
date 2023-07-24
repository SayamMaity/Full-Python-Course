a=int(input("enter no."))
prime=True # first we are thinking that the no. we have entered is prime
for i in range(2,a):
    if (a%i==0):
        prime=False# if it's get dived by the range then the condition become false
        break
if prime:
    print("the no. is prime")
else:
    print("the no. is not prime")

