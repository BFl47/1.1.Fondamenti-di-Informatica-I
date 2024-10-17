def Ex3(file,l):
    competenze = {}
    f = open(file,'r',encoding='UTF-8')
    for riga in f:
        dati = riga.strip().split(',')
        nome = dati[0]
        comp = dati[1]
        disp = int(dati[2])
        costo = int(dati[3])
        if comp not in competenze:
            competenze[comp] = [[nome,disp,costo]]
        else:
            competenze[comp].append([nome,disp,costo])
    f.close()
    ris = {}
    comps = l[0::2]
    numGior = l[1::2]
    costo = 0
    for i in range(len(comps)):
        ris[comps[i]] = 'Nessuno'
        minimo = 2000
        if comps[i] in competenze:
            for elem in competenze[comps[i]]:
                if elem[1] >= numGior[i] and elem[2] < minimo:
                    minimo = elem[2]
                    ris[comps[i]] = elem[0]
            costo += minimo * numGior[i]
    return ris

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['competenze1.csv',['Java',60,'Python',10,'DataBases',40]],{'Java': 'Carlo', 'Python': 'Flavia', 'DataBases': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['competenze1.csv',['Java',20,'MachineLearning',10]],{'Java': 'Flavia', 'MachineLearning': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['competenze1.csv',['Java',20,'Python',60,'MachineLearning',10]],{'Java': 'Flavia', 'Python': 'Nessuno', 'MachineLearning': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['competenze2.csv',['Java',20,'Python',10]],{'Java': 'Flavia', 'Python': 'Flavia'})
    counter_test_positivi += tester_fun(Ex3, ['competenze2.csv',['Java',20,'Python',50,'DataBases',40,'MachineLearning',10]],{'Java': 'Flavia', 'Python': 'Flavia', 'DataBases': 'Nessuno', 'MachineLearning': 'Gianni'})

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, ['competenze3.csv',['C++',20,'Lisp',10]],{'C++': 'Francesca', 'Lisp': 'Francesca'})
    counter_test_positivi += tester_fun(Ex3, ['competenze3.csv',['C++',20,'Lisp',10,'MachineLearning',10]],{'C++': 'Francesca', 'Lisp': 'Francesca', 'MachineLearning': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['competenze3.csv',['C++',20,'Lisp',60,'MachineLearning',10]],{'C++': 'Francesca', 'Lisp': 'Nessuno', 'MachineLearning': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['competenze4.csv',['C++',20,'Lisp',10,'MachineLearning',50]],{'C++': 'Francesca', 'Lisp': 'Gianni', 'MachineLearning': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['competenze4.csv',['C++',20,'Lisp',60,'MachineLearning',10]],{'C++': 'Francesca', 'Lisp': 'Gianni', 'MachineLearning': 'Nessuno'})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
