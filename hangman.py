import random

graphics=['''
------------
|         |''','''
------------
|         |         
|          O''','''
------------
|         | 
|          O 
|         / |''','''
------------
|         | 
|          O 
|         / | 
|          | ''','''
------------
|         |
|          O 
|         / |
|          |
|         / | 
|            ''']

print("The Hangman!")
print("=============================\n")

with open('wordlist.txt','r') as f:
    lista = f.read().splitlines()

da_indovinare = random.choice(lista)        # parola scelta random dalla lista
tentativi = 5                               
flag = False                                # flag per le due funzioni grafiche

def check_health(tentativi):
    if tentativi==4:
        print(graphics[len(graphics)-tentativi-1])
    elif tentativi==3:
        print(graphics[len(graphics)-tentativi-1])
    elif tentativi==2:
        print(graphics[len(graphics)-tentativi-1])
    elif tentativi==1:
        print(graphics[len(graphics)-tentativi-1])
    else:
        print(graphics[len(graphics)-tentativi-1],'\n')
        print(f'The word to guess was {da_indovinare}!')
        exit()

def draw1(scelta):
    # indici del carattere scelto nella parola da indovinare
    indici = [i for i,x in enumerate(da_indovinare) if x == scelta]
    # lista vuota che conterrà i caratteri della parola (grafica con underscores)
    parola = []
    # itero num lungo la parola da indovinare: se num è pari ad un indice tra quelli prima
    # calcolati, aggiunge alla lista il carattere scelto dall'utente,
    # altrimenti aggiunge un underscore
    for num in range(len(da_indovinare)):
        if num in indici:
            parola.append(scelta+' ')
        else:
            parola.append('_ ')
    return parola

def draw2(scelta,parola):
    # indici del carattere scelto nella parola da indovinare
    indici = [i for i,x in enumerate(da_indovinare) if x == scelta]
    # itero num lungo la parola ottenuta dalla prima funzione
    # (la parola con gli underscores): se num è negli indici, sostituisce
    # all'underscore in quell'indice il carattere dell'utente
    for num in range(len(parola)):
        if num in indici:
            parola[num] = scelta+' '
    return parola

def check_parola(parola):
    # converte la lista in una stringa
    parola = ''.join(parola)
    # rimuove tutti gli spazi tra i caratteri (sostituisce ' ' con '')
    parola = parola.replace(' ','')
    # check se la stringa ottenuta contiene solo lettere e ritorna il booleano corrispondente
    return parola.isalpha()



print(f'The word to guess has {len(da_indovinare)} letters')
while True:
    scelta = input('Choose a letter (space to exit): ').lower()
    if scelta == ' ': 
        print('Bye!')
        exit()
    elif scelta.isdigit():      # se il carattere è un numero
        print('Letter not valid... attempt burnt!')
        tentativi-=1
        check_health(tentativi)
        continue

    if not flag:    # per draw1, genera la prima stringa grafica
        if scelta in da_indovinare:
            print(f'{scelta} is in the word!\n')
            parola = draw1(scelta)
            print(''.join(parola))
            flag = True     # dal primo tentativo in poi verrà usata solo draw2
        else:
            print('Letter not found!\n')
            parola = draw1(scelta)
            tentativi-=1
            check_health(tentativi)
            flag = True
            continue
    else:       # da qui solo draw2
        if scelta in da_indovinare:
            print(f'{scelta} is in the word!\n')
            frase = draw2(scelta,parola)
            print(''.join(frase))
            if check_parola(frase):
                print('You win!')
                exit()
            
        else:
            print('Letter not found!\n')
            tentativi-=1
            check_health(tentativi)
            continue