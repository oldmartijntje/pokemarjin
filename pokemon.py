import time
import os
import os.path
import random
import datetime
import math

def typeComparrison(team,enemyTeam,activePokemon):
    if len(team[0][4]) == 1:
        print(len(team[0][4][0]))

def calculateDamage(chosenMove,team,enemyTeam,activePokemon):
    #typeAdventage = typeComparrison(team,enemyTeam,activePokemon)
    typeAdventage = 0
    randomNumber = random.randint(0, 100)
    if chosenMove[1] == 0:
        damage = 0
    elif randomNumber <= chosenMove[2]:
        #damage = math.floor((chosenMove[1] * math.floor(int(vars(team[activePokemon[0]])['level'])) * (typeAdventage+1) * int(vars(team[activePokemon[0]])['currentAttack'])) - math.floor((int(vars(enemyTeam[activePokemon[1]])['currentDef']) / 1.25)) * (random.randint(975, 1025)/1000))
        #if damage < 1:
        damage = math.floor((((2 * math.floor(int(vars(team[activePokemon[0]])['level']))) / 5 + 2) * chosenMove[1] * int(vars(team[activePokemon[0]])['currentAttack']) / int(vars(enemyTeam[activePokemon[1]])['currentDef'])) / 50 + 2)
         #   damage = 1
        print(damage)
        #print(f"{chosenMove[1]},{typeAdventage},", vars(team[activePokemon[0]])['currentAttack'],",",vars(enemyTeam[activePokemon[1]])['currentDef'],",",math.floor(int(vars(team[activePokemon[0]])['level']) / int(vars(enemyTeam[activePokemon[1]])['level'])),",",(vars(enemyTeam[activePokemon[1]])['attackModifier']))
    else:
        print("The attack missed")

def battle(team, enemyTeam, moves):
    print(vars(team[0])['name'] + ", i choose you!\nYour opponent takes " + vars(enemyTeam[0])['name'] + " to the battle")
    battleStillGoing = True
    activePokemon = [0,0]
    while battleStillGoing == True:
        loop1 = True
        while loop1 == True:
            enableMove = [False,False,False,False]
            answer = input("\nwhat do you want to do?\n1.attack\n2.run\n3.items\n4.switch pokemon\n")
            if answer != '1' and answer != '2' and answer != '3' and answer != '4':
                print("sorry, that is not an option")
            elif answer == '1':
                loop2 = True
                while loop2 == True:
                    print("what move do you want to use?")
                    if vars(team[activePokemon[0]])['move1'] != '0':
                        print("1." + moves["m" + vars(team[activePokemon[0]])['move1']][0])
                        enableMove[0] = True
                    if vars(team[activePokemon[0]])['move2'] != '0':
                        print("2." + moves["m" + vars(team[activePokemon[0]])['move2']][0])
                        enableMove[1] = True
                    if vars(team[activePokemon[0]])['move3'] != '0':
                        print("3." + moves["m" + vars(team[activePokemon[0]])['move3']][0])
                        enableMove[2] = True
                    if vars(team[activePokemon[0]])['move4'] != '0':
                        print("4." + moves["m" + vars(team[activePokemon[0]])['move4']][0])
                        enableMove[3] = True
                    print("5.cancel")
                    answer2 = input()
                    if answer2 == "1" and enableMove[0] == True:
                        print("1." + moves["m" + vars(team[activePokemon[0]])['move1']][0])
                        chosenMove = moves["m" + vars(team[activePokemon[0]])['move1']]
                        loop2 = False 
                    elif answer2 == "2" and enableMove[1] == True:
                        print("2." + moves["m" + vars(team[activePokemon[0]])['move2']][0])
                        chosenMove = moves["m" + vars(team[activePokemon[0]])['move2']]
                        loop2 = False 
                    elif answer2 == "3" and enableMove[2] == True:
                        print("3." + moves["m" + vars(team[activePokemon[0]])['move3']][0])
                        chosenMove = moves["m" + vars(team[activePokemon[0]])['move3']]
                        loop2 = False 
                    elif answer2 == "4" and enableMove[3] == True:
                        print("4." + moves["m" + vars(team[activePokemon[0]])['move4']][0])
                        chosenMove = moves["m" + vars(team[activePokemon[0]])['move4']]
                        loop2 = False 
                    elif answer2 == "5":
                        print("cancel")
                    else:
                        print("that is not an option")
                    print(chosenMove)#['Splash', 0, 100, 0, 0]
                damage = calculateDamage(chosenMove,team,enemyTeam,activePokemon)
                        

                
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
    #saveFile.write(pokemons, "/", team, "/", gameData)
