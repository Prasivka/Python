#! python3
rozmer_x = 9
rozmer_y = 9

def hraci_plocha(osa_x, osa_y):
    ''' definice hraci plochy
    vygeneruje herni plan '''
    hraci_plan = []
    for x in range(osa_x):
        temp = []
        for y in range(osa_y):
            temp.append(' ')
        hraci_plan.append(temp)
    return hraci_plan

def vypis_plochy(plocha):
    ''' vypsani hraci plochy - hezky '''
    for i in range(len(plocha)):
        print(i, " ", end="")
    print(end="\n")
    j = 0
    for seznam in plocha:
        for prvek in seznam:
            print(prvek, "|", end="")
        print(" ", j, end="\n")
        j += 1
        for prvek in seznam:
            print("_  ", end="")
        print(end="\n")
    print()

def herni_tah():
    '''  '''
    tah_x = input("Zadej polohu tahu 'x'[0..8] : ")
    tah_y = input("Zadej polohu tahu 'y'[0..8] : ")
    if (int(tah_x) in range(0,9)) and (int(tah_y) in range(0,9)):
        tah_x = int(tah_x)
        tah_y = int(tah_y)
    else:
        pass
    lokace = [tah_x][tah_y]
    return lokace

def switcher(volba='x'):
    # přepínač mezi volbami krizek / kolecko
    if volba == 'x':
        return 'o'
    else:
        return 'x'

# ------------------------------------------------------------

herni_plan = hraci_plocha(rozmer_x, rozmer_y)

vypis_plochy(herni_plan)

hrac = 'x'
pokracuj = True
while pokracuj:
    '''  Stridani tahu '''
    tah_x = input("Zadej polohu tahu 'x'[0..8] : ")
    tah_y = input("Zadej polohu tahu 'y'[0..8] : ")
    if (int(tah_x) in range(0,9)) and (int(tah_y) in range(0,9)):
        tah_x = int(tah_x)
        tah_y = int(tah_y)
        if herni_plan[tah_x][tah_y] == ' ':
            herni_plan[tah_x][tah_y] = hrac
        else:
            print('Obsazené pole!')
            pass
    else:
        pokracuj = False
    vypis_plochy(herni_plan) # vykreslí plochu

    hrac = switcher(hrac) # přepíná mezi hráči


# vypsani hraci plochy - stroze
'''
for seznam in hraci_plocha(rozmer_x, rozmer_y):
    for prvek in seznam:
        print(prvek, end="")
    print(end="\n")
'''
