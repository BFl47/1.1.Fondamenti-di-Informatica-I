def Ex1(m):
##    righe=len(m)
##    colonne=len(m[0])
##    massimo=0
##    for i in range(righe):
##        l=[]
##        for j in range(colonne):
##            if m[i][j]==0:
##                l.append(0)
##            if m[i][j]==1:
##                contazeri=len(l)
##                l=[]
##        contazeri=max(contazeri,len(l))    
##        if contazeri>=massimo:
##            massimo=contazeri
##    return massimo

    righe=len(m)
    colonne=len(m[0])
    massimo=0
    for i in range(righe):
        l=[]
        for j in range(colonne):
            if m[i][j]==0:
                l.append(0)
            if m[i][j]==1:
                count=len(l)
                l=[]
        count=max(count,len(l))
        if count>=massimo:
            massimo=count
    return massimo

        
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex1, [[[1,0,0,1,0],[0,0,0,1,0],[1,0,0,0,0],[1,1,1,0,0]]] , 4)
    counter_test_positivi += tester_fun(Ex1, [[[1,0,0,1,0],[0,0,0,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,0,0,1,0]]] , 4)
    counter_test_positivi += tester_fun(Ex1, [[[1,0,0,1,0],[0,0,0,1,0],[1,0,1,0,0],[1,1,0,1,1],[1,0,0,1,0]]] , 3)
    counter_test_positivi += tester_fun(Ex1, [[[1,0,0,1,0],[0,0,0,1,0],[1,0,1,0,1],[1,1,0,1,0],[1,0,0,1,0]]] , 3)
    counter_test_positivi += tester_fun(Ex1, [[[1,0,0],[0,1,1],[1,0,1],[1,1,0]]] , 2)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
