import random


class Character:
    def __init__(self, name, health_points, level) -> None:
        self.__name = name
        self.__health_points = health_points
        self.__level = level

    def get_name(self):
        return self.__name

    def get_health_points(self):
        return self.__health_points

    def get_level(self):
        return self.__level

    def details(self):
        return f"Name: {self.get_name()}\nHP: {self.get_health_points()}\nLVL: {self.get_level()}"

    def attack(self, target):
        damage_amount = random.randint(self.get_level() * 2, self.get_level() * 4)
        target.damage_health(damage_amount)
        print(f"{self.__name} attacked {target.get_name()} e did {damage_amount} damage!")

    def damage_health(self, amount):
        self.__health_points -= amount
        if self.__health_points < 0:
            self.__health_points = 0


class Hero(Character):
    def __init__(self, name, health_points, level, skill) -> None:
        super().__init__(name, health_points, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill

    def details(self):
        return f"{super().details()}\nSkill: {self.get_skill()}\n"

    def special_attack(self, target: Character):
        damage_amount = random.randint(self.get_level() * 5, self.get_level() * 8)
        target.damage_health(damage_amount)
        print(f"{self.get_name()} used the special skill {self.get_skill()} on {target.get_name()} and did {damage_amount} damage!")


class Enemy(Character):
    def __init__(self, name, health_points, level, type) -> None:
        super().__init__(name, health_points, level)
        self.__type = type

    def get_type(self):
        return self.__type

    def details(self):
        return f"{super().details()}\nType: {self.get_type()}\n"


class Battle:
    def __init__(self) -> None:
        self.hero = Hero(name='The Hero', health_points=100, level=5, skill='Super strength')
        self.enemy = Enemy(name='Bat', health_points=80, level=4, type='Flying')

    def begin(self):
        print('Battle started!')
        while self.hero.get_health_points() > 0 and self.enemy.get_health_points() > 0:
            print("\nCharacter's details:")
            print(self.hero.details())
            print(self.enemy.details())

            input('Press Enter to attack...')
            choice = input("Options (1 - Normal attack, 2 - Special attack): ")

            if choice == '1':
                self.hero.attack(self.enemy)
            elif choice == '2':
                self.hero.special_attack(self.enemy)
            else:
                print('Invalid options. Choose again.')

            if self.enemy.get_health_points() > 0:
                self.enemy.attack(self.hero)

        if self.hero.get_health_points() > 0:
            print("\nCongratulations! You won the battle!")
        else:
            print("\nYou were defeated...")


battle = Battle()
battle.begin()
