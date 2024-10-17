def Ex4(file):
##    fin=open(file,encoding='UTF-8')
##    header=fin.readline()
##    d={}
##    for riga in fin:
##        riga=riga.strip().split(',')
##        nome1=riga[0]
##        nome2=riga[1]
##        relazione=riga[2]
##        if relazione=='amici':
##            if nome1 not in d:
##                d[nome1]=[]
##            if nome2 not in d[nome1]:
##                d[nome1].append(nome2)
##            if nome2 not in d:
##                d[nome2]=[]
##            if nome1 not in d[nome2]:
##                d[nome2].append(nome1)
##            
##        else:
##            if nome1 in d and nome2 in d[nome1]:
##                d[nome1].remove(nome2)
##            if nome1 not in d:
##                d[nome1]=[]
##            if nome2 in d and nome1 in d[nome2]:
##                d[nome2].remove(nome1)
##            if nome2 not in d:
##                d[nome2]=[]
##            
##        d[nome1].sort()
##        d[nome2].sort()
##    fin.close()
##    return d
##                                 

    f=open(file,'r',encoding='UTF-8')
    header=f.readline()
    d={}
    for riga in f:
        riga=riga.strip().split(',')
        n1=riga[0]
        n2=riga[1]
        relazione=riga[2]
        if relazione=='amici':
            if n1 not in d:
                d[n1]=[]
            if n2 not in d[n1]:
                d[n1].append(n2)
            if n2 not in d:
                d[n2]=[]
            if n1 not in d[n2]:
                d[n2].append(n1)
        else:
            if n1 in d and n2 in d[n1]:
                d[n1].remove(n2)
            if n1 not in d:
                d[n1]=[]
            if n2 in d and n1 in d[n2]:
                d[n2].remove(n1)
            if n2 not in d:
                d[n2]=[]
        d[n1].sort()
        d[n2].sort()
    f.close()
    return d
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex4, ["amici1.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(Ex4, ["amici2.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria'], 'Maria': ['Anna'], 'Paola': [], 'Giorgio': []})
    counter_test_positivi += tester_fun(Ex4, ["amici3.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(Ex4, ["amici4.csv"] , {'Marco': ['Giorgio', 'Paolo'], 'Giorgio': ['Marco'], 'Paolo': ['Marco'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna']})
    counter_test_positivi += tester_fun(Ex4, ["amici5.csv"] , {'Marco': [], 'Giorgio': [], 'Paola': [], 'Anna': []})

    print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
