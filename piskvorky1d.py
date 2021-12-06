#! python3
rozmer_x = 9
rozmer_y = 9


def hraci_plocha(osa_x, osa_y):
    hraci_plan = []
    for x in range(osa_x):
        temp = []
        for y in range(osa_y):
            temp.append(' ')
        hraci_plan.append(temp)
    return hraci_plan

def vypis_plochy(plocha):
    # vypsani hraci plochy - hezky
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


herni_plan = hraci_plocha(rozmer_x, rozmer_y)

herni_plan[5][3] = 'x'
herni_plan[5][5] = 'o'

vypis_plochy(herni_plan)

herni_plan[4][4] = 'x'

vypis_plochy(herni_plan)


