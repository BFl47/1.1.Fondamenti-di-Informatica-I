def Ex2(l,s,t):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, [['caste','pesta','paste','pance'],'pinza',(2,0,0,0,1)],['paste'])
    counter_test_positivi += tester_fun(Ex2, [['caste','cesta','pesta','pance'],'pinza',(2,0,0,0,1)],[])
    counter_test_positivi += tester_fun(Ex2, [['carte','sorta','sarte'],'folte',(0,2,0,2,0)],['sorta'])
    counter_test_positivi += tester_fun(Ex2, [['croce','astro','torsa'],'sorta',(1,1,1,1,1)],['astro'])
    counter_test_positivi += tester_fun(Ex2, [['clero','diego','truce','frego','pesto'],'testo',(0,1,0,0,2)],['clero','diego','frego'])
    
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
