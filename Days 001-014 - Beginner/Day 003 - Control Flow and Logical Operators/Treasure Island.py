print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n") 

print('You come to a crossroads in the labyrinth.')
if input('Would you like to go Left or Right? ') == 'Left':
    print('\nIn the next room, there are three doors across a pool of water.')
    if input('Would you like to try and Swim across, or Wait? ') == "Wait":
        print('\nAfter an excruciatingly long time, the pool of water evaporates. You walk across and climb up the wall.')
        door = input('Before you are three doors; one Red, one Blue, and one Yellow. Which one do you pick? ')
        if door == 'Red':
            print('\nThe door lights on fire as you grab the doorknob, engulfing you instantly.')
            print('Game Over.')
        elif door == 'Blue':
            print('\nThis room contains countless indescribable beasts. They tear into your flesh with tooth and claw.')
            print('Game Over.')
        elif door == 'Yellow':
            print('\nNot only is the door yellow; it\'s actually solid gold! You take it off the hinges and bring it home with you, never venturing deeper.')
            print('You Win!.')
        else:
            print('\nYou are overwhelmed by the prospect of a third choice, and your brain instead opts to take none of the choices presented.')
            print('You stay trapped in that room for the rest of your short life, endlessly contemplating the possibilities.')
            print('Game Over.')
    else:
        print('You are attacked by a particularly angry trout.')
        print('Game Over.')
else:
    print('You fall into a hole.')
    print('Game Over.')