def Ex3(file1,file2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
##    info = {}
##    d = {}
##    
##    f1 = open(file1, 'r', encoding = 'UTF-8')
##    for riga in f1:
##        riga = riga.strip().split(',')
##        pc = riga[0]
##        disp = int(riga[1])
##        costo = int(riga[2])
##        caratt = riga[3:]
##        info[pc] = [disp, costo, caratt]
##    f1.close()
##
##    f2 = open(file2, 'r', encoding = 'UTF-8')
##    for riga in f2:
##        riga = riga.strip().split(',')
##        cliente = riga[0]
##        prezzomax = int(riga[1])
##        carattR = riga[2:]
##        costomin = prezzomax
##        pcmin = None
##        for pc in info:
##            if info[pc][0] > 0 and info[pc][1] <= costomin:
##                ok = True
##                for car in carattR:
##                    if car not in info[pc][2]:
##                        ok = False
##                if ok:
##                    costomin = info[pc][1]
##                    pcmin = pc
##        if pcmin != None:
##            d[cliente] = (pcmin, info[pcmin][1])
##            info[pcmin][0] -= 1    
##    f2.close()
##
##    return d

    listino = {}
    f1 = open(file1,'r',encoding='UTF-8')
    for riga in f1:
        riga = riga.strip().split(',')
        pc = riga[0]
        disp = int(riga[1])
        costo = int(riga[2])
        caratt = riga[3:]
        listino[pc] = [disp,costo,caratt]
    f1.close()
    d = {}
    f2 = open(file2,'r',encoding='UTF-8')
    for riga in f2:
        riga = riga.strip().split(',')
        nome = riga[0]
        bud = int(riga[1])
        carattR = riga[2:]
        costomin = bud
        pcmin = None
        for pc in listino:
            if listino[pc][0] > 0 and listino[pc][1] <= costomin:
                ok = True
                for car in carattR:
                    if car not in listino[pc][2]:
                        ok = False
                if ok:
                    costomin = listino[pc][1]
                    pcmin = pc
        if pcmin != None:
            d[nome] = (pcmin,listino[pcmin][1])
            listino[pcmin][0] -= 1
    f2.close()

    return d
                       
   
    
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, ['listino1.csv','ordini1.csv'],{'Giorgio': ('Samsung', 399), 'Paola': ('Acer', 349),'Francesca':('Acer',349)})
    counter_test_positivi += tester_fun(Ex3, ['listino1.csv','ordini2.csv'],{'Giorgio': ('Samsung', 399), 'Paola': ('Acer', 349)})
    counter_test_positivi += tester_fun(Ex3, ['listino1.csv','ordini3.csv'],{'Paola': ('Acer', 349), 'Francesca': ('Samsung', 399)})
    counter_test_positivi += tester_fun(Ex3, ['listino2.csv','ordini2.csv'],{'Giorgio': ('Huawei', 250), 'Paola': ('Acer', 349), 'Francesca': ('Huawei', 250)})
    counter_test_positivi += tester_fun(Ex3, ['listino2.csv','ordini3.csv'],{'Paola': ('Acer', 349), 'Francesca': ('Huawei', 250)})


    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
