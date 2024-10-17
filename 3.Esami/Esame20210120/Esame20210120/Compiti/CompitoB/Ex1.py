def Ex1(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    ris=''
##    for lista in l:
##        s=''
##        massimo=0
##        piufreq=''
##        for parola in lista:
##            s+=parola
##        for car in s:
##            if s.count(car)>massimo:
##                massimo=s.count(car)
##                piufreq=car
##        ris+=piufreq
##    return ris
    ris = ''
    for sottolista in l:
        s = ''
        for parola in sottolista:
            s += parola
        massimo = 0
        for c in s:
            if s.count(c) > massimo:
                massimo = s.count(c)
        for c in s:
            if s.count(c) == massimo and c not in ris:
                ris += c
    return ris
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex1, [[['amare','mare','fermata'], ['accordare','fare','dire']]],"ar")
    counter_test_positivi += tester_fun(Ex1, [[["arciere","pippo","pluto"],["minnie","paperi"],["io","valle"]]],"pil")
    counter_test_positivi += tester_fun(Ex1, [[["arciere","pompiere","bere"]]],"e")
    counter_test_positivi += tester_fun(Ex1, [[["a"],["b"],["c"],["d"]]],"abcd")
    counter_test_positivi += tester_fun(Ex1, [[["mentolo","mentore","o"],["accidentaccio"],["assassino"]]],"ocs")


    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
