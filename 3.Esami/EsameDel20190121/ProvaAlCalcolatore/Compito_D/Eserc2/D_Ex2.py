from tester import tester_fun

def D_Ex2(m):
 """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 righe = len(m)
 somma = 0
 for i in range(righe):
     for j in range(righe):
         if m[i][j] != m[j][i]:
             return -1
         if i != j and m[i][j] > 0:
             somma += m[i][j]
 return somma
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5 

counter_test_positivi += tester_fun(D_Ex2, [[[0,-1,3],[-1,5,5],[3,5,0]]] , 16)
counter_test_positivi += tester_fun(D_Ex2, [[[0,-1,3],[-1,5,5],[3,-5,0]]] , -1)
counter_test_positivi += tester_fun(D_Ex2, [[[0,-1,3,3],[-1,5,5,2],[3,5,0,1],[3,5,0,1]]] , -1)
counter_test_positivi += tester_fun(D_Ex2, [[[1,1],[1,1]]] , 2)
counter_test_positivi += tester_fun(D_Ex2, [[[1]]] , 0)

print('La funzione',D_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
