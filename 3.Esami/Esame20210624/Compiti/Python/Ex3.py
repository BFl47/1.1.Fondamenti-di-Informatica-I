from tester import tester_fun

def Ex3(diz,file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    f = open(file,'r',encoding='UTF-8')
##    for riga in f:
##        riga = riga.strip().split(',')
##        nome = riga[0]
##        territorio1 = riga[1]
##        territorio2 = riga[2]
##        attaccante = diz[nome]
##        for key in diz:
##            if territorio2 in diz[key]:
##                attaccato = diz[key]
##        if (territorio1 in attaccante) and (territorio2 not in attaccante):
##            if attaccante[territorio1] > attaccato[territorio2]:
##                attaccante[territorio2] = attaccante[territorio1] - attaccato[territorio2]
##                attaccante[territorio1] = 1
##                attaccato.pop(territorio2)
##            else:
##                attaccante[territorio1] = 1
##    f.close()
##    return diz

    f = open(file,'r',encoding='UTF-8')
    for riga in f:
        riga = riga.strip().split(',')
        nome = riga[0]
        territorio1 = riga[1]
        territorio2 = riga[2]
        attaccante = diz[nome]
        for key in diz:           
            if territorio2 in diz[key]:
                attaccato = diz[key]
        if (territorio1 in attaccante) and (territorio2 not in attaccante):
            if attaccante[territorio1] > attaccato[territorio2]:
                attaccante[territorio2] = attaccante[territorio1] - attaccato[territorio2]
                attaccante[territorio1] = 1
                attaccato.pop(territorio2)
            else:
                attaccante[territorio1] = 1
    f.close()
    return diz      
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex3, [{'Paolo': {'Italia':5, 'Francia':3}, 'Anna': {'Germania':6}, 'Giorgio': {'Spagna':2,'Austria': 1}},'mossa1.csv'] ,{'Paolo': {'Italia': 1, 'Spagna': 3}, 'Anna': {'Germania': 1, 'Francia': 3}, 'Giorgio': {'Austria': 1}})
counter_test_positivi += tester_fun(Ex3, [{'Paolo': {'Italia':5, 'Francia':3}, 'Anna': {'Germania':6}, 'Giorgio': {'Spagna':2,'Austria': 1}},'mossa2.csv'] ,{'Paolo': {'Francia': 3, 'Spagna': 3}, 'Anna': {'Germania': 1, 'Italia': 5}, 'Giorgio': {'Austria': 1}})
counter_test_positivi += tester_fun(Ex3, [{'Paolo': {'Italia':3, 'Francia':3}, 'Anna': {'Germania':6}, 'Giorgio': {'Spagna':2,'Austria': 1}},'mossa2.csv'] ,{'Paolo': {'Francia': 3, 'Spagna': 1}, 'Anna': {'Germania': 1, 'Italia': 5}, 'Giorgio': {'Austria': 1}})
counter_test_positivi += tester_fun(Ex3, [{'Paolo': {'Italia':3, 'Francia':3}, 'Anna': {'Germania':6}, 'Giorgio': {'Spagna':2,'Austria': 1}},'mossa3.csv'] ,{'Paolo': {'Francia': 3, 'Spagna': 1}, 'Anna': {'Germania': 1, 'Italia': 5}, 'Giorgio': {'Austria': 1}})
counter_test_positivi += tester_fun(Ex3, [{'Paolo': {'Italia':5, 'Francia':3}, 'Anna': {'Germania':4}, 'Giorgio': {'Spagna':3,'Austria': 1}},'mossa3.csv'] ,{'Paolo': {'Francia': 3, 'Spagna': 2}, 'Anna': {'Germania': 1, 'Italia': 3}, 'Giorgio': {'Austria': 1}})

print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

            
    

