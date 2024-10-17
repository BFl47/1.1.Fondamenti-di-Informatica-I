def Ex3(maxSpesa,file):
    ris = {}
    current_spesa = [0 for i in range(61)] # spesa mensile iniziale in ogni mese
    f = open(file,'r',encoding='UTF-8')
    for riga in f:
        dati = riga.strip().split(',')
        mese = int(dati[0])
        oggetto = dati[1]
        numrate = int(dati[2])
        imprata = int(dati[3])
        #print(current_spesa)
        if imprata + current_spesa[mese + 1] <= maxSpesa:
            ris[oggetto] = 'SI'
            for i in range(mese+1,mese+numrate+1):
                current_spesa[i] += imprata
        else:
            ris[oggetto] = 'NO'
    return ris

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, [200,'offerte1.csv'],{'Moto': 'SI', 'Casco': 'SI', 'Cappotto': 'NO', 'Guanti': 'SI', 'Sci': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [180,'offerte1.csv'],{'Moto': 'SI', 'Casco': 'SI', 'Cappotto': 'NO', 'Guanti': 'SI', 'Sci': 'NO'})
    counter_test_positivi += tester_fun(Ex3, [200,'offerte2.csv'],{'Moto': 'SI', 'Casco': 'SI', 'Cappotto': 'NO', 'Guanti': 'SI', 'Maglione': 'SI', 'Scarpe': 'SI', 'Sci': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [260,'offerte2.csv'],{'Moto': 'SI', 'Casco': 'SI', 'Cappotto': 'SI', 'Guanti': 'NO', 'Maglione': 'NO', 'Scarpe': 'SI', 'Sci': 'NO'})
    counter_test_positivi += tester_fun(Ex3, [180,'offerte3.csv'],{'Moto': 'SI', 'Casco': 'SI', 'Cappotto': 'NO', 'Pantaloni': 'SI', 'Guanti': 'SI', 'Maglione': 'SI', 'Scarpe': 'SI', 'Sci': 'NO'})

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, [200,'offerte3.csv'],{'Moto': 'SI', 'Casco': 'SI', 'Cappotto': 'NO', 'Pantaloni': 'SI', 'Guanti': 'SI', 'Maglione': 'SI', 'Scarpe': 'SI', 'Sci': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [180,'offerte4.csv'],{'Auto': 'SI', 'Casco': 'SI', 'Cappotto': 'NO', 'Sciarpa': 'SI', 'Sci': 'NO'})
    counter_test_positivi += tester_fun(Ex3, [200,'offerte4.csv'],{'Auto': 'SI', 'Casco': 'SI', 'Cappotto': 'NO', 'Sciarpa': 'SI', 'Sci': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [260,'offerte5.csv'],{'Auto': 'SI', 'Casco': 'SI', 'Cappotto': 'SI', 'Sciarpa': 'NO', 'Maglione': 'NO', 'Scarpe': 'SI', 'Sci': 'NO'})
    counter_test_positivi += tester_fun(Ex3, [180,'offerte5.csv'],{'Auto': 'SI', 'Casco': 'SI', 'Cappotto': 'NO', 'Sciarpa': 'SI', 'Maglione': 'SI', 'Scarpe': 'SI', 'Sci': 'NO'})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
