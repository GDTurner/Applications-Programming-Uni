import random, items

class EnemyBase:
    def __init__(self, name, strth, int, dex, hp, weapon):
        self.name = name
        self.strength = strth
        self.intelligence = int
        self.dexterity = dex
        self.hp = hp
        self.weapon = weapon
        self.initiative = random.randint(1,20) + self.intelligence


    def get_initiative(self):
        bonus = self.weapon.initbonus
        initiative_value = random.randint(1,20) + (self.intelligence + bonus)
        return initiative_value        


    def alive(self):
        return self.hp > 0

    def description(self):
        pass

class Goon(EnemyBase):
    def __init__(self):
        super().__init__(name="Goon", strth=2, int=-1, dex=0, hp=15, weapon=items.StunStick())

    def attack(self, player):
        self.weapon.attack_text()
        to_hit = random.randint(1,20) + (self.weapon.accuracy + self.dexterity)
        if to_hit >= player.stats.dexterity + 10:
            damage = self.weapon.damage + self.strength
            player.stats.hp -= damage
            if player.stats.hp > 0:
                return f"{self.name} deals {damage} damage to {player.name}. You have {player.stats.hp} hp remaining."
            else:
                return f"{player.name} crumples to the ground, lifeless."
        else:
            return f"{self.name}'s attack misses {player.name}"
    

# print(Goon().initiative)