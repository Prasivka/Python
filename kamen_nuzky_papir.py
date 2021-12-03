#! python3
# Hra Kámen nůžky papír
import random

def game():
    pocet_hracu = int(input("Kolik bude hráčů? (obvykle 2) "))
    volby = ['kámen', 'nůžky', 'papír']
    
    vstup_hrac = int(input("Vyber volbu: (1-kámen,2-nůžky,3-papír)"))
    vstup_comp = random.randint(1,3)
    
# konec
