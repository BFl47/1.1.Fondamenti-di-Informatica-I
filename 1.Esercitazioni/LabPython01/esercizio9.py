##a = input('Inserire un intero \'a\' diverso da 0: ')
##a = int(a)
##b = input('Inserire un intero \'b\': ')
##b = int(b)
##c = input('Inserire un intero \'c\': ')
##c = int(c)
##from math import sqrt
##d = sqrt(b**2 - (4*a*c))
##x1 = (-b + d)/(2 * a)
##x2 = (-b - d)/(2 * a)
##print('Le soluzioni di ax^2+bx+c=0 sono:\n', x1,'\n',x2)

import math

a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))

delta=math.sqrt(b**2-4*a*c)

x1=(-b-delta)/(2*a)
x2=(-b+delta)/(2*a)

print(x1,x2,sep='\n')
