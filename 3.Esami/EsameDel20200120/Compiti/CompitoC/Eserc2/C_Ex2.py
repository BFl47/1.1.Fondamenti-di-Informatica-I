from tester import tester_fun

def C_Ex2(m):
    """Inserite qui la vostra soluzione"""
    righe = len(m)
    costmag = 0
    magica = True
    for i in range(righe):
        costmag += m[i][i]
    for i in range(righe):
        if sum(m[i]) != costmag:
            magica = False
    for j in range(righe):
        col = []
        for i in range(righe):
            col.append(m[i][j])
        if sum(col) != costmag:
            magica = False
    return magica,costmag
            
        
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""
"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex2, [[[2,7,6],[9,5,1],[4,3,8]]], (True,15))
counter_test_positivi += tester_fun(C_Ex2, [[[1,0,0],[1,5,0],[0,0,-1]]], (False, 5))
counter_test_positivi += tester_fun(C_Ex2, [[[7,12,1,14],[2,13,8,11],[16,3,10,5],[9,6,1,4]]], (False,34))
counter_test_positivi += tester_fun(C_Ex2, [[[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]], (True,34))
counter_test_positivi += tester_fun(C_Ex2, [[[1,14,14,4],[11,7,6,9],[8,10,10,5],[13,2,3,15]]], (True,33))

print('La funzione',C_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
