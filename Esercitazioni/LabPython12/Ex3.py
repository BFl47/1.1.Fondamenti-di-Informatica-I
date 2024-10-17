def Ex3(file1,file2):
##    f1=open(file1,'r',encoding='UTF-8')
##    f2=open(file2,'r',encoding='UTF-8')
##    menu={}
##    for riga in f1:
##        riga=riga.strip().split(',')
##        piatto=riga[0]
##        costo=int(riga[1])
##        disp=int(riga[2])
##        menu[piatto]=[disp,costo]
##    f1.close()
##    d={}
##    for ordine in f2:
##        ordine=ordine.strip().split(',')
##        nome=ordine[0]
##        d[nome]=0
##        ordine.remove(nome)
##        respinto=False
##        for elem in ordine:
##            elem=elem.strip().split(':')
##            quant=int(elem[1])
##            piatto=elem[0]
##            totq=int(menu[piatto][0])
##            if totq-quant>=0 and not respinto:
##                d[nome]+=(menu[piatto][1]*quant)
##                menu[piatto][0]-=quant
##            else:
##                d[nome]='respinto'
##                respinto=True
##    f2.close()
##    return d
        
    f1=open(file1,'r',encoding='UTF-8')
    f2=open(file2,'r',encoding='UTF-8')
    menu={}
    for riga in f1:
         riga=riga.strip().split(',')
         piatto=riga[0]
         costo=int(riga[1])
         disp=int(riga[2])
         menu[piatto]=[disp,costo]
    f1.close()
    d={}
    for ordine in f2:
        ordine=ordine.strip().split(',')
        nome=ordine[0]
        d[nome]=0
        ordine.remove(nome)
        respinto=False
        for elem in ordine:
            elem=elem.strip().split(':')
            quant=int(elem[1])
            piatto=elem[0]
            totq=int(menu[piatto][0])
            if totq-quant>=0 and not respinto:
                d[nome]+=(menu[piatto][1]*quant)
                menu[piatto][0]-=quant
            else:
                d[nome]='respinto'
                respinto=True
    f2.close()
    return d
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, ['menu1.csv','ordini1.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66})
    counter_test_positivi += tester_fun(Ex3, ['menu1.csv','ordini2.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66, 'Daniele': 36})
    counter_test_positivi += tester_fun(Ex3, ['menu2.csv','ordini3.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66, 'Daniele': 36, 'Fabio': 'respinto'})
    counter_test_positivi += tester_fun(Ex3, ['menu3.csv','ordini7.csv'],{'Giorgio': 'respinto', 'Paola': 'respinto', 'Francesca': 'respinto', 'Filippo': 'respinto'})
    counter_test_positivi += tester_fun(Ex3, ['menu3.csv','ordini9.csv'],{'Giorgio': 'respinto', 'Paola': 'respinto', 'Luca': 'respinto', 'Gino': 30})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
