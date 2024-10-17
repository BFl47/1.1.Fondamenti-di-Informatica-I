##s=input('inserire una stringa: ')
##
##distanza=0
##
##for c in s:
##    sx=s.find(c)
##    dx=s.rfind(c)
##    distanza=max(distanza, dx-sx)
##print(distanza)

s=input('stringa: ')
distanza=0
for c in s:
    dsx=s.find(c)
    ddx=s.rfind(c)
    distanza=max(distanza, ddx-dsx)
print(distanza)
