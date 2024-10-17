from tester import tester_fun

def A_Ex6(s):
##        freq_max=0
##        for c in s:
##                if ord(c)>=ord('A') and ord(c)<=ord('Z'):
##                        freq_car=s.count(c)
##                        freq_max=max(freq_max,freq_car)
##        return freq_max
        freqm=0
        for c in s:
                if ord(c)>=ord('A') and ord(c)<=ord('Z'):
                        freqcar=s.count(c)
                        freqm=max(freqm,freqcar)
        return freqm
                        
	
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex6, ['aHa^^&^HH'], 3)
counter_test_positivi += tester_fun(A_Ex6, [''], 0)
counter_test_positivi += tester_fun(A_Ex6, ['&&YH&Y'], 2)
counter_test_positivi += tester_fun(A_Ex6, ['stri%$p'], 0)
counter_test_positivi += tester_fun(A_Ex6, ['CIAO'], 1)

print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

###############################################################################

