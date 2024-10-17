def Ex2(m):
    dim = len(m)
    if dim == 0:
        return 0
    if dim == 1:
        return m[0][0]
    maxSum = m[0][0] + m[0][1] + m[1][0] + m[1][1]
    for i in range(dim-1):
        for j in range(dim-1):
            somma = m[i][j] + m[i+1][j] + m[i][j+1] + m[i+1][j+1]
            if somma > maxSum:
                maxSum = somma
    return maxSum
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, [[[3,2,3,4],[2,2,1,4],[6,1,2,3],[1,1,1,1]]],12)
    counter_test_positivi += tester_fun(Ex2, [[[2,3,1],[1,2,2],[2,2,2]]],8)
    counter_test_positivi += tester_fun(Ex2, [[[-2,-3,-1],[-1,-2,-2],[-2,-2,2]]],-4)
    counter_test_positivi += tester_fun(Ex2, [[[3]]],3)
    counter_test_positivi += tester_fun(Ex2, [[]],0)

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex2, [[[4,5,3,4],[2,2,1,4],[6,1,2,3],[1,1,1,1]]],13)
    counter_test_positivi += tester_fun(Ex2, [[[2,3,1],[1,3,2],[2,-2,2]]],9)
    counter_test_positivi += tester_fun(Ex2, [[[-2,-3,-1],[-1,-2,-2],[-2,-2,2]]],-4)
    counter_test_positivi += tester_fun(Ex2, [[[3,2],[-2,-3]]],0)
    counter_test_positivi += tester_fun(Ex2, [[[-4,-5,-3],[3,5,4],[2,1,-4]]],11)

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
