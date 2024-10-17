import os

print("--- Registrazione Dati Studente ---")
completed = False
while not completed:
    print("\n")
    matricola = input("inserire MATRICOLA: ").strip()
    if not matricola.isdigit():
        print("\nMatricola non valida")
        continue
    print("\n")
    cognome = input("inserire COGNOME: ").strip().lower()
    print("\n")
    nome = input("inserire NOME: ").strip().lower()
    print("\n")
    lab = input("inserire Laboratorio (15 o 17): ").strip().lower()
    if not lab.isdigit() or (int(lab) != 15 and int(lab) != 17):
        print("\nLaboratorio non valido")
        continue
    lab = int(lab)
    print("\n")
    turno = input("inserire turno (1 (inizio alle 13) o 2 (inizio alle 16)): ").strip().lower()
    if not turno.isdigit() or (int(turno) != 1 and int(turno) != 2):
        print("\nTurno non valido")
        continue
    turno = int(turno)
    print("\n")
    compito = input("inserire la lettera del tuo compito (una tra A, B, C o D): ").strip().upper()
    if compito < 'A' or compito > 'D':
        print("\ncompito non valido")
        continue
    
    print("Confermi i seguenti dati?\n")
    print("MATRICOLA:",matricola)
    print("COGNOME:",cognome)
    print("NOME:",nome)
    print("LABORATORIO:",lab)
    print("TURNO:",turno)
    print("COMPITO:",compito)
    
    while True:
        print("\n")
        risp = input("Premere S o N: ").strip().lower()
        if risp == "n":
            break
        elif risp == "s":
            try:
                with open("studente.txt", "w") as f:
                    f.write(matricola+"\n")
                    f.write(cognome+"\n")
                    f.write(nome+"\n")
                    f.write(str(lab)+"\n")
                    f.write(str(turno)+"\n")
                    f.write(compito)
                input("\nRegistrazione dati studente completata, premere INVIO per terminare\nDopo aver premuto INVIO puoi chiudere la finestra\n")
                completed = True
                break
            except:
                print("PROBLEMA REGISTRAZIONE DATI")
                input()
        completed = True
        break
