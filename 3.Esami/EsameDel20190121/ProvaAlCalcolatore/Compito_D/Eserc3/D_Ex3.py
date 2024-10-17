from tester import tester_fun

def D_Ex3(l1,l2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    l = []
    ris = []
    for parola in l2:
        nuova = ''
        nuova = parola[1:] + parola[0]
        l.append(nuova)
    for i in range(len(l1)):
        if l1[i] == l[i]:
            ris.append(l1[i])
    ris.sort()
    return ris
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(D_Ex3, [["mamma", "asso", "re"],["amamm", "lago", "er"]],["mamma", "re"])
counter_test_positivi += tester_fun(D_Ex3, [["sara","osso"],["asar","ooss"]],["osso","sara"])
counter_test_positivi += tester_fun(D_Ex3, [["sara"],["rasa"]],[])
counter_test_positivi += tester_fun(D_Ex3, [["a"],["a"]],["a"])
counter_test_positivi += tester_fun(D_Ex3, [["a"],["A"]],[])

print('La funzione',D_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
