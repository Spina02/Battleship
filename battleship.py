import numpy as np                          #libreria per le matrici
from random import randint
import os
import sys

def wcls():
    os.system("cls")
    return

def grid_fun():                             #crea una matrice 8x8 di zeri
    grid = np.full((8, 8), '0')             #corrisponde su python ad una lista di liste
    return grid

def check(grid, boat, src1, src2, x, dir, usr_cpu):             #controlla se le caselle dove devono andare le barche sono vuote o occupate
    count = 0                               #variabile counter
    for c in boat:
        if c == '0':                        #se l'elemento è uno zero allora indica una casella vuota...
            count += 1                      #...dunque aggiunge 1 al counter
    if count == len(boat):                  #se il counter segna un valore pari a quello della barca...
        return True                         #...allora tutte e x le caselle sono vuote, ritorna vero
    else:
        if usr_cpu == "cpu":
            src1 = randint(0, 7)                #altrimenti ritorna falso
            src2 = randint(0, 7 - x)
            if dir:
                boat = grid[src1:src1 + 1, src2:src2 + x]
                check(grid, boat, src1, src2, x, dir, usr_cpu)
            else:
                boat = grid[src1:src1 + x, src2:src2 + 1]
                check(grid, boat, src1, src2, x, dir, usr_cpu)
        else:
            print('Coordinates invalid. Try again')
            src1 = int(input('Inserisci la riga: '))
            src2 = int(input('Inserisci la colonna: '))
            if dir:
                boat = grid[src1:src1 + 1, src2:src2 + x]
                check(grid, boat, src1, src2, x, dir, usr_cpu)
            else:
                boat = grid[src1:src1 + x, src2:src2 + 1]
                check(grid, boat, src1, src2, x, dir, usr_cpu)

def coll(grid):                                                    #colloca le barche della cpu
    for x in boats:                                                 #boats -> vedi "variabili", il valore x indica anche la lunghezza della barca
        dir = randint(0,1)                                           #sceglie randomicamente un valore booleano, True = barca orizzontale, False = barca verticale
        line = randint(0, 7)                                              #sceglie la riga in cui si troverà la barca nel caso in cui sia orizzontale
        column = randint(0, 7)                                            #sceglie la colonna in cui si troverà la barca nel caso in cui sia verticale
        if dir:                                                     #(= se orizzontale)
            column = randint(0, 7 - x)                                    #sceglie la colonna in cui si trova l'estremo sinistro della barca
            boat = grid[line:line + 1, column:column + x]           #crea una sottomatrice con le sole celle di dove si troverà la barca
            check(grid, boat[0], line, column, x, dir, "cpu")              #controlla che le caselle siano vuote
            for i in range(x):                                      #sostituisce gli zeri nella matrice con gli 1...
                grid[line, column+i] = '1'                          #...nei punti in cui è presente una barca
        else:                                                       #analogamente se la direzione è verticale
            line = randint(0, 7 - x)
            boat = grid[line:line + x, column:column + 1]
            check(grid, boat[0], column, line, x, dir, "cpu")
            for ii in range(x):
                grid[line + ii, column] = '1'

def coll_user(grid):
    for x in boats:
        print(f"la barca che stai piazzando è da {x} spazi")
        line = int(input('Inserisci la riga: '))
        column = int(input('Inserisci la colonna: '))
        dir = input('Choose the direction (h or v): ')
        if dir.lower == 'horizontal' or dir == 'h':
            boat = grid[line: line + 1, column:column + x]
            check(grid, boat[0], line, column, x, dir, "usr")
            for i in range(x):
                grid[line-1, column + i-1] = '1'
            show_grid(grid_usr)
        elif dir.lower == 'vertical' or dir == 'v':
            boat = grid[line: line + x, column:column + 1]
            check(grid, boat[0], column, line, x, dir, "usr")
            for ii in range(x):
                grid[line + ii -1, column-1] = '1'
            show_grid(grid_usr)
        else:
            print("Wrong input. Try again")
            pass


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
            print("  1   2   3   4   5   6   7   8 \n")                       #stampa i numeri corrispondenti alle colonne


#variabili
boats = [4, 3, 2, 1]                       #ogni elemento è una barca di lunghezza pari al suo valore
grid_cpu = grid_fun()                      #crea la variabile a cui è associata la matrice
grid_usr = grid_fun()

def main():
    coll(grid_cpu)     #colloca le barche della cpu
    show_grid(grid_usr)
    coll_user(grid_usr)
    show_grid(grid_cpu)                    #stampa il campo da gioco
    show_grid(grid_usr)

if __name__ == '__main__':
    main()
