import time, enemies
from combat import Combat_func
from Character import *



### https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-4-the-game-loop/
### This source was invaluable for understanding how I could utilise classes. This source directly inspired me to my class inheritance from 'a -> b, c -> d' etc 
# to having one base class that all other classes inherit from. It also gave me the idea of taking my existing 'player_effect' method and using that as the gateway to the room objects
#instead of previously calling intro_text methods and fairly complicated if/else logic to select the right method of the class

# player = Player("guy", "eagle")
class BasicRoom:
    def __init__(self, name, exits, actions):
        self.name = name
        self.exits = exits
        self.actions = actions
        
    def intro_text(self, player):
        raise NotImplementedError()

    def player_effect(self, player):
        pass
    
    def __str__(self):
        return self.name


class ItemRoom(BasicRoom):
    def __init__(self, name, exits, actions, item):
        super().__init__(name, exits, actions)
        self.items = item
        

class EncounterRoom(BasicRoom):
    def __init__(self, name, exits, actions, enemy):
        super().__init__(name, exits, actions)
        self.enemy = enemy


    def enemy_intro(self):
        if self.enemy.hp() > 0:
            return """Enemy Intro"""
        else:
            return """Enemy is dead"""

    # def 





class StartRoom(BasicRoom):
    def __init__(self):
        exit_list = {"north": Hall1}
        action_list = {}
        super().__init__(name="start room", exits=exit_list, actions=action_list)
        

    
    def intro_text(self, player):
        if self.name in player.visited:
            return """Your cell is much as it was. A grey concrete box, suspended in dim green light. Only one way in or out *north*."""
        else:
           print("""\nYou blink awake. Your eyes take a moment to adjust to the dim, sickly green glow of the fluorescent light above you.""") 
           return "Now you're used to the gloom, you can see the cell door is open to the *north* in front of you."
            
    def player_effect(self, player):
        print(self.intro_text(player))
        if self.name not in player.visited:
            player.visited.append(self.name)

                
            

class Hall1(BasicRoom):
    def __init__(self):
        exit_list = {'north': PipeRoom, 'south': StartRoom}
        action_list = {}
        super().__init__(name="Hall1", exits=exit_list, actions=action_list)

    def intro_text(self, player):
        if self.name in player.visited:
            return """A featureless concrete corridor. A door stands on the *north* end and the opening to your cell the *south*."""

        else:
            return """After a few moments adjusting yourself to the waking world, you roll your shoulders and step through the narrow concrete doorway and out into the hallway beyond.\n\n
            A long concrete corridor; featureless. The same green lights dot the cieling at regular intervals.\n 
            Only a door lies in front of you to the *north*, and your cell just behind to the *south*.
             """
    
    def player_effect(self, player):
        print(self.intro_text(player))
        if self.name not in player.visited:
            player.visited.append(self.name)
                   
    

class PipeRoom(ItemRoom):
    def __init__(self):
        exit_list = {'south': Hall1, 'ladder': GoonRoom}
        action_list = {}
        item_list = [items.Pipe()]
        super().__init__(name="Pipe Room", exits=exit_list, item=item_list, actions=action_list)
        

    def intro_text(self, player):
        if self.name in player.visited:
            return """A dirty, litter-filled room. At one end, a door exits into a hallway *south*. The only other exit is a rusty *ladder*."""
        else:
            print("""Another unremarkable room. Oblong in shape, grey walls and green lights.\nSome refuse and debris are scattered across the floor. A battered bit of piping catches your eye from amongst the litter.\nYou pick it up and give it a test swing.\n""")
            time.sleep(1)
            print(".....")
            time.sleep(1)
            print("It'll do...")
            self.add_inventory(player)
            return "On the far side of the room you see a ladder (ladder). A quick glance reveals it's the only other exit."
            
            
    def add_inventory(self, player):
        for item in self.items:
            print(f"You added: {item} to your inventory.")
            player.inv.append(item)
            player.weapon = item
            time.sleep(1)
        return

    def player_effect(self, player):
        print(self.intro_text(player))
        if self.name not in player.visited:
            player.visited.append(self.name) 
            
class VentShaft(ItemRoom):
    def __init__(self):
        exit_list = {'south': GoonRoom, 'west': GoonRoom}
        action_list = {}
        item_list = [items.MinorStim(), items.MinorStim()]
        super().__init__(name="Vent Shaft", exits=exit_list, item=item_list, actions=action_list)
        

    def intro_text(self, player):
        if self.name in player.visited:
            return """An old vent shaft with a sharp turn in it. You can exit to the *south* or the *west*"""
        else:
            print("You squeeze yourself into the vent shaft. It's murder on your knees...")
            time.sleep(1)
            print("As you're crawling, you find two discarded medical stims. They look old, but the seals are still in tact.")
            time.sleep(0.5)
            print("Mama said don't take sweets from stangers. She said nout about using strange needles you find in a vent.")
            print("You pocket them and crawl on.")
            time.sleep(1)
            self.add_inventory(player)
            return "The vent takes a sharp turn to the *west*. The room where that goon rushed you is *south*."
            
            
    def add_inventory(self, player):
        for item in self.items:
            print(f"\nYou added: {item} to your inventory.")
            player.inv.append(item)
            time.sleep(0.25)
        return

    def player_effect(self, player):
        print(self.intro_text(player))
        if self.name not in player.visited:
            player.visited.append(self.name)         



class GoonRoom(EncounterRoom):
    def __init__(self):
        exit_list = {'ladder': PipeRoom, 'vent':VentShaft}
        action_list = {}
        foe = enemies.Goon()
        # item_list = [items.Pipe()]
        super().__init__(name = 'Goon Room', exits=exit_list, enemy=foe, actions=action_list)

    def intro_text(self):
        return """The goon lies dead. You look around and see two exits. A large door to the *west* and a *vent* shaft that looks big enough to crawl through. There's also the *ladder* you came up."""

            

    def enemy_intro(self):
            return """As you pull yourself up from the ladder, a nasty looking brute of a goon rushes you."""

    
    def player_effect(self, player):
        if self.name not in player.visited:
            print(self.enemy_intro())
            Combat_func(player, self.enemy)
            player.visited.append(self.name) 
            print(self.intro_text())
        else:
            print(self.intro_text())



        
        # TRY OBFUSCATING TO A COMBAT CLASS?
        
# def main():
#     player = Player("Guy", "eagle")
#     player.inv.append(items.MinorStim())
#     current_room = StartRoom()
#     global_actions = {'inventory': 'inventory'}
#     i = ""
#     while i != 'quit':
#         # print(current_room.intro_text())
#         current_room.player_effect(player)     
#         i = input('\nWhat would you like to do?\n')
#         if i in current_room.exits:
#             current_room = current_room.exits[i]()
#         elif i in global_actions:
#             action = getattr(player, i)
#             if action:
#                 action()      
#         else:
#             print('Cant go that way')
#             time.sleep(1.5)
#             print('Nerd...')
#             time.sleep(0.5)
    
# main()       
        



# current_room = StartRoom()
# print(current_room.exit_list)

# print(player.__dict__)


# player = Player("Guy", "eagle")
# # player.maxHP = player.stats.hp
# print(player.stats)
# print(player.maxHP)








#             if weapon in data.objects.items
# if i in current_room.exits:
#     player.current = current_room.exits[i]()
#     current_room = current_room.exits[i]()

