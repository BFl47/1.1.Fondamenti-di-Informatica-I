def Ex1(l,x,y):
    includi=False
    ris=l 
    corrente=[] 
    for elem in l:
        if elem==x:
            corrente=[x] 
            includi=True
        elif elem==y and includi:
            corrente.append(y)
            if len(corrente)<len(ris): 
                ris=corrente 
                includi=False
        elif includi:
            corrente.append(elem) 
    return ris
    
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione
    
    counter_test_positivi += tester_fun(Ex1, [[1,2,2,0,3,1,3,4,2,1,7,3],2,3],[2,0,3])
    counter_test_positivi += tester_fun(Ex1, [[4,5,2,3,6],2,5],[4, 5, 2, 3, 6])
    counter_test_positivi += tester_fun(Ex1, [[0,3,4,6,2,3,1,2,5],3,2],[3,1,2])
    counter_test_positivi += tester_fun(Ex1, [[3,2,1,3,6,2,3],2,3],[2,3])
    counter_test_positivi += tester_fun(Ex1, [[7,5,4,3,6,9,10],4,9],[4,3,6,9])

    # test correzione

    counter_test_positivi += tester_fun(Ex1, [[11,8,8,10,9,11,9,4,8,11,17,9],8,9],[8,10,9])
    counter_test_positivi += tester_fun(Ex1, [[24,15,12,23,26],12,15],[24,15,12,23,26])
    counter_test_positivi += tester_fun(Ex1, [[10,6,8,12,4,6,1,4,5],6,4],[6,1,4])
    counter_test_positivi += tester_fun(Ex1, [[7,8,1,7,6,8,7],8,7],[8,7])
    counter_test_positivi += tester_fun(Ex1, [[7,5,1,3,8,11,10],1,11],[1,3,8,11])
    
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
