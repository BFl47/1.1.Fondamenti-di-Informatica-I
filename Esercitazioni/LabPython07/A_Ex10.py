def A_Ex10(i):
##    div5=[]
##    l=list(i)
##    for pos in range(len(l)):
##        if l[pos]%5==0:
##            div5.append(l[pos])
##    div5.sort()
##    tup=tuple(div5)
##    return tup


    d5=[]
    for elem in i:
        if elem%5==0:
            d5.append(elem)
    d5.sort()
    t=tuple(d5)
    return t
            

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex10, [{3,345,15,24,25,-10}], (-10,15,25,345))
    counter_test_positivi += tester_fun(A_Ex10, [set()], ())
    counter_test_positivi += tester_fun(A_Ex10, [{1,2,3}], ())
    counter_test_positivi += tester_fun(A_Ex10, [{5,10,0,-5,-10}], (-10,-5,0,5,10))
    counter_test_positivi += tester_fun(A_Ex10, [{100,50,-12,34,65}], (50,65,100))

    print('La funzione',A_Ex10.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
