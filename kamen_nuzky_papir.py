#! python3
# kamen nuzky papir
import random # nacteni knohovny pro generovani nahody

def rozhodnuti(vstup_hrac, vstup_pocitac):
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

def vyhodnoceni(vysledek):
    ''' Převedeni vysledku do vystupu '''
    if vysledek == 'loose':
        return 'Bohužel, prohrál jsi.'
    elif vysledek == 'win':
        return 'Gratuluji, vyhrál jsi!'
    elif vysledek == 'repeat':
        return 'Remíza, zkus to ještě jednou.'
    else:
        return 'Takhle by to nešlo'

def main():
    ''' Hlavni program '''
#    volby = ['kámen', 'núžky', 'papír']
    opakuj = True
    while opakuj:
        # vstupy hracu
        vstup_hrac = int(input("Zvol si: (1-kámen,2-nůžky,3-papír) "))
        vstup_pocitac = random.randint(1, 3)
        # vysledek
        print(vyhodnoceni(rozhodnuti(vstup_hrac, vstup_pocitac)))
        pokracovat = input("Chceš pokračovat? y/n ")
        if pokracovat.lower() == 'y':
            opakuj = True
        elif pokracovat.lower() == 'n':
            opakuj = False
        else:
            break

main()
