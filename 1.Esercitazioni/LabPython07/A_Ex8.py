def A_Ex8(s1,s2):
##    s=''
##    if s1=='' or s2=='':
##        return s
##    lun=min(len(s1),len(s2))
##    for i in range(lun):
##        if s1[i]==s2[i]:
##            s+=s1[i]
##        if s1[i]!= s2[i]:
##            return s    
##    return s

    s=''
    if s1=='' or s2=='':
        return s
    lun=min(len(s1),len(s2))
    for i in range(lun):
        if s1[i]==s2[i]:
            s+=s1[i]
        else:
            return s
    return s

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, ['amaca','amaranto'], 'ama')
    counter_test_positivi += tester_fun(A_Ex8, ['asso','assolato'], 'asso')
    counter_test_positivi += tester_fun(A_Ex8, ['','stringa'], '')
    counter_test_positivi += tester_fun(A_Ex8, ['stringa',''], '')
    counter_test_positivi += tester_fun(A_Ex8, ['ciao mamma','ciao '], 'ciao ')

    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
