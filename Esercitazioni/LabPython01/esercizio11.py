##c = input('Inserire un carattere: ')
##c = str(c)
##n = input('Inserire un intero positivo: ')
##n = int(n)
##l = c*n
##print((l+'\n')*(n - 1) +l)

c=str(input('carattere: '))
n=int(input('intero: '))
lato=c*n+'\n'
quad=lato*(n-1)+lato.strip()
print(quad)
