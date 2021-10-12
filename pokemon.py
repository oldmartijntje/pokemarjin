import time
import os
import os.path
import random
import datetime


def calculateDamage(chosenMove,team,enemyTeam):
    print()

def battle(team, enemyTeam, moves):
    print(team[0][0] + ", i choose you!\nYour opponent takes " + enemyTeam[0][0] + " to the battle")
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
                    if team[activePokemon[0]*10][5][1] != '0':
                        print("1."+moves["m"+team[activePokemon[0]*10][5][0]][0])
                        enableMove[0] = True
                    if team[activePokemon[0]*10][5][1] != '0':
                        print("2."+moves["m"+team[activePokemon[0]*10][5][1]][0])
                        enableMove[1] = True
                    if team[activePokemon[0]*10][5][2] != '0':
                        print("3."+moves["m"+team[activePokemon[0]*10][5][2]][0])
                        enableMove[2] = True
                    if team[activePokemon[0]*10][5][3] != '0':
                        print("4."+moves["m"+team[activePokemon[0]*10][5][3]][0])
                        enableMove[3] = True
                    print("5.cancel")
                    answer2 = input()
                    if answer2 == "1" and enableMove[0] == True:
                        print("1."+moves["m"+team[activePokemon[0]*10][5][0]][0])
                        chosenMove=moves["m"+team[activePokemon[0]*10][5][0]]
                        loop2 = False 
                    elif answer2 == "2" and enableMove[1] == True:
                        print("2."+moves["m"+team[activePokemon[0]*10][5][1]][0])
                        chosenMove=moves["m"+team[activePokemon[0]*10][5][1]]
                        loop2 = False 
                    elif answer2 == "3" and enableMove[2] == True:
                        print("3."+moves["m"+team[activePokemon[0]*10][5][2]][0])
                        chosenMove=moves["m"+team[activePokemon[0]*10][5][2]]
                        loop2 = False 
                    elif answer2 == "4" and enableMove[3] == True:
                        print("4."+moves["m"+team[activePokemon[0]*10][5][3]][0])
                        chosenMove=moves["m"+team[activePokemon[0]*10][5][3]]
                        loop2 = False 
                    elif answer2 == "5":
                        print("cancel")
                    else:
                        print("that is not an option")
                    print(chosenMove)#['Splash', 0, 100, 0, 0]
                damage = calculateDamage(chosenMove,team,enemyTeam)
                        

                
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
    p1 = Pokemon("Magikarp",'3','1','1',['Water'],['1','2'],'10','10','10')
    p2 = Pokemon("Stannina",'1','3','1',['Fire'],['1','2','5','6','8','9'],'10','10','10')
    p3 = Pokemon("Thomas",'2','2','1',['Dark'],['1','3','4','6','7'],'10','10','10')
    p4 = Pokemon("Eevee",'1','2','2',['Normal'],['1','3','4','7'],'10','10','10')
#print(p1.type)

moves = {
    #[name,baseattack,accuracy,special,minimumLevel]
    'm1' : ['Splash',0,100,0,0],
    'm2' : ['SelfHate',0,100,1,5],#ur speed goes to like idk 0, but ur defense increases
    'm3' : ['Tackle',3,100,0,0],
    'm4' : ['Ember',2,100,0,8],
    'm5' : ['Neko power',0,100,2,10],#enemy falls in love for some rounds
    'm6' : ['Hacking the mainframe',0,100,3,10],
    'm7' : ['Watergun',2,100,0,8],
    'm8' : ['Free Premium',0,100,4,12],#lowers their attacks, defence and speed
    'm9' : ['Neko Energy',0,100,5,10],#your speed and attack increases

}
#Stannina"','1','2','1',['Fire','none'],['1','2','0','0'],'10','10','10',level; = 10
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
team= [["Thomas", '2', '2', '1', ["Dark"], ['1','3','4','0'], '10', '10', '10','10',1]]
battle(team, team, moves)