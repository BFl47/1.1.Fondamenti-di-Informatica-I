from tester import tester_fun

def A_Ex3(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    l1 = l.copy()
    massimo = 0
    for parola in l:
        count = 0
        for c in parola:
            if c.isupper():
                count += 1
        if count > massimo:
            massimo = count
    for parola in l:
        count = 0
        for c in parola:
            if c.isupper():
                count += 1
        if count == massimo:
            l1.remove(parola)
    return l1
        

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, [["piPPo", "pippo","PLuto","Pippo"]],["pippo","Pippo"])
counter_test_positivi += tester_fun(A_Ex3, [["Maria", "mamma","Monica"]] ,["mamma"])
counter_test_positivi += tester_fun(A_Ex3, [["","questa è una stringa"]] ,[])
counter_test_positivi += tester_fun(A_Ex3, [["Ciao","ciao"]] ,["ciao"])
counter_test_positivi += tester_fun(A_Ex3, [["gennaio","FEbbraio","Marzo"]] ,["gennaio","Marzo"])

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
