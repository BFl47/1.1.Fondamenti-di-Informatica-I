from tester import tester_fun

def B_Ex1(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    ins = set()
    for parola in l:
        if l.index(parola) % 2 == 0:
            for i in range(len(parola)):
                if i % 2 != 0:
                    ins.add(parola[i])                    
        else:
            for i in range(len(parola)):
                if i % 2 == 0:
                    ins.add(parola[i])
    ris = list(ins)
    ris.sort()
    return ris
###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex1, [["mamma","sole","casa"]],['a', 'l', 'm', 's'])
counter_test_positivi += tester_fun(B_Ex1, [["mamma","sole","casa","sacco"]],['a', 'c', 'l', 'm', 'o', 's'])
counter_test_positivi += tester_fun(B_Ex1, [["pippo","castello","se"]],['c', 'e', 'i', 'l', 'p', 's'])
counter_test_positivi += tester_fun(B_Ex1, [[]],[])
counter_test_positivi += tester_fun(B_Ex1, [["assolo",""]],['o', 's'])


print('La funzione',B_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
