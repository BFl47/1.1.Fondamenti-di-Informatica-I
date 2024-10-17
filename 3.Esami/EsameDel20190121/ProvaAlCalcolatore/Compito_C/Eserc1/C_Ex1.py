from tester import tester_fun

def C_Ex1(s1, s2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    s2inv = s2[::-1]
    lung = min(len(s1),len(s2))
    s = ''
    i = 0
    while i < lung:
        s = s + s1[i] + s2inv[i]
        i += 1
    for c in s1:
        if c not in s:
            s += c
    for c in s2:
        if c not in s:
            s += c
    return s
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5 

counter_test_positivi += tester_fun(C_Ex1, ["abcd","xyefgh"] , "ahbgcfdexy")
counter_test_positivi += tester_fun(C_Ex1, ["abcd","ef"] , "afbecd")
counter_test_positivi += tester_fun(C_Ex1, ["abc","abc"] , "acbbca")
counter_test_positivi += tester_fun(C_Ex1, ["xyz","a"] , "xayz")
counter_test_positivi += tester_fun(C_Ex1, ["a","b"] , "ab")

print('La funzione',C_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
