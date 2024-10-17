from tester import tester_fun

def simil(s1,s2):
    lung = min(len(s1),len(s2))
    count = 0
    for i in range(lung):
        if s1[i] == s2[i]:
            count += 1
    return count
    
def A_Ex2(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    massimo = 0
    for parola1 in l:
        for parola2 in l:
            if parola1 != parola2 and simil(parola1,parola2) > massimo:
                massimo = simil(parola1,parola2)
    return massimo
                

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [['casa','palla','freno','cosa']] ,3)
counter_test_positivi += tester_fun(A_Ex2, [['casale','pallae','freno','treno']] ,4)
counter_test_positivi += tester_fun(A_Ex2, [['cascata','pallone','caserma','freno','qualcuno', 'qualcosa']] ,5)
counter_test_positivi += tester_fun(A_Ex2, [['cascata','pallone','caserma','freno','qualcuno', 'qualcosa','palloni']] ,6)
counter_test_positivi += tester_fun(A_Ex2, [['cascata','pilone','frase']] ,0)

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
