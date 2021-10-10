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
def saving(pokemons, team, gameData):
    gameData[0] +=1
    saveFile = open("yourSaveFile.txt", "a+")
    saveFile.truncate(0)
    saveFile.seek(0)
    saveFile.write(pokemons, "/", team, "/", gameData)
class Pokemon:
      def __init__(self, name, hp, defense, speed, type, possibleMoves, baseHp, baseDefence, baseSpeed):
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
    p1 = Pokemon("Magikarp",'3','1','1',['Water'],['m1','m2'],'10','10','10')
    p2 = Pokemon("Stannina",'1','3','1',['Fire'],['m1','m2','m5','m6','m8','m9'],'10','10','10')
    p3 = Pokemon("Thomas",'2','2','1',['Dark'],['m1','m3','m4','m6','m7'],'10','10','10')
    p4 = Pokemon("Eevee",'1','2','2',['Normal'],['m0','m2','m4','m7'],'10','10','10')
#print(p1.type)

moveNames = {
    #[name,baseattack,accuracy,special]
    'm1' : ['Splash',0,100,0],
    'm2' : ['SelfHate',0,100,1],#ur speed goes to like idk 0, but ur defense increases
    'm3' : ['Tackle',3,100,0],
    'm4' : ['Ember',2,100,0],
    'm5' : ['Neko power',0,100,2],#enemy falls in love for some rounds
    'm6' : ['Hacking the mainframe',0,100,3],
    'm7' : ['Watergun',2,100,0],
    'm8' : ['Free Premium',0,100,4],#lowers their attacks, defence and speed
    'm9' : ['Neko Energy',0,100,5],#your speed and attack increases

}
#Stannina",1,2,1,['Fire','none'],['m0','m1','none','none'],10,10,10,level; = 10
activePokemon = 0
gameData =[0]
if os.path.isfile("yourSaveFile.txt"):
    saveFile = open("yourSaveFile.txt", "a")
    pokemonsWrapped, teamWrapped, gameDataWrapped = saveFile.read().split('/')
    pokemons = pokemonsWrapped.spit(',')
    team = teamWrapped.spit(',')
    gameData = gameDataWrapped.spit(',')
    gameData[0] = int(gameData[0])
else:
    saveFile = open("yourSaveFile.txt", "x")
saveFile.close()

#print(moveNames["m0"])
#lista = [p1,'p2']
#print(vars(lista[0])['name'])

#Start of game
print("Welkom to PokeMarjin, my own spin-off pokemon game fully made with python")
menu()