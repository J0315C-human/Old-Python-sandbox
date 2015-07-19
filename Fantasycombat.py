#a set of classes for an adventure/fantasy game.
#Example for subclasses/inheritance etc
from random import randint


def Dice(compareValue = None):
    """rolls a 20 sided dice, if compare is passed, returns True if the roll is <= compare
    """
    roll = randint(1, 20)

    if compareValue == None:
        return roll
    else:
        if roll <=  compareValue:
            return True
        else:
            return False

    
class Character:
    def __init__(self, HP, Weapon, name):
        self.HP = HP
        self.Weapon = Weapon
        self.name = name

    def __repr__(self):
        return "Name: " + self.name + "\nHP: " + str(self.HP) + "\nWeapon: " + self.Weapon.name
    def attack(self, enemy):
        print("attempting attack on ", enemy.name, " with ", self.Weapon.name)
        self.Weapon.use(enemy)
    def isDead(self):
        if self.HP >1:
            return True
        else:
            return False

class Weapon:
    def __init__(self, name, accuracy, damage, Wrange=2):
        self.name = name
        self.accuracy = accuracy
        self.damage = damage
        self.Wrange = Wrange

    def use(self, enemy):
        if Dice(self.accuracy):
            enemy.HP = enemy.HP - self.damage
            print("success - ", self.damage, "HP strength!")
        else:
            print("attack failed.")


Dagger = Weapon("dagger", 10, 10)
Sword = Weapon("sword", 8, 15)
Zach = Character(60, Dagger, "Zach")
DougH = Character(46, Sword, "Doug H")

        