class PokemonInTeam:
    def __init__(self, name, hp, defense, attack, speed, type, moves, baseHp, baseDefence, baseAttack, baseSpeed, level):
        self.name = name
        self.hppl = hp
        self.speedpl = speed
        self.attack = attack
        self.baseAttack = baseAttack
        self.defensepl = defense
        self.type = type
        self.move1 = moves[0]
        self.move2 = moves[1]
        self.move3 = moves[2]
        self.move4 = moves[3]
        self.moves = moves
        self.basehp = baseHp
        self.baseDefence = baseDefence
        self.baseSpeed = baseSpeed
        self.level = level
        self.currentHp = str(int(hp) * int(level)+int(baseHp))
        self.currentSpeed = str(int(speed) * int(level)+int(baseSpeed))
        self.currentDef = str(int(defense) * int(level)+int(baseDefence))
        self.currentAttack = str(int(attack) * int(level)+int(baseAttack))
class Pokemon:
      def __init__(self, name, hp, defense, attack, speed, type, possibleMoves, baseHp, baseDefence, baseAttack,baseSpeed):
        self.name = name
        self.hppl = hp
        self.attack = attack
        self.baseAttack = baseAttack
        self.speedpl = speed
        self.defensepl = defense
        self.type = type
        self.moves = possibleMoves
        self.basehp = baseHp
        self.baseDefence = baseDefence
        self.baseSpeed = baseSpeed
print("Loading...\n")
if True:
    p1 = Pokemon("Magikarp", '3', '1', '1', '1', ['Water'], ['1', '2'], '10', '10', '10', '10')
    p2 = Pokemon("Stannina", '1', '3', '1', '1', ['Fire'], ['1', '2', '5', '6', '8', '9'], '10', '10', '10', '10')
    p3 = Pokemon("Thomas", '2', '2', '1', '1', ['Dark'], ['1', '3', '4', '6', '7'], '10', '10', '10', '10')
    p4 = Pokemon("Eevee", '1', '2', '1', '2', ['Normal'], ['1', '3', '4', '7'], '10', '10', '10', '10')
    p5 = Pokemon("Muik", '3', '3', '1', '1', ['Water'], ['2', '6', '7', '4'], '8', '8', '8', '8')
#print(p1.type)
moves = {
    #[name,baseattack,accuracy,special,minimumLevel,maxPP]
    'm1' : ['Splash',0,100,0,0,20],
    'm2' : ['SelfHate',0,100,1,5,5],#ur speed goes to like idk 0, but ur defense increases
    'm3' : ['Tackle',3,85,0,0,15],
    'm4' : ['Ember',2,75,0,8,15],
    'm5' : ['Neko power',0,80,2,10,10],#enemy falls in love for some rounds
    'm6' : ['Hacking the mainframe',0,50,3,10,5],
    'm7' : ['Watergun',2,75,0,8,15],
    'm8' : ['Free Premium',0,90,4,12,5],#lowers their attacks, defence and speed
    'm9' : ['Neko Energy',0,100,5,10,5],#your speed and attack increases
    'm10' : ['Buff',0,100,6,15,10]#significatly boosts your defence

}
#Stannina"','1','2','1',['Fire','none'],['1','2','0','0'],'10','10','10',level; = 11
gameData =[0]
if os.path.isfile("yourSaveFile.txt"):
    try:
        saveFile = open("yourSaveFile.txt", "a")
        pokemonsWrapped, teamWrapped, gameDataWrapped = saveFile.read().split('/')
        pokemons = pokemonsWrapped.spit(',')
        team = teamWrapped.spit(',')
        gameData = gameDataWrapped.spit(',')
        gameData[0] = int(gameData[0])
    except:
        gameData =[0]
else:
    saveFile = open("yourSaveFile.txt", "x")
saveFile.close()

#print(moves["m0"])
#lista = [p1,'p2']
#print(vars(lista[0])['name'])

#Start of game
print("Welkom to PokeMarjin, my own spin-off pokemon game fully made with python")
menu()
#team= [["Thomas", '2', '2', '1', '1', ["Dark"], ['1','3','4','0'], '10', '10', '10','10','10']]
t1 =PokemonInTeam("Thomas", '2', '2', '1', '1', ["Dark"], ['1','3','4','0'], '10', '10', '10', '10', '10')
t2 =PokemonInTeam("Thomas", '2', '2', '1', '1', ["Dark"], ['1','3','4','0'], '10', '10', '10', '10', '10')
t3 =PokemonInTeam("Thomas", '2', '2', '1', '1', ["Dark"], ['1','3','4','0'], '10', '10', '10', '10', '10')
t4 =PokemonInTeam("Thomas", '2', '2', '1', '1', ["Dark"], ['1','3','4','0'], '10', '10', '10', '10', '10')
t5 =PokemonInTeam("Thomas", '2', '2', '1', '1', ["Dark"], ['1','3','4','0'], '10', '10', '10', '10', '10')
t6 =PokemonInTeam("Thomas", '2', '2', '1', '1', ["Dark"], ['1','3','4','0'], '10', '10', '10', '10', '10')
team = [t1, t2, t3, t4, t5, t6]
battle(team, team, moves)