def Ex1(l1,l2,n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    count = 0
##    for parola1 in l1:
##        for parola2 in l2:
##            trovato = False
##            for i in range(len(parola1)-n+1):
##                if parola1[i:i+n] in parola2:
##                    trovato = True
##            if trovato:
##                count +=1
##    
##    return count

    count = 0
    for parola1 in l1:
        for parola2 in l2:
            trovato = False
            for i in range(len(parola1)-n+1):
                if parola1[i:i+n] in parola2:
                    trovato = True
            if trovato:
                count += 1
    return count
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [['arciere', 'pippo', 'accordare'],['arco', 'pappa', 'corda'],3],2)
    counter_test_positivi += tester_fun(Ex1, [['arciere', 'pippo', 'accordare'],['corda', 'arco', 'pappa', 'ippopotamo'],3],3)
    counter_test_positivi += tester_fun(Ex1, [['lanciere', 'ceppo', 'accordarsi'],['corda', 'arco', 'pappa', 'ippopotamo'],4],1)
    counter_test_positivi += tester_fun(Ex1, [['lanciatore', 'ceppo', 'accordarsi'],['corda', 'arco', 'pappa', 'ippopotamo','sciatore'],4],2)
    counter_test_positivi += tester_fun(Ex1, [['lanciere', 'ceppo', 'accordarsi'],['corda', 'arco', 'pappa', 'ippopotamo'],1],12)
                
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
