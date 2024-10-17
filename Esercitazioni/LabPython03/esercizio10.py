##n=int(input())
##i=2
##while i<=n:
##    num_d=0
##    d=1
##    while d <= i:
##        if i%d==0:
##            num_d += 1
##        d+=1
##    if num_d==2:
##        print(i)
##    i+=1
  

n=int(input('intero: '))
i=2
while i<=n:
    numd=0
    d=1
    while d<=i:
        if i%d==0:
            numd+=1
        d+=1
    if numd==2:
        print(i)
    i+=1
