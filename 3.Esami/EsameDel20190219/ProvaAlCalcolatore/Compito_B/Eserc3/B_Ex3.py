from tester import tester_fun

def B_Ex3(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    accettati = 'AEIOUaeiou'
    f = open(file,'r',encoding='UTF-8')
    pos = 1
    d = {}
    for riga in f:
        riga = riga.strip().split()
        s = ''
        for parola in riga:
            s += parola
        minimo = 999
        for c in s:
            if c in accettati and s.count(c) < minimo:
                minimo = s.count(c)
        for c in s:
            if c in accettati and s.count(c) == minimo:
                if c not in d:
                    d[c] = []
                if pos not in d[c]:
                    d[c].append(pos)
        pos += 1
    return d
###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, ['file1.txt'],{'I': [1], 'A': [1], 'e': [1], 'u': [2, 3]})
counter_test_positivi += tester_fun(B_Ex3, ['file2.txt'],{'I': [1], 'A': [1], 'e': [1, 5], 'u': [2, 3, 5, 6], 'o': [4, 5]} )
counter_test_positivi += tester_fun(B_Ex3, ['file3.txt'],{'I': [1], 'A': [1], 'u': [1, 2, 3]})
counter_test_positivi += tester_fun(B_Ex3, ['file4.txt'],{'I': [1], 'A': [1, 4], 'u': [1, 2, 3, 4, 6], 'o': [5], 'e': [6]} )
counter_test_positivi += tester_fun(B_Ex3, ['file5.txt'],{'I': [1, 7, 8], 'A': [1, 4], 'u': [1, 2, 3, 4, 6, 8, 9], 'o': [5], 'e': [6]})

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

