##s='sei'
##i=0
##while not ('a' and 'c' in s):
##    s=input('inserire una stringa: ')
##    i+=1
##print(i)

count=0
s='jdas'
while s.count('a')==0 or s.count('c')==0:
    s=input('stringa: ')
    count+=1
print(count)
