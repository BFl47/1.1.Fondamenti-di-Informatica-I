def Ex5(file):
##    fin=open(file,encoding='UTF-8')
##    d={}
##    d['invalidi']=0
##    d['domestici']=0
##    d['altri']=0
##    for riga in fin:
##        riga=riga.strip().split('.')
##        invalido=False
##        for num in riga:
##            if len(num)>3:
##                invalido=True
##            num=int(num)
##            if num<0 or num>255:        
##                invalido=True
##        if invalido:
##            d['invalidi']+=1
##        elif riga[0]=='192' and riga[1]=='168':
##            d['domestici']+=1
##        else:
##            d['altri']+=1
##    fin.close()    
##    return d
##                

    f=open(file,'r',encoding='UTF-8')
    d={}
    d['invalidi']=0
    d['domestici']=0
    d['altri']=0
    for riga in f:
        riga=riga.strip().split('.')
        invalido=False
        for num in riga:
            if len(num)>3:
                invalido=True
            num=int(num)
            if num<0 or num>255:
                invalido=True
        if invalido:
            d['invalidi']+=1
        elif riga[0]=='192' and riga[1]=='168':
            d['domestici']+=1
        else:
            d['altri']+=1
    f.close()
    return d

        
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex5, ["ip1.txt"] , {'invalidi': 0, 'domestici': 0, 'altri': 5})
    counter_test_positivi += tester_fun(Ex5, ["ip2.txt"] , {'invalidi': 2, 'domestici': 1, 'altri': 2})
    counter_test_positivi += tester_fun(Ex5, ["ip3.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
    counter_test_positivi += tester_fun(Ex5, ["ip4.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
    counter_test_positivi += tester_fun(Ex5, ["ip5.txt"] , {'invalidi': 3, 'domestici': 0, 'altri': 2})

    print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
