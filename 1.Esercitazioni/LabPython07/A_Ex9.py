def A_Ex9(t):
##    lfin=[]
##    l=list(t)
##    for i in range(len(l)):
##        l1=list(l[i])
##        l1.sort()
##        massimo=0
##        piufreq=''
##        for c in l1:
##            if l1.count(c)>massimo:
##                piufreq=c
##                massimo=l1.count(c)
##        lfin.append(piufreq)
##    lfin.sort()
##    ins=set(lfin)
##    return ins

##    insieme=set()
##    for elem in t:
##        maxfreq=0
##        maxchar=''
##        for c in elem:
##            if elem.count(c)>maxfreq or (elem.count(c)==maxfreq and c<maxchar):
##                maxfreq=elem.count(c)
##                maxchar=c
##                
##        insieme.add(maxchar)
##    return insieme

    ins=set()
    for elem in t:
        maxfreq=0
        maxchar=''
        for c in elem:
            if elem.count(c)>maxfreq or (elem.count(c)==maxfreq and c<maxchar):
                maxfreq=elem.count(c)
                maxchar=c
        ins.add(maxchar)
    return ins
            
            

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex9, [('amaca','amaranto','rosso')], {'a','o'})
    counter_test_positivi += tester_fun(A_Ex9, [('osso','assolato','alto')], {'o','a'})
    counter_test_positivi += tester_fun(A_Ex9, [('stringa','a','bbbbcccc','dado')], {'d','a','b'})
    counter_test_positivi += tester_fun(A_Ex9, [('fosso','dosso','rosso','fosso')], {'o'})
    counter_test_positivi += tester_fun(A_Ex9, [('ciao mamma','ciao ')], {' ','a'})

    print('La funzione',A_Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
