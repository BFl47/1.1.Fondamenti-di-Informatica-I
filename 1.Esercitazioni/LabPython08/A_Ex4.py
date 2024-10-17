from tester import tester_fun

def A_Ex5(l):
##        ins=set()
##        lista=[]
##        for s in l:
##                num=l.count(s)
##                lista=[s,num]
##                t=tuple(lista)
##                ins.add(t)
##        return ins

        ins=set()
        for elem in l:
                count=l.count(elem)
                t=(elem,count)
                ins.add(t)
        return ins
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, [['jkl', 'h', 'plqa', 'jkl', 'h', 'xkj']] , {('jkl',2), ('h',2), ('plqa',1), ('xkj',1)})
    counter_test_positivi += tester_fun(A_Ex5, [[]] , set())
    counter_test_positivi += tester_fun(A_Ex5, [['a', 'ab', 'abc']] , {('a', 1), ('ab', 1), ('abc', 1)})
    counter_test_positivi += tester_fun(A_Ex5, [['e', 'a', 'e', 'lp', 'a', 'ql', 'cl']] ,  {('e', 2), ('a', 2), ('lp', 1), ('ql', 1), ('cl', 1)} )
    counter_test_positivi += tester_fun(A_Ex5, [['hjkl', 'hjkl']] , {('hjkl', 2)})


    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

