from tester import tester_fun

def D_Ex1(s,c,n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    ris = ''
    if n == 0:
        return s
    for i in range(len(s)):
        ris += s[i]
        if (i+1)%n == 0 and i != len(s)-1:
            ris += c
    return ris

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5 

counter_test_positivi += tester_fun(D_Ex1, ["abcdefghi","X",3],"abcXdefXghi")
counter_test_positivi += tester_fun(D_Ex1, ["abcdefghi","X",0],"abcdefghi")
counter_test_positivi += tester_fun(D_Ex1, ["abcdefghi","X",2],"abXcdXefXghXi")
counter_test_positivi += tester_fun(D_Ex1, ["123","X",1],"1X2X3")
counter_test_positivi += tester_fun(D_Ex1, ["a","a",0],"a")

print('La funzione',D_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
