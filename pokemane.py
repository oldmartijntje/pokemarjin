def menu():
    loop1 = True
    while loop1 == True:
        input1 = input("\nChoose what to do (by typing the right number)\n1.Start Game\n2.Options\n3.Info")
        if input1 != "1" and input1 != "2" and input1 != "3":
            print("sorry, that is not an option")
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
    p1 = Pokemon("Magikarp",2,1,1,'Water',['m0000','m0001'],10,10,10)
print(p1.type)
moveNames = {
    #[name,baseattack,accuracy,special]
    'm0000' : ['Splash',0,100,0],
    'm0001' : ['SelfHate',0,100,1]
}
lista = [p1,'p2']
print(vars(lista[0])['name'])
#Start of game
print("Welkom to PokeMarjin, my own spin-off pokemon game fully made with python")
menu()