import random

class Character:
    def __init__(self, name, hp, damage, weapon):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, amount):
        self.hp -= amount

        if self.hp <= 0:
            self.hp = 0
            return f"{self.name} died"

        return f"{self.name} has {self.hp} HP left"
    
    def dodge(self):
        return random.random() < 0.3
    

    def attack(self, target):
        if target.dodge():
            return f"{target.name} dodged {self.name}'s attack!"
        
        damage_result = target.take_damage(self.damage)
        return f"{self.name} hits {target.name} for {self.damage} damage. {damage_result}"