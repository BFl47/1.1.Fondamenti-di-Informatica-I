##s1=input('inserire una stringa: ')
##s2=input('inserire una stringa: ')
##
##for i in range(0, len(s1)):
##    if s1[i] in s2:
##        print('', end='')
##    else:
##        print(s1[i], end= '')

s1=input('stringa 1: ')
s2=input('stringa 2: ')
s=''

for i in range(len(s1)):
    if s1[i] not in s2:
        s+=s1[i]
print(s)
