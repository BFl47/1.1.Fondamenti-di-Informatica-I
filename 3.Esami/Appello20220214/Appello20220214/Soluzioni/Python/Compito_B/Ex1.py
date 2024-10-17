def Ex1(l,x,y):
    ris=[]
    aggiungo=False
    inseriti=0 # conto gli elementi inseriti. vanno poi eliminati se non trovo y dopo x
    for elem in l:
        if elem==x and not aggiungo:
            aggiungo=True
        elif elem==y:
            aggiungo=False
            inseriti=0 #azzero la lista di inseriti
        elif aggiungo:
            ris.append(elem)
            inseriti+=1
    return ris[:len(ris)-inseriti]


###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [[1,2,2,0,3,1,3,4,2,1,4,2,3],2,4],[2,0,3,1,3,1])
    counter_test_positivi += tester_fun(Ex1, [[1,2,0,3,4,2,1,0,3],1,0],[2])
    counter_test_positivi += tester_fun(Ex1, [[17,1,3,6,0,1,7,8,0,1,2],1,0],[3,6,7,8])
    counter_test_positivi += tester_fun(Ex1, [[3,4,2,5,78,2,9,0],2,4],[])
    counter_test_positivi += tester_fun(Ex1, [[1,2,3,4,5,1,2,3,4,5,6],1,5],[2,3,4,2,3,4])

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex1, [[1,2,2,0,3,1,3,4,2,1,4,2,3],2,3],[2, 0, 1, 4, 2])
    counter_test_positivi += tester_fun(Ex1, [[1,2,0,3,4,2,1,0,3],1,3],[2, 0, 0])
    counter_test_positivi += tester_fun(Ex1, [[17,1,3,6,0,1,7,8,0,1,2],3,2],[6, 0, 1, 7, 8, 0, 1])
    counter_test_positivi += tester_fun(Ex1, [[3,4,2,5,78,2,9,0],2,3],[])
    counter_test_positivi += tester_fun(Ex1, [[1,2,3,4,5,1,2,3,4,5,6],2,5],[3, 4, 3, 4])



    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
