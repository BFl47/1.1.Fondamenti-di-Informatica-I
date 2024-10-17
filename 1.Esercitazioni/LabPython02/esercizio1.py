##hh=int(input('Inserisci il numero di ore: '))
##mm=int(input('Inserisci il numero di minuti: '))
##ss=int(input('Inserisci il numero di secondi: '))
##
##s_tot=(hh*60)*60+mm*60+ss 
##
##print('Il numero totale di secondi è: ',s_tot)

hh=int(input('ore: '))
mm=int(input('minuti: '))
ss=int(input('secondi: '))

m_tot= hh*60 + mm
s_tot= m_tot*60 + ss
print(s_tot)
