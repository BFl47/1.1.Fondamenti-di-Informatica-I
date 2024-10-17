def A_Ex6(fileName):
##    fin=open(fileName,encoding='UTF-8')
##    d={}
##    pos=0
##    for riga in fin:
##        l=riga.strip().split(',')
##        pos+=1
##
##        for elem in l:
##            key=int(elem)
##            if key in d:
##                d[key].add(pos)
##            else:
##                d[key]=set([pos])
##            #if key not in d:
##            #    d[key]=set()
##            #d[key].add(pos)
##            
##    fin.close()
##    return d
##            

    f=open(fileName,'r',encoding='UTF-8')
    d={}
    count=0
    for riga in f:
        riga=riga.strip().split(',')
        count+=1
        for num in riga:
            key=int(num)
            if key in d:
                d[key].add(count)
            else:
                d[key]=set()
                d[key].add(count)
    f.close()
    return d

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['numeri1.txt'] , {10: {1,2}, -5: {1,2}, 0: {1}, 8: {2}, -3: {2}})
    counter_test_positivi += tester_fun(A_Ex6, ['numeri2.txt'] , {10: {1,2}, 0: {2}})
    counter_test_positivi += tester_fun(A_Ex6, ['numeri3.txt'] , {3: {1,2}, 4: {1}, 5: {1}, 2: {2,3}, 0: {2,3}})
    counter_test_positivi += tester_fun(A_Ex6, ['numeri4.txt'] , {2: {1,2,3,4,5}, 1: {1,2,6}, 3: {6}})
    counter_test_positivi += tester_fun(A_Ex6, ['numeri5.txt'] , {})

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
