# A SELECTION OF SOURCES THAT OBVIOUSLY INFLUENCED MY WORK: https://python-forum.io/thread-20570.html , https://gamedev.stackexchange.com/questions/143523/movement-in-a-text-based-game-using-room-class-python
# https://codereview.stackexchange.com/questions/259245/python-text-based-game-room-to-room-movement , https://python-forum.io/thread-21.html
# https://stackoverflow.com/questions/15114843/accessing-dictionary-value-by-index-in-python , https://codereview.stackexchange.com/questions/161321/character-creation-in-text-adventure-proper-use-of-main-and-global-values
# https://replit.com/talk/learn/Python-Text-Adventure-RPG-Tutorial-2-orAdd-Character-and-Item-Objects/53299 , https://python-forum.io/thread-29477.html
# https://github.com/ramza/PythonTuts/blob/main/RPG_Character_Builder/random_character_generator.py.py




import world, items, time, random
import os.path
from pathlib import Path
from Character import Player, Eagle, Hawk, Owl, Falcon 

objects = {
    'items': {
        'Pipe': items.Pipe, 'Fists': items.Fists, 'Stun Stick': items.StunStick, 'Makeshift Stim': items.MinorStim, 'Battered HoloDeck': items.StartDeck
    },
    'rooms': {
        'start room': world.StartRoom, 'Hall1': world.Hall1, 'Pipe Room': world.PipeRoom, 'Goon Room': world.GoonRoom, 'Vent Shaft': world.VentShaft
    }
}



def load():
    with open("birdcage/txt_files/save_file.txt") as s:
        name = s.readline()
        species = s.readline()
        deck = s.readline()
        visitstr = s.readline()
        visited = visitstr.split(',')
        current = s.readline()
        weapon = s.readline()
        invstr = s.readline()
        inventory = invstr.split(',')

        player = Player(name.replace('\n', ''), species.replace('\n', ''))
        player.current = objects['rooms'][current.replace('\n', '')]()
        for x in visited:
            visited.pop()
            player.visited.append(x)
        if weapon:
                player.weapon = objects['items'][weapon.replace('\n', '')]()
        if deck:
                player.deck = objects['items'][deck.replace('\n', '')]()
        if inventory:
            inventory.pop()
            for x in inventory:
                player.inv.append(objects['items'][x]())

        print("You loaded a saved game!")     
        time.sleep(1)
        return player    

def species_desc(species):
    if species == "eagle":
        return Eagle()
    if species == "hawk":
        return Hawk() 
    if species == "owl":
        return Owl() 
    if species == "falcon":
        return Falcon()
    if species == "all":
        return f"{Eagle()}\n\n------\n{Hawk()}\n------\n{Owl()}\n------\n{Falcon()}\n------\n"
    if species == "stats":
        return f"\nStrength: adds this as a bonus to your damage\nDexterity: adds this as a bonus to your chance to hit and dodge attacks\nIntelligence: adds this as a bonus to your chance of going first in combat\n"  

def character_creation():

    def species_select():
        commands = ["eagle", "hawk", "owl", "falcon"]
        species = input("In The Birdcage, everyone in the world is an anthropomorphised bird. You are a bird of prey. Your choice here determines your stats.\n(eagle | hawk | owl | falcon | stats | all): >>> ")
        description = species_desc(species.lower())
        if species.lower() in commands:
            print(description)    
            ans = input(f"Would you like to select - {species.title()} - as your stat selection?: (y/n) >>> ")
            if ans.lower() == "y":
                cc.append(species)
                player = Player(cc[0], cc[1])
                print(player)
                return player
            elif ans.lower() == "n":
                species_select()
            else:
                ans = input("Please type a valid input: (y/n) >>> ")
        elif species.lower() == "all":
            print(description)
            species_select()
        elif species.lower() == "stats":
            print(description)
            species_select()


    cc = []
    while True:
        name = input("Please enter your name: >>> ")
        i = input(f"Are you happy with: {name}? (y/n): >>> ")
        if i.lower() == "y":
            cc.append(name)
            return species_select()
        elif i.lower() == "n":
                break
        else: print("Please type *y* or *n*")
            

# The ascii text was created using: https://patorjk.com/software/taag/
def intro():
    with open("birdcage/txt_files/intro.txt") as title:
        contents = title.read()
        print(contents)

    i = input("Do you have a save file? (y/n): >>> ")
    if i == 'n':
        while True:
            i = ""
            i = input("Would you like to play? (y/n): >>> ")
            if i.lower() == "y":
                return character_creation()
            elif i.lower() == "n":
                print("See ya!")
                break
            else:
                print("Please type *y* or *n*")
    # path.lib method to check file from:  https://stackoverflow.com/questions/57375806/how-can-i-check-if-a-file-exists-in-python         
    elif i == 'y':
        s_file = Path('birdcage/txt_files/save_file.txt')
        if s_file.is_file():
            return load()
        else:
            print("You don't have a save file!")
            time.sleep(2)
            main()


    


def main():
    player = intro()
    # player.inv.append(items.MinorStim())
    current_room = player.current
    global_actions = ['inventory', 'heal', 'holodeck', 'equipped', 'save']
    i = ""
    while True:
        # print(current_room.intro_text())
        current_room.player_effect(player)     
        i = input('\nWhat would you like to do?\n')
        print("\n")
        if i in current_room.exits:
            player.current = current_room.exits[i]()
            current_room = current_room.exits[i]()
        elif i.lower() in global_actions:
            action = getattr(player, i)
            if action:
                action()
        elif i.lower() == "quit":
            print("See ya later, space cowboy.")
            break
        elif i.lower() == "help":
            print("\n")
            for i in global_actions:
                print(f"*{i.title()}*")
            print("\n\n")
            time.sleep(1)
        else:
            print('Can\'t recognise that command')
            time.sleep(1.5)
            print('Nerd...')
            time.sleep(0.5)
    
main()     

