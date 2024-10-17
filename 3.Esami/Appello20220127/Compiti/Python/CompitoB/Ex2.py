def Ex2(file,ins):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt',{'palloni','Marco','devono','viaggio'}],{'Marco':[3,1],'palloni':[3,2,1],'devono':[2]})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt',{'palloni','Marco','viaggio'}],{'palloni': [3,1], 'Marco': [2, 1]})
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt',{'Marco','arbitro','11'}],{'arbitro': [4, 1], '11': [3]})
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt',{'Mario','arbitri','122'}],{})
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt',{'Marco','fermata','222'}],{'222': [5, 4, 1], 'fermata': [4]})
    
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
