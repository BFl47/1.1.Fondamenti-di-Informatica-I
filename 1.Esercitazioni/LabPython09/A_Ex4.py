def A_Ex4(l):
##    d={}
##    if len(l)==0:
##        return d
##    
##    for elem in l:
##        d[elem]=l.count(elem)
##            
##    return d
##
    d={}
    if len(l)==0:
        return d
    for parola in l:
        d[parola]=l.count(parola)
    return d
    
 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, [['casa','orso','cane','casa','orso','casa']] , {'casa': 3, 'orso': 2, 'cane': 1})
    counter_test_positivi += tester_fun(A_Ex4, [['casa','casa','casa']] , {'casa': 3})
    counter_test_positivi += tester_fun(A_Ex4, [['casa','orso','cane','cassa','osso','casta']] , {'casa': 1, 'orso': 1, 'cane': 1, 'cassa': 1, 'osso': 1, 'casta': 1})
    counter_test_positivi += tester_fun(A_Ex4, [['casa']] , {'casa': 1})
    counter_test_positivi += tester_fun(A_Ex4, [[]] , {})

    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
