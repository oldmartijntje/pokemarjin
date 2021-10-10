class Person:
      def __init__(self, name,hp,defense,speed):
        self.name = name
        self.hp = hp

def assignPokemons():
    p1 = Person("Magikarp", 10,10,10)

pokemon = {
    'p0000' : ['Magikarp','10',''],
    'p0001'   : 'Eevee',
    'p0002': 'Pikachu',
    'p0003': 'Turtwig',
    'p0004'  : 'Stannina'
}
pokemonPossibleMoves = {
    'p0000' : 'm0000;m0001',
    'p0001'   : 'm0002,m0003;m0001',
    'p0002': 'm0003;m0004;m0005',
    'p0003': 'm0001;m0005;m0006',
    'p0004'  : 'm0000;m0007'
}
moveNames = {
    'm0000' : 'Splash'
}
print(pokemon['p0003'])