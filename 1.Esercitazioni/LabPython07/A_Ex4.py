def A_Ex4(l):
##    s=''
##    for i in range(len(l)):
##        if l[i]%2==0:
##            s+='P'
##        else:
##            s+='D'
##    return s

    s=''
    for i in range(len(l)):
        if l[i]%2==0:
            s+='P'
        else:
            s+='D'
    return s

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, [[3,7,8,9]], 'DDPD')
    counter_test_positivi += tester_fun(A_Ex4, [[3]], 'D')
    counter_test_positivi += tester_fun(A_Ex4, [[8]], 'P')
    counter_test_positivi += tester_fun(A_Ex4, [[]], '')
    counter_test_positivi += tester_fun(A_Ex4, [[7,7,7,7,8]], 'DDDDP')

    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
