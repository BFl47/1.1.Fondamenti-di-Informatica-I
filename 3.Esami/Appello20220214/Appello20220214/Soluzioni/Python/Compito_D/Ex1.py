def Ex1(l):
    maxlung = 0
    for i in range(2,len(l)):
        lung = 2
        for j in range(i,len(l)):
            if l[j-2]+l[j-1] == l[j]:
                lung += 1
            else: break
        if lung>2 and lung > maxlung:
            maxlung = lung
    return maxlung
    

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione
    
    counter_test_positivi += tester_fun(Ex1, [[7,3,10,2,5,7,12,3]],4)
    counter_test_positivi += tester_fun(Ex1, [[1,1,1,2,2,3,1,4,5,9]],5)
    counter_test_positivi += tester_fun(Ex1, [[1,3,5,7,11,19]],0)
    counter_test_positivi += tester_fun(Ex1, [[1,3,4,7,11,18,2,3,5,1]],6)
    counter_test_positivi += tester_fun(Ex1, [[10,1,2,3,1,4,2,9]],3)

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex1, [[8,3,11,3,6,9,15,3]],4)
    counter_test_positivi += tester_fun(Ex1, [[0,1,1,2,3,1,4,5,9]],5)
    counter_test_positivi += tester_fun(Ex1, [[1,3,5,7,12,19]],4)
    counter_test_positivi += tester_fun(Ex1, [[1,3,4,7,11,18,2,3,6,1]],6)
    counter_test_positivi += tester_fun(Ex1, [[10,1,1,3,1,4,2,9]],3)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
