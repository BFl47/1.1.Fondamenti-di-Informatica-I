from tester import tester_fun

def B_Ex2(m):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    righe = len(m)
    colonne = len(m[0])
    count = 0
    for j in range(colonne):
        col = []
        for i in range(righe):
            col.append(m[i][j])
        for i in range(righe):
            if sum(col) == sum(m[i]):
                count += 1
    return count
###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex2, [[[1,3,4,5],[2,3,4,2],[1,7,3,3]]] ,2)
counter_test_positivi += tester_fun(B_Ex2, [[[1,3,4,5],[2,3,4,2],[1,7,3,3],[10,0,0,5]]] ,4)
counter_test_positivi += tester_fun(B_Ex2, [[[1,3,4,5],[2,5,4,2],[1,7,3,3]]] ,0)
counter_test_positivi += tester_fun(B_Ex2, [[[1,3,4,5],[2,3,4,2],[1,7,5,3],[8,0,0,5]]] ,4)
counter_test_positivi += tester_fun(B_Ex2, [[[1,1,1],[1,1,1],[1,1,1]]] ,9)

print('La funzione',B_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
