def Ex2(m,s):
    ris={}
    for i in range(len(m)):
        for j in range(len(m[0])):
            c=m[i][j]
            selezionato=False
            if c in s:
                selezionato=True
                for k in range(0,len(s),2):
                    if c==s[k]:
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

    counter_test_positivi += tester_fun(Ex2, [[['a','r','d'],['d','b','r']],'fredda'],{'a':{(0,0)},'r':{(0,1),(1,2)}})
    counter_test_positivi += tester_fun(Ex2, [[['a','r','d'],['d','b','r']],'zorro'],{})
    counter_test_positivi += tester_fun(Ex2, [[['x','O','i'],['t','o','d'],['c','i','m']],'domenica'],{'o':{(1,1)},'i':{(0,2),(2,1)}})
    counter_test_positivi += tester_fun(Ex2, [[['x','o']],'oxford'],{'x':{(0,0)}})
    counter_test_positivi += tester_fun(Ex2, [[['x','O','e'],['a','o','d'],['c','i','o']],'arcobaleno'],{'e':{(0,2)},'o':{(1,1),(2,2)}})
    

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex2, [[['a','r','d'],['d','e','r']],'freddate'],{'a':{(0,0)},'r':{(0,1),(1,2)}})
    counter_test_positivi += tester_fun(Ex2, [[['a','r','d'],['d','b','r']],'zoaro'],{'r': {(0, 1), (1, 2)}})
    counter_test_positivi += tester_fun(Ex2, [[['x','O','i'],['t','o','d'],['c','i','m']],'sabato'],{'o': {(1, 1)}})
    counter_test_positivi += tester_fun(Ex2, [[['x','o']],'exford'],{'x': {(0, 0)}, 'o': {(0, 1)}})
    counter_test_positivi += tester_fun(Ex2, [[['x','O','e'],['a','o','d'],['c','i','o']],'sole'],{'e':{(0,2)},'o':{(1,1),(2,2)}})


    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
