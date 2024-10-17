##s=input('inserire una stringa: ')
##n=int(input('inserire un intero: '))
##
##for i in range(0, len(s)):
##    print(s[i]*n, end='')

s=str(input('stringa: '))
n=int(input('intero: '))
s1=''

for i in range(len(s)):
    s1+=s[i]*n
print(s1)
