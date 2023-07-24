n=3
for i in range(3):# depecting rows
    print(" " * (n-i-1),end="")#for spaces
    print("*" * (2*i+1),end="")#then stars
    print(" " * (n-i-1))#again spaces