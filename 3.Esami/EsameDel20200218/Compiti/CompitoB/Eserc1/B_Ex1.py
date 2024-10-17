from tester import tester_fun

def B_Ex1(s):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    s1 = ''
    i = 0
    while i < len(s):
        car = s[i]
        j = i
        count = 0
        finito = False
        while j < len(s) and not finito:
            if s[i] == s[j]:
                count += 1
                j += 1
            else:
                finito = True
        i = j       
        s1 = s1 + str(count) + car
    return s1
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex1, ["WWWWEERWWRRRFF"] , "4W2E1R2W3R2F")
counter_test_positivi += tester_fun(B_Ex1, ["sTTTFFL"] , "1s3T2F1L")
counter_test_positivi += tester_fun(B_Ex1, [""] , "")
counter_test_positivi += tester_fun(B_Ex1, ["a"] , "1a")
counter_test_positivi += tester_fun(B_Ex1, ["aaaahhajjllhhhh"] , "4a2h1a2j2l4h")

print('La funzione',B_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
