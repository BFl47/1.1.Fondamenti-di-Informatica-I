from tester import tester_fun

def B_Ex3(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    massimo = 0
    for parola in l:
        count = 0
        for c in parola:
            if c.islower():
                count += 1
        if count > massimo:
            massimo = count
    l1 = []
    for parola in l:
        l1.append(parola)
        count = 0
        for c in parola:
            if c.islower():
                count += 1
        if count == massimo:
            l1.append(parola)
    return l1
        
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, [["piPPo", "PIppO", "PLuto", "PiPPo"]] ,["piPPo", "piPPo", "PIppO","PLuto", "PLuto", "PiPPo"])
counter_test_positivi += tester_fun(B_Ex3, [["mamma", "pippo", "Pluto", "Pluto"]]  ,["mamma", "mamma", "pippo", "pippo", "Pluto", "Pluto"])
counter_test_positivi += tester_fun(B_Ex3, [["ACME", "ACM"]] ,["ACME","ACME", "ACM","ACM"])
counter_test_positivi += tester_fun(B_Ex3, [[""]] ,["",""])
counter_test_positivi += tester_fun(B_Ex3, [["ciao","ciao"]] ,["ciao","ciao","ciao","ciao"])

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

