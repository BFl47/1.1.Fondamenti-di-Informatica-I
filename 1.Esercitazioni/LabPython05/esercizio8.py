##base=int(input('inserire la base del triangolo: '))
##j=base//2
##for i in range(1,base+1,2):
##    print(' '*j,'','*'*i)
##    j-=1
##

b=int(input('base: '))
j=b//2
for i in range(1,b+1,2):
    print(' '*j,'*'*i)
    j-=1
