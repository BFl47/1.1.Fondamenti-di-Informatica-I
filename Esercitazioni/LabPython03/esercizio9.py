##n=int(input())
##num_d=0
##d=1
##
##while d <= n:
##    if n%d==0:
##        num_d += 1
##    d+=1
##if num_d==2:
##    print('numero primo')
##else:
##    print('numero non primo')

n=int(input('intero: '))
numd=0
d=1

while d<=n:
    if n%d==0:
        numd+=1
    d+=1
if numd==2:
    print('numero primo')
else:
    print('numero non primo')
