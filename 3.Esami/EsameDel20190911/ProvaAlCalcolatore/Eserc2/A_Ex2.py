from tester import tester_fun

def A_Ex2(M):
    righe = len(M)
    colonne = len(M[0])
    l = []
    for i in range(righe):
        for j in range(colonne):
            l.append(M[i][j])
    l.sort()
    k = 0
    for i in range(righe):
        for j in range(colonne):
            M[i][j] = l[k]
            k += 1
    return M    
    

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [[[3,4,3],[2,1,2]]],[[1,2,2],[3,3,4]])
counter_test_positivi += tester_fun(A_Ex2, [[[3,4,3],[2,1,2],[0,-2,7]]],[[-2,0,1],[2,2,3],[3,4,7]])
counter_test_positivi += tester_fun(A_Ex2, [[[9,8,7],[6,5,4],[3,2,1],[0,-1,-2]]],[[-2,-1,0],[1,2,3],[4,5,6],[7,8,9]])
counter_test_positivi += tester_fun(A_Ex2, [[[5,5,5],[4,4,4]]],[[4,4,4],[5,5,5]])
counter_test_positivi += tester_fun(A_Ex2, [[[2],[1]]],[[1],[2]])

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
