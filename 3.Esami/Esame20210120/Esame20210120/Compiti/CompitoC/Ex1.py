def Ex1(l1,l2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    ins=set()
##    for parola1 in l1:
##        for parola2 in l2:
##            if len(parola1) == len(parola2):
##                count = 0
##                listacar1 = list(parola1)
##                for c in parola2:
##                    if c in listacar1:
##                        count += 1
##                if count == len(parola1):
##                    ins.add(parola2)
##    for parola2 in l2:
##        for parola1 in l1:
##            if len(parola1) == len(parola2):
##                count = 0
##                listacar2 = list(parola2)
##                for c in parola1:
##                    if c in listacar2:
##                        count+=1
##                if count == len(parola2):
##                    ins.add(parola1)
##    return ins
    ins = set()
    for parola1 in l1:
        for parola2 in l2:
            if len(parola1) == len(parola2):
                count = 0
                for c in parola2:
                    if c in parola1:
                        count += 1
                if count == len(parola1):
                    ins.add(parola1)
                    ins.add(parola2)
    return ins
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex1, [['arco', 'pippo', 'pluto', 'corda'],['palla', 'darco', 'ocra', 'casa']],{'corda', 'darco', 'ocra', 'arco'})
    counter_test_positivi += tester_fun(Ex1, [['arco', 'pala', 'pluto', 'corda'],['palla', 'caro', 'ocra', 'casa']],{'caro', 'arco', 'ocra'})
    counter_test_positivi += tester_fun(Ex1, [['arco', 'pala', '', 'corda'],['palla', 'codarco', 'ocra', 'casa', '']],{'', 'arco', 'ocra'})
    counter_test_positivi += tester_fun(Ex1, [['arco', 'pala', '', 'corda', 'roccado'],['palla', 'codarco', 'ocra', 'casa']],{'codarco', 'arco', 'ocra', 'roccado'})
    counter_test_positivi += tester_fun(Ex1, [['pala', '', 'corda', 'rocca do'],['palla', 'co darco', 'ocra', 'casa']],{'rocca do', 'co darco'})

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
