from tester import tester_fun

def B_Ex1(s1,s2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    s1inv = s1[::-1]
    s2inv = s2[::-1]
    lung = min(len(s1),len(s2))
    ris = ''
    i = 0
    while i < lung and s1inv[i] == s2inv[i]:
        ris += s1inv[i]
        i += 1
    return len(ris)
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex1, ["arciere","pompiere"], 4)
counter_test_positivi += tester_fun(B_Ex1, ["arciere","pippo"], 0)
counter_test_positivi += tester_fun(B_Ex1, ["","pompiere"] , 0)
counter_test_positivi += tester_fun(B_Ex1, ["ma","mamma"] , 2)
counter_test_positivi += tester_fun(B_Ex1, ["reggimento","mento"] , 5)

print('La funzione',B_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
