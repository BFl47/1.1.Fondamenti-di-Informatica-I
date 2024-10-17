def Ex2(i,file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""        
    import re
##    
##    f = open(file,'r',encoding='UTF-8').read()
##    pattern = r'\W*(\+|00)(\d\d?\d?)-?\d\d\d-?\d\d\d\d\d\W*'
##    ms = re.finditer(pattern, f)
##    d = {}
##    for elem in i:
##        d[elem] = 0
##    for m in ms:
##        pre = m.group(2)
##        if pre in d:
##            d[pre] += 1
##    return d

    d = {}
    for elem in i:
        d[elem] = 0
    f = open(file,'r',encoding='UTF-8').read()
    pattern = r'\W*(00|[+])-?(\d?\d?\d)-?\d\d\d-?\d\d\d\d\d\W*'
    i = re.finditer(pattern, f)
    for m in i:
        prefisso = m.group(2)
        if prefisso in d:
            d[prefisso] += 1
    return d
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex2, [{'39','351','34'},'testo1.txt'],{'39':2,'351':1,'34':0})
    counter_test_positivi += tester_fun(Ex2, [{'1','351'},'testo2.txt'],{'1':3,'351':1})
    counter_test_positivi += tester_fun(Ex2, [{'39','351','34','1'},'testo3.txt'],{'1':0,'351':0,'34':0,'39':2})
    counter_test_positivi += tester_fun(Ex2, [{'351','34'},'testo3.txt'],{'351':0,'34':0})
    counter_test_positivi += tester_fun(Ex2, [{'7','1'},'testo4.txt'],{'7':2,'1':2})

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
