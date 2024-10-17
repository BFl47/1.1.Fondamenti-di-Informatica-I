def Ex3(file1,file2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
###############################################################################
##    f1 = open(file1, 'r', encoding = 'UTF-8')
##    menu = {}
##    for riga in f1:
##        riga = riga.strip().split(',')
##        piatto = riga[0]
##        costo = int(riga[1])
##        disp = int(riga[2])
##        menu[piatto] = [disp, costo]
##    f1.close()
##    
##    f2 = open(file2, 'r', encoding = 'UTF-8')
##    ris = {}
##    for riga in f2:
##        riga = riga.strip().split(',')
##        nome = riga[0]
##        ris[nome] = 0
##        riga.remove(nome)
##        respinto = False
##        for ordine in riga:
##            ordine = ordine.strip().split(':')
##            quant = int(ordine[1])
##            piatto = ordine[0]
##            totq = int(menu[piatto][0])
##            if totq - quant >= 0 and not respinto:
##                ris[nome] += (menu[piatto][1] * quant)
##                menu[piatto][0] -= quant
##            else:
##                ris[nome] = 'respinto'
##                respinto = True
##    f2.close()
##    return ris

    ris = {}
    menu = {} #menu[piatto] = [costo,disp]
    f1 = open(file1,'r',encoding='UTF-8')
    for riga in f1:
        riga = riga.strip().split(',')
        piatto = riga[0]
        costo = int(riga[1])
        disp = int(riga[2])
        menu[piatto] = [costo,disp]
    f1.close()    
    f2 = open(file2,'r',encoding='UTF-8')
    for riga in f2:
        riga = riga.strip().split(',')
        nome = riga[0]
        ris[nome] = 0
        riga.remove(nome)
        commanda = {}
        for ordine in riga:
            ordine = ordine.strip().split(':')
            piatto = ordine[0]
            quant = int(ordine[1])
            commanda[piatto] = quant
        respinto = False
        for ordine in commanda:
            if commanda[ordine] > menu[piatto][1]:
                respinto = True
        if not respinto:
            for ordine in commanda:
                ris[nome] += (commanda[ordine]*menu[ordine][0])
                menu[ordine][1] -= commanda[ordine]
        else:
            ris[nome] = 'respinto'
    f2.close()
    return ris
                
"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, ['menu1.csv','ordini1.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66})
    counter_test_positivi += tester_fun(Ex3, ['menu1.csv','ordini2.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66, 'Daniele': 36})
    counter_test_positivi += tester_fun(Ex3, ['menu2.csv','ordini3.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66, 'Daniele': 36, 'Fabio': 'respinto'})
    counter_test_positivi += tester_fun(Ex3, ['menu2.csv','ordini4.csv'],{'Giorgio': 68, 'Paola': 55, 'Francesca': 66, 'Daniele': 36, 'Fabio': 'respinto'})
    counter_test_positivi += tester_fun(Ex3, ['menu2.csv','ordini5.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66, 'Daniele': 36, 'Fabio': 'respinto', 'Carlo': 30})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
