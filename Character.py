import random, items, time, world


class Species:
    def __init__(self, species):
        self.species = species
        self.strength = None
        self.intelligence = None
        self.dexterity = None
        self.hp = None

    def __str__(self):
        return f"{self.species}\n------\nStrength bonus: {self.strength}\nIntelligence bonus: {self.intelligence}\nDexterity bonus: {self.dexterity}\nHealth: {self.hp}"

class Eagle(Species):
    def __init__(self, species="Eagle"):
        self.species = species
        self.strength = 4
        self.intelligence = -1
        self.dexterity = -4
        self.hp = "50"


class Hawk(Species):
    def __init__(self, species="Hawk"):
        self.species = species
        self.strength = 1
        self.intelligence = 2
        self.dexterity = 2
        self.hp = "40"

class Owl(Species):
    def __init__(self, species="Owl"):
        self.species = species
        self.strength = 0
        self.intelligence = 5
        self.dexterity = 1
        self.hp = "30"

class Falcon(Species):
    def __init__(self, species="Falcon"):
        self.species = species
        self.strength = -2
        self.intelligence = 3
        self.dexterity = 5
        self.hp = "20"

class Player:
    def __init__(self, name, species):
        self.name = name.title()
        self.species = species.title()
        self.inv = [items.MinorStim()]
        self.stats = None
        self.hp = 0
        self.maxHP = 0
        self.weapon = items.Fists()
        self.deck = items.StartDeck()
        self.visited = []
        self.current = world.StartRoom()
        
        self.timer = 0
        if self.timer == 0:
            self.set_stats(self.species)

        if self.stats == None:
            self.set_stats(self.species)


    def set_stats(self, choice):
        if choice == "Eagle":
            self.stats = Eagle()
            self.hp, self.maxHP = 50, 50
        if choice == "Hawk":
             self.stats = Hawk()
             self.hp, self.maxHP = 40, 40
        if choice == "Owl":
             self.stats = Owl()
             self.hp, self.maxHP = 30, 30
        if choice == "Falcon":
             self.stats = Falcon()
             self.hp, self.maxHP = 20, 20

    def holodeck(self):
        self.deck.item_text()

    def equipped(self):
        if self.weapon:
            time.sleep(1)
            print(self.weapon)
        else:
            time.sleep(1)
            print("You don't have a weapon!")
            time.sleep(0.5)
        return

    def alive(self):
        return self.hp > 0

    def inventory(self):
        if self.inv:
            for item in self.inv:
                print(item)
        else:
            print("Nothin' but dust and flies in there, bub.")
        print(self.deck.name)
        return
 
    def heal(self):
        heal_list = []
        for item in self.inv:
            if isinstance(item, items.HealItem):
                heal_list.append(item)

        if heal_list:
            print("Pick and item to heal you:")
            for i, h_item in enumerate(heal_list, 1):
                print(f"{i}: {h_item.name}")
            e = input(" >>> ")     
            while True:
                if int(e) in range(len(heal_list) + 1):
                    choice = heal_list[int(e) - 1]
                    amount = choice.heal
                    self.hp = min(self.maxHP, self.hp + amount)
                    print(f"You've healed {amount} hp.")
                    print(f"You're hp is now {self.hp}")
                    self.inv.remove(h_item)
                    time.sleep(1)
                    break
                else:
                    print("You don't have that!")
        else: 
            print("You've got nothing to heal with. Should take a trip to the pharmacy...")
            return      



    def get_initiative(self):
        bonus = self.weapon.initbonus
        initiative_value = random.randint(1,20) + (self.stats.intelligence + bonus)
        return initiative_value


    def attack_weapon(self, enemy, bonus=0 ):
        modifier = bonus
        print(self.weapon.attack_text())
        to_hit = random.randint(1,20) + (self.weapon.accuracy + self.stats.dexterity)
        print(f"You roll {to_hit} to hit.")
        if to_hit >= enemy.dexterity + 10:
            print(f" You hit {enemy.name}!")
            damage = self.weapon.damage + self.stats.strength + modifier
            enemy.hp -= damage
            if enemy.alive():
                print(f"You deal {damage} damage to {enemy.name}. They have {enemy.hp} hp remaining.")
                return 
            else:
                print(f"{enemy.name} crumples to the ground, lifeless.")
                return
        else:
            print(f"Your attack misses {enemy.name}")
            return

    def save(self):
        with open("birdcage/txt_files/save_file.txt", "w") as s:
            s.write(f"{self.name}\n")
            s.write(f"{self.species}\n")
            s.write(f"{self.deck.name}\n")
            for v in self.visited:
                s.write(f"{v},")
            s.write(f"\n{self.current.name}\n")    
            s.write(f"{self.weapon.name}\n")
            for i in self.inv:
                s.write(f"{i.name},")
            print("You saved the game!")
            time.sleep(1)
            return



    def __str__(self):
        return f"\nName: {self.name}\nSpecies: {self.species}\n------\n{self.stats}"



    


