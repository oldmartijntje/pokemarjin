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

if True:
    p1 = Pokemon("Magikarp", 2,1,1,'Water',['m0000','m0001'],10,10,10)
print(p1.type)
moveNames = {
    #[name,baseattack,accuracy,special]
    'm0000' : ['Splash',0,100,0],
    'm0001' : ['SelfHate',0,100,1]
}
