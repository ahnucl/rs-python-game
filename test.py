from game import Enemy, Hero

heroi = Hero(name='Hero1', health_points=100, level=5, skill='Super strength')
print(heroi.details())
monster = Enemy(name='Bat', health_points=10, level=1, type='Flying')
print(monster.details())
