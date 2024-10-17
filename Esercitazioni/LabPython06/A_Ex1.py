from tester import tester_fun

def A_Ex1(s):
##    freq_max=0
##    s1=''
##    for c in s:
##        freq=s.count(c)
##        freq_max=max(freq_max, freq)
##    for c in s:
##        if (s.count(c) == freq_max) and (c not in s1):
##            s1+=c
##    return s1

    freqmax=0
    s1=''
    for c in s:
        freq=s.count(c)
        freqmax=max(freqmax, freq)
    for c in s:
        if (s.count(c)==freqmax) and (c not in s1):
            s1+=c
    return s1

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ['caso palese'] ,'ase')
counter_test_positivi += tester_fun(A_Ex1, ['caso palesemente'] ,'e')
counter_test_positivi += tester_fun(A_Ex1, ['caso palese zitto'] ,'aso et')
counter_test_positivi += tester_fun(A_Ex1, ['aca'] ,'a')
counter_test_positivi += tester_fun(A_Ex1, [''] ,'')

print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
