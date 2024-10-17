def Ex2(m):
    ris={}
    for i in range(len(m)):
        for j in range(len(m[0])-1):
            c=m[i][j]
            selezionato=True
            for k in range(j+1,len(m[0])):
                    if c<=m[i][k]:
                       selezionato=False
                       break
            if selezionato:
                ris[c]=ris.get(c,set()) | {(i,j)}
    return ris   
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, [[[1,10,4,5],[10,7,8,9],[7,8,7,6]]],{10:{(0,1),(1,0)},8:{(2,1)},7:{(2,2)}})
    counter_test_positivi += tester_fun(Ex2, [[[0,1,2,3],[4,5,6,7]]],{})
    counter_test_positivi += tester_fun(Ex2, [[[3,2,1,0],[3,2,1,0]]],{3:{(1,0),(0,0)},2:{(0,1),(1,1)},1:{(0,2),(1,2)}})
    counter_test_positivi += tester_fun(Ex2, [[[3,2,3,2,3,2]]],{3:{(0,4)}})
    counter_test_positivi += tester_fun(Ex2, [[[5,5],[5,4],[5,3],[3,2]]],{5:{(1,0),(2,0)},3:{(3,0)}})    

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex2, [[[1,12,4,5],[12,7,8,9],[7,8,7,6]]],{12:{(0,1),(1,0)},8:{(2,1)},7:{(2,2)}})
    counter_test_positivi += tester_fun(Ex2, [[[0,1,2,5],[4,5,6,8]]],{})
    counter_test_positivi += tester_fun(Ex2, [[[4,2,1,0],[4,2,1,0]]],{4:{(1,0),(0,0)},2:{(0,1),(1,1)},1:{(0,2),(1,2)}})
    counter_test_positivi += tester_fun(Ex2, [[[4,2,4,2,4,2]]],{4:{(0,4)}})
    counter_test_positivi += tester_fun(Ex2, [[[6,5],[6,4],[6,3],[3,2]]],{6: {(1, 0), (2, 0), (0, 0)}, 3: {(3, 0)}})    
 
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
