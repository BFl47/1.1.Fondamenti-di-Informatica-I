from tester import tester_fun

def B_Ex3(file):
    accettati = 'abcdefghijklmnopqrstuvwxyz'
    f = open(file,'r',encoding='UTF-8')
    d = {}
    for riga in f:
        riga = riga.strip()
        primo = False
        i = 0
        while not primo:
            if riga[i] in accettati:
                primo = True
                if riga[i] not in d:
                    d[riga[i]] = [0,0] #primo riga, ultimo riga
                d[riga[i]][0] += 1
            i += 1
        ultimo = False
        j = -1
        while not ultimo:
            if riga[j] in accettati:
                ultimo = True
                if riga[j] not in d:
                    d[riga[j]] = [0,0]
                d[riga[j]][1] += 1
            j -= 1
    f.close()
    return d
        
        

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, ['file1.txt'],{'n': [1, 0], 'a': [0, 2], 'u': [1, 0], 'o': [0, 1], 's': [1, 0]})
counter_test_positivi += tester_fun(B_Ex3, ['file2.txt'],{'n': [1, 0], 'a': [1, 4], 'u': [2, 0], 'o': [0, 1], 's': [1, 0], 'e': [0, 1], 'v': [1, 0]})
counter_test_positivi += tester_fun(B_Ex3, ['file3.txt'],{'n': [1, 0], 'o': [0, 1], 's': [1, 0], 'e': [0, 1], 'u': [1, 0], 'a': [0, 1]})
counter_test_positivi += tester_fun(B_Ex3, ['file4.txt'],{'n': [1, 0], 'o': [0, 2], 's': [1, 0], 'e': [0, 1], 'u': [2, 0], 'a': [0, 3], 'l': [1, 0], 'p': [1, 0]})
counter_test_positivi += tester_fun(B_Ex3, ['file5.txt'],{'n': [1, 0], 'o': [0, 3], 's': [1, 0], 'e': [0, 1], 'u': [2, 0], 'a': [1, 4], 'l': [2, 0], 'p': [1, 0], 'i': [0, 1], 'c': [1, 0]})

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

