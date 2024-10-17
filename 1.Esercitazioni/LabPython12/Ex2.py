import re

def Ex2(i,file):
##    f=open(file,'r',encoding='UTF-8')
##    s=f.read()
##    f.close()
##    pattern=r'\W*([00]|\+)(\d\d?\d?)-?\d{3}-?\d{5}\b\W*'
##    d={}
##    for elem in i:
##        d[elem]=0
##    ins=re.finditer(pattern, s)
##    for m in ins:
##        preint=m.group(2)
##        parola=''
##        for car in preint:
##            if car!='0':
##                parola+=car
##        if parola in d:
##            d[parola]+=1
##    return d
    
    f=open(file,'r',encoding='UTF-8')
    s=f.read()
    f.close()
    pattern=r'\W*([00]|\+)(\d\d?\d?)-?\d{3}-?\d{5}\b\W*'
    d={}
    for elem in i:
        d[elem]=0
    ins=re.finditer(pattern,s)
    for m in ins:
        preint=m.group(2)
        parola=''
        for car in preint:
            if car!='0':
                parola+=car
        if parola in d:
            d[parola]+=1
    return d
        
            
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex2, [{'39','351','34'},'testo1.txt'],{'39':2,'351':1,'34':0})
    counter_test_positivi += tester_fun(Ex2, [{'1','351'},'testo2.txt'],{'1':3,'351':1})
    counter_test_positivi += tester_fun(Ex2, [{'39','351','34','1'},'testo3.txt'],{'1':0,'351':0,'34':0,'39':2})
    counter_test_positivi += tester_fun(Ex2, [{'39','44','661','9'},'testo6.txt'],{'661': 1, '39': 2, '9': 1, '44': 2})
    counter_test_positivi += tester_fun(Ex2, [set(),'testo6.txt'],{})
    
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
