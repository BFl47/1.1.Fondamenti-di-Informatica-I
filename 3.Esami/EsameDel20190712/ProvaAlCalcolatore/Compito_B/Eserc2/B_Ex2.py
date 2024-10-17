from tester import tester_fun

def B_Ex2(M,s):
    n = len(M)
    n = len(M[0])
    diag1 = ''
    diag2 = ''
    for i in range(n):
        for j in range(n):
            if i == j:
                diag1 += M[i][j]
            if (i+j) == (n-1):
                diag2 += M[i][j]
    if s in diag1 or s in diag2:
        return True
    return False
 



###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex2, [[['a','m','o','r'],['r','i','o','y'],['i','s','a','x'],['a','s','t','a']],'rosa'],True)
counter_test_positivi += tester_fun(B_Ex2, [[['a','m','o','r'],['r','i','o','y'],['i','s','a','x'],['a','s','t','a']],'aia'],True)
counter_test_positivi += tester_fun(B_Ex2, [[['a','m','o','r'],['r','i','o','y'],['i','s','a','x'],['a','s','t','a']],'rosato'],False)
counter_test_positivi += tester_fun(B_Ex2, [[['a','m'],['a','m']],'ma'],True)
counter_test_positivi += tester_fun(B_Ex2, [[['a']],'b'],False)


print('La funzione',B_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
