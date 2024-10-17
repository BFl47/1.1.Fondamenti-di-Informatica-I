from tester import tester_fun

def A_Ex7(b1,b2):
##    lun=max(len(b1),len(b2))
##    if len(b1)<len(b2):
##        b1=b1+('0'*(len(b2)-len(b1)))
##    elif len(b2)<len(b1):
##        b2=b2+('0'*(len(b1)-len(b2)))
##        
##    s=''
##    for i in range(0,lun):
##        if (b1[i] == b2[i]) and (b1[i] == '1'):
##            s+='1'
##        else:
##            s+='0'
##    return s
    lung=max(len(b1),len(b2))
    if len(b1)<len(b2):
        b1+=('0'*(len(b2)-len(b1)))
    elif len(b1)>len(b2):
        b2+=('0'*(len(b1)-len(b2)))

    s=''
    for i in range(lung):
        if b1[i]==b2[i]=='1':
            s+='1'
        else:
            s+='0'
    return s

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex7, ['1011','100'],'1000')
counter_test_positivi += tester_fun(A_Ex7, ['','111'],'000')
counter_test_positivi += tester_fun(A_Ex7, ['1','1'],'1')
counter_test_positivi += tester_fun(A_Ex7, ['111','10'],'100')
counter_test_positivi += tester_fun(A_Ex7, ['1010',''],'0000')

print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)




