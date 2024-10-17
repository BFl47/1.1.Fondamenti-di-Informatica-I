def Ex3(file):
##    f=open(file,'r',encoding='UTF=8')
##    mat=[]
##    dim=f.readline().split()
##    righe=int(dim[0])
##    colonne=int(dim[1])
##    for i in range(righe):
##        riga=f.readline().split()
##        for j in range(colonne):
##            riga[j]=int(riga[j])
##        mat.append(riga)
##    f.close()
##
##    massimo=0
##    for i in range(righe):
##        contoneg=0
##        for j in range(colonne):
##            if int(mat[i][j])<0:
##                contoneg+=1
##        if contoneg>=massimo:
##            ris=i
##            massimo=contoneg
##    return ris
    f=open(file,'r',encoding='UTF-8')
    dim=f.readline().split()
    righe=int(dim[0])
    colonne=int(dim[1])
    mat=[]
    for i in range(righe):
        riga=f.readline().split()
        for j in range(colonne):
            riga[j]=int(riga[j])
        mat.append(riga)
    f.close()

    massimo=0
    for i in range(righe):
        count=0
        for j in range(colonne):
            if int(mat[i][j])<0:
                count+=1
        if count>=massimo:
            ris=i
            massimo=count
    return ris

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, ["matrice1.txt"] , 3)
    counter_test_positivi += tester_fun(Ex3, ["matrice2.txt"] , 0)
    counter_test_positivi += tester_fun(Ex3, ["matrice3.txt"] , 1)
    counter_test_positivi += tester_fun(Ex3, ["matrice4.txt"] , 3)
    counter_test_positivi += tester_fun(Ex3, ["matrice5.txt"] , 4)

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
