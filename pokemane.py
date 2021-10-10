import time
import os
import os.path
import random
import datetime

def menu():
    loop1 = True
    while loop1 == True:
        input1 = input("\nChoose what to do (by typing the right number)\n1.Start Game\n2.Options\n3.Info\n")
        if input1 != "1" and input1 != "2" and input1 != "3":
            print("sorry, that is not an option")
        elif input1 == "1":
            loop1 = False
def saving(pokemons,team):
    saveFile = open("yourSaveFile.txt", "a+")
    saveFile.truncate(0)
    saveFile.seek(0)
class Pokemon:
      def __init__(self, name,hp,defense,speed,type,possibleMoves,baseHp,baseDefence,baseSpeed):
        self.name = name
        self.hppl = hp
        self.speedpl = speed
        self.defensepl = defense
        self.type = type
        self.moves = possibleMoves
        self.basehp = baseHp
        self.baseDefence = baseDefence
        self.baseSpeed = baseSpeed
print("Loading...\n")
if True:
    p1 = Pokemon("Magikarp",2,1,1,['Water'],['m0','m1'],10,10,10)
    p2 = Pokemon("Stannina",1,2,1,['Fire'],['m0','m1'],10,10,10)
print(p1.type)

moveNames = {
    #[name,baseattack,accuracy,special]
    'm0' : ['Splash',0,100,0],
    'm1' : ['SelfHate',0,100,1]
}

playtime = 0
if os.path.isfile("yourSaveFile.txt"):
    saveFile = open("yourSaveFile.txt", "a")
    saveFile.read().split(';')
else:
    saveFile = open("yourSaveFile.txt", "x")
saveFile.close()

print(moveNames["m0"])
lista = [p1,'p2']
print(vars(lista[0])['name'])

#Start of game
print("Welkom to PokeMarjin, my own spin-off pokemon game fully made with python")
menu()