def Ex3(disp,file):
    ris = {}
    current_disp = [disp for i in range(61)] # disponibilità iniziale in ogni mese
    f = open(file,'r',encoding='UTF-8')
    for riga in f:
        dati = riga.strip().split(',')
        mese = int(dati[0])
        cliente = dati[1]
        importo = int(dati[2])
        numrate = int(dati[3])
        imprata = int(dati[4])
        if importo <= current_disp[mese]:
            ris[cliente] = 'SI'
            for i in range(mese,61):
                current_disp[i] -= importo
            for i in range(mese+1,61):
                current_disp[i] += imprata * min(numrate,i-mese)
        else:
            ris[cliente] = 'NO'
    return ris

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, [10000,'prestiti1.csv'],{'Paola': 'SI', 'Flavio': 'SI', 'Gianna': 'NO', 'Francesco': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [15000,'prestiti1.csv'],{'Paola': 'SI', 'Flavio': 'SI', 'Gianna': 'SI', 'Francesco': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [10000,'prestiti2.csv'],{'Paola': 'SI', 'Flavio': 'SI', 'Gianna': 'NO', 'Paolo': 'SI', 'Piera': 'SI', 'Francesco': 'NO', 'Franca': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [15000,'prestiti2.csv'],{'Paola': 'SI', 'Flavio': 'SI', 'Gianna': 'SI', 'Paolo': 'SI', 'Piera': 'SI', 'Francesco': 'NO', 'Franca': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [12000,'prestiti2.csv'],{'Paola': 'SI', 'Flavio': 'SI', 'Gianna': 'SI', 'Paolo': 'SI', 'Piera': 'SI', 'Francesco': 'NO', 'Franca': 'SI'})

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, [10000,'prestiti3.csv'],{'Maria': 'SI', 'Flavio': 'SI', 'Gianni': 'NO', 'Paolo': 'SI', 'Francesco': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [12000,'prestiti3.csv'],{'Maria': 'SI', 'Flavio': 'SI', 'Gianni': 'SI', 'Paolo': 'SI', 'Francesco': 'NO'})
    counter_test_positivi += tester_fun(Ex3, [15000,'prestiti3.csv'],{'Maria': 'SI', 'Flavio': 'SI', 'Gianni': 'SI', 'Paolo': 'SI', 'Francesco': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [10000,'prestiti4.csv'],{'Maria': 'SI', 'Flavio': 'SI', 'Gianni': 'NO', 'Paolo': 'SI', 'Francesco': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [15000,'prestiti4.csv'],{'Maria': 'SI', 'Flavio': 'SI', 'Gianni': 'SI', 'Paolo': 'SI', 'Francesco': 'SI'})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
