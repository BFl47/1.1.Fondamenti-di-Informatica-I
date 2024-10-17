from tester import tester_fun

import re

def A_Ex3(file):
    f = open(file,'r',encoding='UTF-8')
    testo = f.read()
    f.close()
    d = {}
    pattern = r'<[a-z] ([a-z]*)=\'([A-Za-z0-9 ]*)\'>'
    i = re.finditer(pattern,testo)
    for m in i:
        attributo = m.group(1)
        dato = m.group(2)
        if attributo not in d:
            d[attributo] = set()
        d[attributo].add(dato)
    return d
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ["file1.txt"],{'nome': {'Marco Rossi', 'Mario Bianchi'},'indirizzo':{'viale dei Gladiatori'}})
counter_test_positivi += tester_fun(A_Ex3, ["file2.txt"],{'eta': {'30', '25'}, 'citta': {'Roma'}, 'auto': {'BMW'}})
counter_test_positivi += tester_fun(A_Ex3, ["file3.txt"],{'nome': {'Michele Bianchi'}, 'descrizione': {'Romaratona'}, 'posizione': {'1'}})
counter_test_positivi += tester_fun(A_Ex3, ["file4.txt"],{})
counter_test_positivi += tester_fun(A_Ex3, ["file5.txt"],{'eta': {'80'}, 'descrizione': {'Romaratona'}, 'posizione': {'789'}, 'stato': {'buono'}})

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

