import numpy as np                          #libreria per le matrici
from random import choice, randint

def grid_fun():                             #crea una matrice 8x8 di zeri
    grid = np.full((8, 8), '0')             #corrisponde su python ad una lista di liste
    return grid

def rand(src):                              #ritorna un numero casuale tra 0 e src
    l_c = randint(0, src)
    return l_c


def check(boat):                            #controlla se le caselle dove devono andare le barche sono vuote o occupate
    count = 0                               #variabile counter
    for c in boat:
        if c == '0':                        #se l'elemento è uno zero allora indica una casella vuota...
            count += 1                      #...dunque aggiunge 1 al counter
        elif c == '1':
            continue                        #altrimenti riinizia il ciclo
    if count == len(boat):                  #se il counter segna un valore pari a quello della barca...
        return True                         #...allora tutte e x le caselle sono vuote, ritorna vero
    else:
        return False                        #altrimenti ritorna falso


def coll(boats):                                                    #colloca le barche della cpu
    boo = [True, False]
    for x in boats:                                                 #boats -> vedi "variabili", il valore x indica anche la lunghezza della barca
        dir = choice(boo)                                           #sceglie randomicamente un valore booleano, True = barca orizzontale, False = barca verticale
        line = rand(7)                                              #sceglie la riga in cui si troverà la barca nel caso in cui sia orizzontale
        column = rand(7)                                            #sceglie la colonna in cui si troverà la barca nel caso in cui sia verticale
        if dir:                                                     #(= se orizzontale)
            column = rand(7 - x)                                    #sceglie la colonna in cui si trova l'estremo sinistro della barca
            boat = grid[line:line + 1, column:column + x]           #crea una sottomatrice con le sole celle di dove si troverà la barca
            while not check(boat[0]):                               #finchè le non è rispettato il check:
                line = rand(7)                                      #genera randomicamente altri punti...
                column = rand(7 - x)                                #...di collocazione per la barca
                boat = grid[line:line + 1, column:column + x]       #e li assegna alla barca
            for i in range(x):                                      #sostituisce gli zeri nella matrice con gli 1...
                grid[line, column+i] = '1'                          #...nei punti in cui è presente una barca
        else:                                                       #analogamente se la direzione è verticale
            line = rand(7 - x)
            boat = grid[line:line + x, column:column + 1]
            while not check(boat):
                column = rand(7)
                line = rand(7 - x)
                boat = grid[line:line + x, column:column + 1]
            for ii in range(x):
                grid[line + ii, column] = '1'


def show_grid(grid):                                                        #crea una rappresentazione grafica per la matrice
    tmp = 0                                                                 #variabile utilizzata sia per indicizzare le caselle che per riconoscere quando stampare la base del campo
    letters = "abcdefgh"                                                    #lista di lettere
    print("┌───┬───┬───┬───┬───┬───┬───┬───┐")                              #disegna il sopra del campo
    for x in grid:                                                          #la matrice è una lista di liste, dunque le x rappresentano le righe
        for y in x:                                                         # y sono gli elementi della matrice
            if y == '1':                                                    #sostituisce gli 1 con  ■
                print("│ ■ ", end = "")
            else:                                                           #sostituisce gli 0 con degli spazi vuoti
                print("│   ", end = "")
        if tmp < 7:                                                         #riconosce quando il campo finisce
            print(f"│ {letters[tmp]}\n├───┼───┼───┼───┼───┼───┼───┼───┤")   #disegna la parte centrale del campo
            tmp += 1
        else:
            print(f"│ {letters[tmp]}\n└───┴───┴───┴───┴───┴───┴───┴───┘")   #disegna la base del campo
            print("  1   2   3   4   5   6   7   8 ")                       #stampa i numeri corrispondenti alle colonne


#variabili
boats = [4, 3, 2, 1]                   #ogni elemento è una barca di lunghezza pari al suo valore
grid = grid_fun()                      #crea la variabile a cui è associata la matrice


def main():
    coll(boats)                        #colloca le barche della cpu
    show_grid(grid)                    #stampa il campo da gioco


if __name__ == '__main__':
    main()