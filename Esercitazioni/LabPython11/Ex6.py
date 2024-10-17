def Ex6(m):
##    righe=len(m)
##    colonne=len(m[0])
##    conto=0    
##    for i in range(1,righe-1): 
##        for j in range(1,colonne-1):
##            if m[i][j]<=m[i][j+1] and m[i][j]<=m[i][j-1] and m[i][j]<=m[i+1][j] and m[i][j]<=m[i-1][j] and m[i][j]<=m[i+1][j+1] and m[i][j]<=m[i+1][j-1] and m[i][j]<=m[i-1][j+1] and m[i][j]<=m[i-1][j-1]:
##                conto+=1
##    return conto

    righe=len(m)
    colonne=len(m[0])
    count=0
    for i in range(1,righe-1):
        for j in range(1,colonne-1):
            if m[i][j]<=m[i][j+1] and m[i][j]<=m[i][j-1] and m[i][j]<=m[i+1][j] and m[i][j]<=m[i-1][j] and m[i][j]<=m[i-1][j-1] and m[i][j]<=m[i-1][j+1] and m[i][j]<=m[i+1][j-1] and m[i][j]<=m[i+1][j+1]:
                count+=1
    return count


            
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex6, [[[3, 2, 0, 1], [4, 1, 2, 1], [2, 1, 3, 1], [2, 2, 2, 4], [3, 4, 2, 2]]] ,1)
    counter_test_positivi += tester_fun(Ex6, [[[3, 2, 0, 1, 2], [4, 1, 2, 1, 3], [2, 1, 3, 1, 1], [2, 2, 2, 4, 3], [3, 4, 2, 2, 2]]] , 2)
    counter_test_positivi += tester_fun(Ex6, [[[3, 2, 0], [3, 2, 3], [3, 2, 2], [2, 2, 4]]] , 1)
    counter_test_positivi += tester_fun(Ex6, [[[3, 2, 0, 1, 2, 2], [4, 1, 2, 1, 3, 2], [2, 1, 3, 1, 1, 4], [2, 2, 2, 4, 3, 3], [3, 4, 2, 2, 2, 4]]] ,3)
    counter_test_positivi += tester_fun(Ex6, [[[1]]] ,0)

    print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
