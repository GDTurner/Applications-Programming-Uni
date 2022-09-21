# import random
# import birdcage.data as data
# from birdcage.Character import Player

# from birdcage.Character import Player

# # class Ability:
# #     def __init__(self, name, ability):
# #         self.name = name
# #         self.ability = ability

# #     def desc(self):
# #         print("Sick tricks bro")

# #     def display(self):
# #         print(f"You do a sick trick that buffs you by 2 for two turns.")
# #         return self.ability


# # test = Ability("pogs", 5)
# # test.display()

# # i = test.display() + 5
# # print(i)
# class Room:
#     def __init__(self, name, exits, description):
#         self.name = name
#         self.exits = exits
#         self.description = description
#         self.visited = 0



# class Lobby(Room):
#     def __init__(self):
#         exit_list = {"north":Lounge, "south":Airlock}
#         super().__init__("an empty lobby", exit_list, "There is an empty desk in the room.\nThe floors are made of cold metal.")
#         self.visited += 1        
#     def visit(self):    
#         print(self.visited)


# class Lounge(Room):
#     def __init__(self):
#         exit_list = {"south":Lobby}
#         super().__init__("a quiet lounge", exit_list, "The bartender asks what you want.")
#         self.visited += 1   
#     def visit(self):    
#         print(self.visited)

# class Airlock(Room):
#     def __init__(self):
#         exit_list = {"north":Lobby}
#         super().__init__("a cold landing pad", exit_list, "There is a ship parked here")
#         self.visited += 1      
#     def visit(self):    
#         print(self.visited)

# def main():
#     current_room = Lobby()
#     d = ""
#     while d != 'quit':
#         print(current_room.name)
#         print(current_room.visit())
#         d = input('\nWhich way do you want to go?\n')
#         if d in current_room.exits:
#             current_room = current_room.exits[d]()
#         else:
#             print('Cant go that way')

# main()



# def rand():
#     return random.randint(1,10)

# damage = rand()
# hp = 100
# while True:
#     damage = rand()
#     if hp > 0:
#         i = input("x to attack: >>> ")
#         if i == "x":
#             hp -= damage
#             print(f"You did {damage} damage. They have {hp} hp remaining.")
#     else:
#         print("you win!")
#         break


# while True:
#     x = input("x: ")
#     if x == "x":
#         print("do a thing")
#         y = input("an input")
#     print("now we're out of the if block")
#     z = input("Press y to clap your hands")
#     print("clap your hands")

# class TestRoomA:
#     def __init__(self, a , b):
#        self.a = a
#        self.b = b
#        self.c = [a, b]

#     def __str__(self):
#         return str(self.c)


# one = TestRoomA('a', 'b')
# print(one)

# x = ['a','b','c','d','e']
# y = len(x) + 1
# print(y)

# with open("birdcage/txt_files/intro.txt") as title:
#     contents = title.read()
#     print(contents)



