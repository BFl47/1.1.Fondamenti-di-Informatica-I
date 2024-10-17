##s=input()
##while s[:] != s[::-1]:
##    print('stringa non palindroma, inserire una stringa palindroma')
##    s=input()
##print('stringa palindroma di lunghezza', len(s))

s=input('stringa: ')
while s != s[::-1]:
    print('stringa non palindroma, inserire una stringa palindroma')
    s=input('stringa: ')
print('stringa palindroma di lunghezza', len(s))
