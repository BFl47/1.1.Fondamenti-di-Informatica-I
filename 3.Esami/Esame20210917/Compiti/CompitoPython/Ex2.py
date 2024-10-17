from tester import tester_fun

def Ex2(M,I):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    l=[]
##    for riga in M:
##        if sum(riga) == 0:
##            l.append(M.index(riga))
####    if len(l) == len(M):
####        return 0
##    for t in I:
##        c1 = t[0]
##        c2 = t[1]
##        if M[c1][c2] == 1:
##            M[c1][c2] == 0
##    navi_fin = 0
##    for riga in M: 
##        if sum(riga) == 0 and M.index(riga) not in l:
##            navi_fin += 1
##    print(l,navi_fin)

    affondate = 0
    righe = len(M)
    colonne = len(M[0])
    for i in range(righe):
        barca = set()
        for j in range(colonne):
            if M[i][j] == 1:
                barca.add((i,j))
                if j == colonne-1 or M[i][j+1] == 0:
                    if barca < I:
                        affondate += 1
            else:
                barca = set()
    return affondate
    
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex2,[[[0,1,1,0,1,0],[0,0,0,1,1,0],[0,0,0,1,1,1]],{(0,1),(0,2),(1,3),(1,0),(2,3),(2,4),(2,5)}],2)
counter_test_positivi += tester_fun(Ex2,[[[1,1,1],[0,1,0],[0,0,0],[1,0,1]],{(0,0),(0,1),(0,2),(1,0),(1,1),(2,2),(3,0),(3,2)}],4)
counter_test_positivi += tester_fun(Ex2,[[[1,1,1],[0,1,0],[0,0,0],[1,0,1]],{(0,1),(0,2),(1,2),(2,2),(3,1)}],0)
counter_test_positivi += tester_fun(Ex2,[[[0,0],[0,1],[1,1]],{(0,0),(1,1),(2,1)}],1)
counter_test_positivi += tester_fun(Ex2,[[[0,0,0],[0,0,0],[0,0,0]],{(0,0),(0,1),(0,2),(1,0),(2,2)}],0)

print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
