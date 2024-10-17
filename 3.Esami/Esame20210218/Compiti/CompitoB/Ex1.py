def Ex1(s,l):
        """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##        ris = set()
##        for parola in l:
##                count = 0
##                if len(parola) == len(s):
##                        for car in parola:
##                                if car in s:
##                                        count += 1
##                if count == len(parola)-1:
##                        ris.add(parola)
##        return ris

        ris = set()
        for parola in l:
                count = 0
                if len(s) == len(parola):
                        for c in parola:
                                if c in s:
                                        count += 1
                        
                if count == len(parola)-1:
                        ris.add(parola)
        return ris             
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, ['malta',['marea','malia','alta','molta']],{'malia','molta'})
    counter_test_positivi += tester_fun(Ex1, ['morto',['giorno','notte','botte']],set())
    counter_test_positivi += tester_fun(Ex1, ['morto',['molto','mosto','porto']],{'molto','mosto','porto'})
    counter_test_positivi += tester_fun(Ex1, ['a',['a','b','c','d']],{'b','c','d'})
    counter_test_positivi += tester_fun(Ex1, ['asse',['atte','basse','asso','asta']],{'asso'})
    
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
