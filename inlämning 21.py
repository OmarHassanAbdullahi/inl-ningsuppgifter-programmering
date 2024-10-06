import random
# Denna funktion representerar kortleken på 52 kort, siffra 2 och 10 repesenterar sina egna värden. medan 10 också reperesenterar klädda kort (knekt,dam,kung).
# 11 används för att reperesnetera ess, som kan ha värdet 11 eller 1 beroende på om det är över 21 eller under.
def kort_lek() -> list[int]:
    return [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

# klassen som representerar spelaren i spelet.
class Spelare:
    def __init__(self) -> None:
        # skapar en lista för att hålla koll på spelarens kort.
        self.hand: list[int] =  []
     # metod för att dra ett kort från leken.
    def dra_kort(self, deck: list[int]) -> None:
        #blanda kortleken innan man dra ett kort för att simulera slump.
        random.shuffle(deck)
        #Drar ett kort deån toppen av kortleken
        kort = deck.pop()
        #lägger till kortet i spelarens hand
        self.hand.append(kort)
        print(f"Spelaren drog kort: {kort}") #presenterar det kort spelaren drog till spelarens hand
      
      #metoden för räkna den totala poängen av kortren i spelarens hand.
    def räkna_kort(self) -> int: 
        total: int = sum(self.hand) # summerar alla kort i spelarens hand 
       # om spelaren ta upp ett ess och totalen översitger 21      
        if total > 21 and 11 in self.hand:
            #ändras essets värde från 11 till 1.
            self.hand[self.hand.index(11)] = 1
            total = sum(self.hand)
        return total # retunerar värdet av totalen inklusive essets värde
    

# klassen som representerar spelaren i spelet.
class NPC:

    def __init__(self) -> None:
        # skapar en lista för att hålla koll på npc kort.
        self.npc_hand: list [int]= []
# metod för att dra ett kort från leken.
    def dra_kort(self, deck: list[int]) -> None:
         #blanda kortleken innan man dra ett kort för att simulera slump.
        random.shuffle(deck)
        #Drar ett kort deån toppen av kortleken
        kort = deck.pop()
        #lägger till kortet i npcs hand
        self.npc_hand.append(kort)
        print(f"Npc: {kort}") # presenterar kortet npc drog till hans hand
 
 #metoden för räkna den totala poängen av kortren i npcs hand.
    def räkna_kort(self) -> int:
        total:int = sum(self.npc_hand) #summerar alla kort i Npc hand 
        # om npc tar upp ett ess och totalen översitger 21 
        if total > 21 and 11 in self.npc_hand:
             #ändras essets värde från 11 till 1.
            self.npc_hand[self.npc_hand.index(11)] = 1
            total = sum(self.npc_hand)
        return total # retimdera den nya totalen inklusive essets värde 
    
    #klass som hanterar huvudprogrammet för spelet 
class huvudspelet:
    def __init__(self, deck: list [int]) -> None:
        #tilldelar den skapade kortleken till spelet.
        self.deck: list [int] = deck
        #skapar instanser av klassen spelare och npc för att kunna köra klasserna i huvudklassen 
        self.spelare = Spelare()
        self.npc = NPC()

           # metod som hanterar spelets vinnare och strukturera turer i spelet.
    def winner_winner(self) -> None:
        #räknar första poängen för både spelare och npc
        spelarens_poäng: int = self.spelare.räkna_kort()
        npc_poäng: int = self.npc.räkna_kort()
        # en loop som kör til att spelaren tar upp ett kort.
        while True:
            self.spelare.dra_kort(self.deck)
            poäng = self.spelare.räkna_kort()
            print(f"spelarens poäng: {poäng}") # presenterar det kortet spelaren har tagit. 
            
            # om spelaren har taigt upp kort som överstiger 21 gå vidare och bestämm vinnaren baserat på slutpoäng.
            if poäng > 21: 
                print("spelarens fick över 21, Npc vann!") # skriver ut resultatet 
                return 
            välj: str = input("vill dra ett kort eller stanna? (ja/nej): ") # inputen som hanterar spelarens val ifall spelaren vill dra ett kort eller stanna
            if välj != 'ja':
                break 
        # en loop som körs tills att npc har nått minst 17 poäng.
        while npc_poäng < 17:
            self.npc.dra_kort(self.deck)
            npc_poäng = self.npc.räkna_kort()
            print(f"Npc poäng: {npc_poäng}") # presenterar det kortet mpc har tagit upp.
            # om npc har fått över 21 
            if npc_poäng > 21:
                print("Npc fick över 21,spelaren vann") # presentera att npc har förlorat 
                return

        # skriv ut slutpoängen för både spelaren och npc. 
        print(f"Spelarens slut poäng: {spelarens_poäng}")
        print(f"npc slut poäng: {npc_poäng}")
         # om spelaren får över npcs poäng och det är under 21
        if spelarens_poäng > npc_poäng:
            print("Spelaren vinner!") #skriv ut att spelaren vinner 
        # om annars npc får över spelaren och det är under 21 
        elif npc_poäng > spelarens_poäng:
            print("Npc vinner!") #skriv ut att npc vinner 
        # annars är det oavgjort
        else:
            print("Det är oavgjort, Npc vann!") # presentera att det är oavgjort(då vinner npc)

    #metod som startar spelet och bestämmer vinnaren.
    def spel(self) -> None:
        # om spelaren inte har över 21, ska spelet fortsätta.
        if self.spelare.räkna_kort() <= 21: 

            self.winner_winner()

# om "name" körs ditekt, skapa en kortlek och starta spelet
if __name__ == "__main__":
    kortlek = kort_lek()
    spel = huvudspelet(kortlek)
    spel.spel()


    



