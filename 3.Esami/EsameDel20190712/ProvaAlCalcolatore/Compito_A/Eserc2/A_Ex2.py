from tester import tester_fun

def A_Ex2(M,s):
    righe = len(M)
    colonne = len(M[0])
    for i in range(righe):
        riga = ''
        for j in range(colonne):
            riga += M[i][j]
        if s in riga:
            return True       
    for j in range(colonne):
        col = ''
        for i in range(righe):
            col += M[i][j]
        if s in col:
            return True
    return False



###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [[['a','m','o'],['r','e','a'],['i','d','i'],['a','x','a']],'amo'],True)
counter_test_positivi += tester_fun(A_Ex2, [[['a','m','o'],['r','e','a'],['i','d','i'],['a','x','a']],'aria'],True)
counter_test_positivi += tester_fun(A_Ex2, [[['a','m','o'],['r','e','a'],['i','d','i'],['a','x','a']],'aia'],True)
counter_test_positivi += tester_fun(A_Ex2, [[['a','m','o'],['r','e','a'],['i','d','i'],['a','x','a']],'amore'],False)
counter_test_positivi += tester_fun(A_Ex2, [[['a']],'c'],False)

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
