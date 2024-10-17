def Ex5(file):
##    f=open(file,'r',encoding='UTF=8')
##    mat=[]
##    for riga in f:
##        riga=riga.strip()
##        riga=list(riga)
##        mat.append(riga)
##    f.close()
##    righe=len(mat)
##    colonne=len(mat[0])
##    quadlat=True
##    if righe!=colonne:
##        quadlat=False
##    for i in range(righe):
##        for j in range(colonne):
##            if mat[i].count(mat[i][j])!=1:
##                quadlat=False
##    return quadlat
    
    f=open(file,'r',encoding='UTF-8')
    mat=[]
    for riga in f:
        riga=riga.strip()
        riga=list(riga)
        mat.append(riga)
    f.close()
    righe=len(mat)
    colonne=len(mat[0])
    quadlat=True
    if righe!=colonne:
        quadlat=False
    for i in range(righe):
        for j in range(colonne):
            if mat[i].count(mat[i][j])!=1:
                quadlat=False
    return quadlat
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex5, ['file5_1.txt'] , True)
    counter_test_positivi += tester_fun(Ex5, ['file5_2.txt'] , False)
    counter_test_positivi += tester_fun(Ex5, ['file5_3.txt'] , False)
    counter_test_positivi += tester_fun(Ex5, ['file5_4.txt'] , True)
    counter_test_positivi += tester_fun(Ex5, ['file5_5.txt'] , False)

    print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
