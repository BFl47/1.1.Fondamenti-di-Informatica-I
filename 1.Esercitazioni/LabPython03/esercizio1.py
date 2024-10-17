##n=int(input())
##i=0
##if n>2:
##    if n%2==0:
##        while i<n:
##            i += 2
##            print(i)              
##    elif n%2==1:
##        while i<(n-1):
##            i += 2
##            print(i)

n=int(input('intero: '))
i=0
if n>2:
    if n%2==0:
        while i<n:
            i+=2
            print(i)
    else:
        while i<(n-1):
            i+=2
            print(i)
