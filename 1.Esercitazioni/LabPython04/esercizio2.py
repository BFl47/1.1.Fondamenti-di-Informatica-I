##s=input('inserire un numero intero: ')
##i=0
##while s!='*':
##    n=int(s)
##    if n>=0:
##        i+=1
##    s=input('inserire un numero intero: ')
##print(i)

n=input('intero: ')
count=0
while n!='*':
    n=int(n)
    if n>=0:
       count+=1
    n=input('intero: ')
print(count)
