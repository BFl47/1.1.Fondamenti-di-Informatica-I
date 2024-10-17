import re

def Ex6(file):
##    fin=open(file,encoding='UTF=8')
##    pattern='[A-Z]{3} ?[A-Z]{3} ?(\d{2})([A-Z])(\d{2}) ?[A-Z]\d{3}[A-Z]'
##    l=[]
##    for riga in fin:
##        i=re.finditer(pattern,riga)
##        res=re.findall(pattern,riga)
##        codicecorretto=True
##        if len(res)==0:
##            l.append('Codice errato')
##            codicecorretto=False
##        if codicecorretto:
##            for m in i:
##                giorno=int(m.group(3))
##                mese=m.group(2)
##                anno=int(m.group(1))
##                mesi='ABCDEHLMPRST'
##                if anno<=20:
##                    veroanno='20'+str(anno)
##                else:
##                    veroanno='19'+str(anno)               
##                mesecorretto=True
##                if mese not in mesi:
##                    l.append('Mese errato')
##                    mesecorretto=False
##                if mesecorretto:
##                    veromese=mesi.find(mese) +1
##                    
##                    if veromese<10:
##                        veromese='0'+str(veromese)
##                    else:
##                        veromese=str(veromese)
##                    
##                    if giorno>40:
##                        verogiorno=giorno-40
##                    else:
##                        verogiorno=giorno
##                    if (mese in 'DHPS' and 1<=verogiorno<=30) or (mese in 'ACELMRT' and 1<=verogiorno<=31) or (mese=='B' and 1<=verogiorno<=28):
##                        if verogiorno<10:
##                            verogiorno='0'+str(verogiorno)
##                        else:
##                            verogiorno=str(verogiorno)
##                        data=verogiorno+'/'+veromese+'/'+veroanno
##                        l.append(data)
##                    else:
##                        l.append('Giorno errato')
##
##    fin.close()
##    return l

    f=open(file,'r',encoding='UTF-8')
    pattern='[A-Z]{3} ?[A-Z]{3} ?(\d{2})([A-Z])(\d{2}) ?[A-Z]\d{3}[A-Z]'
    mesi={'A': ['01',31],'B' : ['02',28],'C': ['03',31],'D' :['04',30],'E': ['05',30],'H': ['06',30],'L':['07',31],'M': ['08',31],'P': ['09',30],'R': ['10',31],'S': ['11',30],'T':['12',31]}
    l=[]
    for riga in f:
        riga=riga.strip()
        m=re.match(pattern,riga)
        if m==None:
            l.append('Codice errato')
        else:
            anno=int(m.group(1))
            mese=m.group(2)
            giorno=int(m.group(3))
            if anno <= 20:
                anno+=2000
            else:
                anno+=1900
            if mese not in mesi:
                l.append('Mese errato')
            else:
                maxgiorni=mesi[mese][1]
                mese=mesi[mese][0]
                if giorno>40:
                    giorno=giorno-40
                if giorno <1 or giorno>maxgiorni:
                    l.append('Giorno errato')
                else:
                    if giorno<10:
                        giorno='0'+str(giorno)
                    else:
                        giorno=str(giorno)
                    l.append(giorno+'/'+mese+'/'+str(anno))
    f.close()
    return l
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex6, ["codici1.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex6, ["codici2.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex6, ["codici3.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921'])
    counter_test_positivi += tester_fun(Ex6, ["codici4.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931'])
    counter_test_positivi += tester_fun(Ex6, ["codici5.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931', 'Codice errato', 'Giorno errato'])

    print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
