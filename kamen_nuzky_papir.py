#! python3
# kamen nuzky papir
import random # nacteni knohovny pro generovani nahody
# definice
volby = ['kámen', 'núžky', 'papír']

# vstupy hracu
vstup_hrac = int(input("Zvol si: (1-kámen,2-nůžky,3-papír) "))
vstup_pocitac = random.randint(1, 3)
# vysledek


def hra(vstup_hrac, vstup_pocitac):
    ''' Vlastni hra'''
    # vyhodnoceni
    if vstup_hrac == vstup_pocitac:
        return 'repeat'
    elif vstup_hrac == 1:
        if vstup_pocitac == 2:
            return 'win'
        elif vstup_pocitac == 3:
            return 'loose'
    elif vstup_hrac == 2:
        if vstup_pocitac == 3:
            return 'win'
        elif vstup_pocitac == 1:
            return 'loose'
    elif vstup_hrac == 3:
        if vstup_pocitac == 1:
            return 'win'
        elif vstup_pocitac == 2:
            return 'loose'
    else:
        return 'wrong'

print(hra(vstup_hrac, vstup_pocitac))


