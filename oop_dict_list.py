class Character(object):
    def __init__(self,name,health,damage,inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.inventory = inventory
    
    def __repr__(self): #return string, make it possible to use print function
        return self.name

heroes = []
heroes.append(Character('iron man', 100, 200, {'gold': 500, 'weapon': 'laser'}))
heroes.append(Character('dead pool', 300, 30, {'gold': 300, 'weapon': 'sword'}))

monsters = []
monsters.append(Character('goblin', 90, 30, {'gold': 50, 'weapon': 'spear'}))
monsters.append(Character('dragon', 200, 80, {'gold': 200, 'weapon': 'fire'}))

print(heroes)
print(monsters)
del heroes[0]
print(heroes)