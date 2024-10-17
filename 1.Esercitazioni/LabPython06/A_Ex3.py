from tester import tester_fun

def A_Ex3(s):
##    car_ug_cifra=False
##    i=0
##    for c in s:
##        car=int(c)
##        if car==i:
##            car_ug_cifra=True
##            return car_ug_cifra
##        i+=1
##    return car_ug_cifra
##
    uguale=False
    i=0
    for c in s:
        car=int(c)
        if car==i:
            uguale=True
            return uguale
        i+=1
    return uguale


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ['223367'],True)
counter_test_positivi += tester_fun(A_Ex3, ['1234567890'],False)
counter_test_positivi += tester_fun(A_Ex3, ['2211003367'],False)
counter_test_positivi += tester_fun(A_Ex3, ['1234567899'],True)
counter_test_positivi += tester_fun(A_Ex3, ['2234567'],False)

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
