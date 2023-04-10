a=0
b=1
n=int(input("the number of elements to be printed:"))
print("the fibonacci series:")
print(a)
print(b)
while (n-2)>0:
    c=a+b
    print(c)
    a=b
    b=c
    n=n-1
