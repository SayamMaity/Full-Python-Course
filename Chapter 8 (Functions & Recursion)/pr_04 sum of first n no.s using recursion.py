# sum(n) = sum(n-1) +n


def sum_recursive(n):
    if n==0:
        return 0
    else:
        return n + sum_recursive(n-1)
a=int(input("enter no."))
f=sum_recursive(a)
print(f)