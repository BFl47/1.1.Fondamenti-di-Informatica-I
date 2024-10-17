from tester import tester_fun

def C_Ex3(l1,l2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    l = []
    for i in range(len(l1)):
        parola1 = l1[i]
        parola2 = l2[i]
        count = 0
        s = ''
        for c in parola1:
            if c in parola2 and c not in s:
                s += c
        l.append(parola1)
        l.append(len(s))
    return l
                
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex3, [["mamma", "asso", "re", "pluto"],["mare", "lago", "fante", "barba"]] ,["mamma", 2, "asso", 2, "re", 1, "pluto", 0])
counter_test_positivi += tester_fun(C_Ex3, [["","aaa"],["regina","fante"]] ,["",0,"aaa",1])
counter_test_positivi += tester_fun(C_Ex3, [["re","regina","cavallo"],["re","cavallo","regina"]] ,["re",2,"regina",1,"cavallo",1])
counter_test_positivi += tester_fun(C_Ex3, [["","aaa"],["","aaa"]] ,["",0,"aaa",1])
counter_test_positivi += tester_fun(C_Ex3, [["Marea"],["marea"]],["Marea",3])

print('La funzione',C_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

