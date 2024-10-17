#import re

def Ex2(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
##    f = open(file,'r',encoding='UTF-8').read()
##    d = {}
##    pattern = r'mailto:(\w+)@\w+.(\w+)'
##    ris = re.finditer(pattern,f)
##    for m in ris:
##        nome = m.group(1)
##        sigla = m.group(2)
##        if sigla not in ['com','org','net'] and len(sigla) > 1:
##            if sigla not in d:
##                d[sigla] = [nome]
##            else:
##                d[sigla].append(nome)
##                d[sigla].sort()
##    return d
##
    import re
    d = {}
    f = open(file,'r',encoding = 'UTF-8').read()
    pattern = r'mailto:(\w+)@\w+\.([a-z]+)'
    i = re.finditer(pattern, f)
    for m in i:
        nome = m.group(1)
        sigla = m.group(2)
        if sigla not in ['org','com','net']:
            if sigla not in d:
                d[sigla] = []
            d[sigla].append(nome)
            d[sigla].sort()
    return d
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt'],{'it':['domenico','maria'],'es':['marco']})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt'],{'it': ['anna','marco']})
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt'],{'usa':['dad','mom'], 'it':['giovanna','giovanna','marco']})
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt'],{})
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt'],{'uk':['boris','elizabeth'], 'it':['sergio']})

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
