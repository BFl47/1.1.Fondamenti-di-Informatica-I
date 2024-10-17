from tester import tester_fun

def B_Ex1(s1,s2):
###############################################################################
    if len(s1) != len(s2) or s1 == s2:
        return False
    s = ''
    for c in s1:
        if c in s2:
            s += c
    if len(s) == len(s1) - 1:
        return True

    
"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex1, ["amata","arata"],True)
counter_test_positivi += tester_fun(B_Ex1, ["blu","blue"],False)
counter_test_positivi += tester_fun(B_Ex1, ["osso","osso"],False)
counter_test_positivi += tester_fun(B_Ex1, ["antico","antica"],True)
counter_test_positivi += tester_fun(B_Ex1, ["",""],False)


print('La funzione',B_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
