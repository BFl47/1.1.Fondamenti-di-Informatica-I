from tester import tester_fun

#import re

def Ex2(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    ins = set()
##    f = open(file,'r',encoding='UTF-8')
##    testo = f.read()
##    pattern = r'\b(\w)\w*(ab|bc|cd|de|ef|fg|gh|hi|ij|jk|kl|lm|mn|no|op|pq|qr|rs|st|tu|uv|vw|wx|xy|yz)\w*\1\b'
##    ris = re.finditer(pattern,testo)
##    f.close()
##    for m in ris:
##        parola = m.group(0)
##        ins.add(parola)
##    return ins

    import re
    ris = set()
    f = open(file,'r',encoding='UTF-8').read()
    pattern = r'\b(\w)\w*(ab|bc|cd|de|ef|fg|gh|hi|ij|jk|kl|lm|mn|no|op|pq|qr|rs|st|tu|uv|vw|wx|xy|yz)\w*\1\b'
    i = re.finditer(pattern,f)
    for m in i:
        parola = m.group(0)
        ris.add(parola)
    return ris
        
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex2, ['file1.txt'] ,{'ostico', 'astuta', 'abracadabra'})
counter_test_positivi += tester_fun(Ex2, ['file2.txt'] ,{'acaba', 'arsa', 'alma'})
counter_test_positivi += tester_fun(Ex2, ['file3.txt'] ,{'inoltrati', 'aruva'})
counter_test_positivi += tester_fun(Ex2, ['file4.txt'] ,set())
counter_test_positivi += tester_fun(Ex2, ['file5.txt'] ,{'oxyzwo', 'eebcdeee', 'astratta', 'gghhgg'})


print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

           
    
