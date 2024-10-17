from tester import tester_fun

def A_Ex4(s,n):
##    s1=''
##    for c in s:
##        if ord(c)%n==0 and not c in s1:
##            s1+=c
##    return s1
        
    ris=''
    for c in s:
        if ord(c)%n==0 and not c in ris:
            ris+=c
    return ris

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['stringa di prova',3],'rio')
counter_test_positivi += tester_fun(A_Ex4, ['stringa di prova',2],'trn dpv')
counter_test_positivi += tester_fun(A_Ex4, ['stringa di prova',5],'sind')
counter_test_positivi += tester_fun(A_Ex4, ['',1],'')
counter_test_positivi += tester_fun(A_Ex4, ['stringa di prova stringa di prova',4],'t dp')

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

