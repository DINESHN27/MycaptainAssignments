#TO FIND FIBONACCI SERIES
n=int(input("How many terms do you need fibonacci series?  "))
i,j=0,1
print(i,j,end=' ')
for k in range(1,n-1):
    x=i+j
    print(x,end=' ')
    i=j
    j=x

