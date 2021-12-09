# !python3
class Kostka:
    '''
    Tato třída reprezentuje hrací kostku.
    '''
    def __init__(self, pocet_sten=6):
        self.__pocet_sten = pocet_sten
    
    def vrat_pocet_sten(self):
        '''
        Vrátí počet stěn kostky.
        '''
        return self.__pocet_sten

sestistennakostka = Kostka()
desetistennakostka = Kostka(10)
print(desetistennakostka.vrat_pocet_sten())
print(sestistennakostka.vrat_pocet_sten())
