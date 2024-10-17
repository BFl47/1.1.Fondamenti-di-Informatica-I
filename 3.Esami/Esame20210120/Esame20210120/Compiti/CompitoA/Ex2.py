

def Ex2(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    import re
##    f = open(file,'r',encoding='UTF-8').read()
##    pattern = r'\d\d\d-?(\d\d)-?\d\d\d-?\d\d\d\d-?\d'
##    i = re.finditer(pattern,f)
##    d={}
##    for m in i:
##        numero = m.group().replace('-','')
##        lingua = m.group(1)
##            
##        somma = 0
##        for i in range(len(numero)):
##            cifra = int(numero[i])
##            if i % 2 == 0:
##                somma += cifra
##            else:
##                somma += cifra*3    
##        if somma % 10 == 0:
##            d[lingua]=d.get(lingua,0)+1
##    
##    return d

    import re
    f = open(file,'r',encoding='UTF-8').read()
    pattern = r'\d\d\d-?(\d\d)-?\d\d\d-?\d\d\d\d-?\d'
    i = re.finditer(pattern,f)
    d = {}
    for m in i:
        numero = m.group(0).replace('-','')
        lingua = m.group(1)
        somma = 0
        for i in range(len(numero)):
            cifra = int(numero[i])
            if i % 2 == 0:
                somma += cifra
            else:
                somma += cifra*3
        if somma % 10 == 0:
            d[lingua] = d.get(lingua,0) + 1
    return d
        
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt'],{'88': 1, '78': 1})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt'],{'88': 2, '78': 1})
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt'],{'88': 2, '78': 2, '15': 1})
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt'],{'88': 2, '78': 2, '15': 1, '05': 1})
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt'],{'88': 1, '78': 1, '15': 1, '05': 1})

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
