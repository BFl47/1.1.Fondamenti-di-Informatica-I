from tester import tester_fun
import re

def A_Ex3(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(file,'r',encoding='UTF-8')
    posriga = 1   
    d = {}
    for riga in f:
        riga = riga.strip().split()
        for parola in riga:
            if parola[0] == '*' and parola[-1] =='*' and parola.count('*') ==2:
                pulita = parola[1:-1]
                if pulita not in d:
                    d[pulita] = set()
                d[pulita].add(posriga)
        posriga +=1
    f.close()
    return d
        
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ["file1.txt"],{'testo': {1}, 'parole': {1, 2}, 'immagini': {3}, 'importanti': {3}})
counter_test_positivi += tester_fun(A_Ex3, ["file2.txt"],{'testo': {1, 4}, 'parole': {1, 2, 4, 5}, 'immagini': {3, 6}, 'importanti': {3, 6}})
counter_test_positivi += tester_fun(A_Ex3, ["file3.txt"],{'testo': {1, 3}, 'parole': {1, 2, 3, 4}, 'immagini': {5}, 'importanti': {5}})
counter_test_positivi += tester_fun(A_Ex3, ["file4.txt"],{'testo': {1, 4, 7}, 'parole': {1, 2, 4, 5, 7}, 'immagini': {3, 6}, 'importanti': {3, 6}})
counter_test_positivi += tester_fun(A_Ex3, ["file5.txt"],{'testo': {1, 4, 7}, 'parole': {1, 2, 4, 5, 7}, 'immagini': {3, 6}, 'importanti': {3, 6}})

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

