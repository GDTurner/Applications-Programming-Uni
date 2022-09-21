import random, time

class ItemBase:
    def __init__(self, name, value):
        self.value = value
        self.name = name
        self.desc = "item text."



    def __str__(self):
        return f"{self.name} | {self.value} credits \n -------- \n{self.desc}"


class HealItem(ItemBase):
    def __init__(self, name, value, heal, healrange):
        super().__init__(name, value)
        self.heal = heal
        self.healrange = healrange
        self.desc = "Item Text"


    def __str__(self):
        return f"{self.name} | {self.value} credits \n -------- \n{self.desc}\n -------- \n{self.healrange} healing"


class MinorStim(HealItem):
    def __init__(self):
        super().__init__(name="Makeshift Stim", value=10, heal=random.randint(4, 12), healrange=('4 - 12'))
        self.desc = "A basic, widely available med. Boosts adrenaline, blood count and muscle regeneration."
        


class Weapon(ItemBase):
    def __init__(self, name, value, acc, damage, damrange, initbonus=0):
        super().__init__(name, value)
        self.accuracy = acc
        self.damage = damage
        self.damrange = damrange
        self.initbonus = initbonus


        self.desc = "this is an item"

    def attack_text(self):
        return "Text"

    def __str__(self):
        return f"{self.name} | {self.value} credits \n -------- \n{self.desc}\n -------- \n{self.damrange} damage"


class Deck(ItemBase):
    def __init__(self, name, value):
        super().__init__(name, value)

    def abilityA(self):
        pass

    def abilityB(self):
        pass


class Pipe(Weapon):
    def __init__(self):
        super().__init__(name="Pipe", value=2, acc=0, damage=random.randint(4, 8), damrange="4 - 8")
        self.desc = "A length of heavy metal piping."


    def attack_text(self):
        return "You swing the metal pipe hard."

class StunStick(Weapon):
    def __init__(self):
        super().__init__(name="Stun Stick", value=15, acc=0, damage=random.randint(4, 14), damrange="4 - 14")
        self.desc = """A metre long baton. A moulded plastic grip makes up the first quarter.\n 
        The remainder is thinner, set into the grip, and bolts of electricity crackle and jump between metal plates set into the top of the grip and the umbrella shaped end.\n
        Nasty..."""

    def attack_text(self):
        return "The Stun Stick crackles as it whistles through the air"

class Fists(Weapon):
    def __init__(self):
        super().__init__(name="Fists", value=0, acc=0, damage=random.randint(1, 5), damrange="1 - 5")
        self.desc = "Nothin' but knuckles"

    def attack_text(self):
        return "You swing your fists"

class StartDeck(Deck):
    def __init__(self):
        super().__init__(name="Battered HoloDeck", value=15)
        self.ability_a = "W1ld R1pp3r!"
        self.ability_b = "360 Whirlwind" 

   
    def item_text(self):
        print("""A beat up HoloDeck. A FireX3000; barely more than a kids deck... They say HoloDecks are based on something from the old days: planks of wood with wheels.
        \nYou wonder what happened when someone hit a crack... Or a rock. Or... anything??""")
        print("\n")
        time.sleep(0.75)
        print(f"Ability 1: {self.ability_a}\n")
        time.sleep(0.5)
        print(f"-------\n'Go animal when you use this wiiiiiiiild ability!!!'\n(Perform a weapon attack with a random damage modifer between -2 and +3 applied on hit)\n")
        time.sleep(0.5)
        print(f"Ability 2: {self.ability_a}\n")
        time.sleep(0.5)
        print(f"-------\n'Goons giving you trouble? Get them in such a twist they'll trip over their own feet trying to keep track of you!!'\n(Buff your dexterity by +5 for 3 turns)\n")
        time.sleep(1)
        print("*You could bowl a perfect game with how hard your eyes roll at the marketing on this holo*")
        time.sleep(1)
        return

    def abilityA(self, enemy, player):
        damage = random.randint(-2,3)
        print("Barely able to control the battered deck, you zip towards your enemy and lash out wildly with your weapon")
        player.attack_weapon(enemy, damage)

    def abilityB(self, player):
        player.stats.dexterity = 5
        player.timer = 3
        print("You set this old holo into overdrive. You start circling your foe at high speed. Running rings around them, you might say...")
        time.sleep(0.5)
        print("You've buffed your dexterity!")
        time.sleep(0.75)
        print(player.timer)
        print(player.stats.dexterity)
        return

    def __str__(self):
        return f"{self.name} | {self.value} credits \n -------- \n{self.item_text}"




# def abilityA(self, player):
#     strength = player.stats.strength
#     while player.timerA <= 2:
#         player.stats.strength = strength + 2
#         player.timerA += 1
#     else:
#         pass

# l = [Pipe(), StunStick()]
# p = l[0]
# print(p)