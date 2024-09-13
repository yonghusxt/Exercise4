import random 
import time
from copy import deepcopy

card_deck = {
    "a": {"Name":"Diablo","Health": 100, "Attack": 90, "Defense": 60},
    "b": {"Name":"Medusa","Health": 100, "Attack": 70, "Defense": 70},
    "c": {"Name":"Jester","Health": 120, "Attack": 60, "Defense": 90},
    "d": {"Name":"Troll","Health": 150, "Attack": 40, "Defense": 94},
    "e": {"Name":"Specter","Health": 100, "Attack": 70, "Defense": 70},
    "f": {"Name":"Mist", "Health": 100, "Attack": 75, "Defense": 65},
    "g": {"Name":"Savage", "Health": 100, "Attack": 90, "Defense": 50},
    "h": {"Name":"Marauder", "Health": 100, "Attack": 85, "Defense": 50},
    "i": {"Name":"Wimp","Health": 110, "Attack": 40, "Defense": 85},
    "j": {"Name":"Sorcerer","Health": 100, "Attack": 70, "Defense": 55}
}
deck_size = 3


#The following is used to draw randomly n number of cards from the deck, where n = deck_size
player = random.sample(list(card_deck.items()), deck_size)
opponent = random.sample(list(card_deck.items()), deck_size)


player_deck_copy = dict(player)
opponent_deck_copy = dict(opponent)

player_deck = deepcopy(player_deck_copy)
opponent_deck = deepcopy(opponent_deck_copy)

def inner1(name1,name2,attack,defence,health):
    print(f"Both {name1} and {name2} are now battling it out \nUsing your warrior {name1},")
    print(f"  you attacked with a force of {attack} Newton")
    print(f"  and your opponent resisted it with a force of {defence} Nekton.")
    print(f"  At the end of this turn,your opponent's health is {health}")

def inner2(name1,name2,attack,defence,health):
    print(f"Both {name1} and {name2} are now battling it out \nUsing your warrior {name1},")
    print(f"  your opponent's attack with a force of {attack} Newton")
    print(f"  and your resisted it with a force of {defence} Nekton.")
    print(f"  At the end of this turn,your health is {health}")


while len(player_deck)>0 and len(opponent_deck)>0:
    print()
    print("Player's turn: ")
    for k in player_deck.keys():
        print(f"card number: {k}")
        print(f"Name: {player_deck[k]['Name']}")
        print(f"Health: {player_deck[k]['Health']}")
        print(f"Attack: {player_deck[k]['Attack']}")
        print(f"Defense: {player_deck[k]['Defense']}")
        print()
    
    opp = random.choice(list(opponent_deck.keys()))
    print(f"Your opponent has chosen {opponent_deck[opp]['Name']} for this round")
    print()
    print(f"Health: {opponent_deck[opp]['Health']}")
    print(f"Attack: {opponent_deck[opp]['Attack']}")
    print(f"Defense: {opponent_deck[opp]['Defense']}")
    print()
    number = input("Select the card number you want to dispatch:")
    print()
    if player_deck[number]['Attack'] >= (opponent_deck[opp]['Health']+opponent_deck[opp]['Defense']):
        inner1(player_deck[number]['Name'],opponent_deck[opp]['Name'],player_deck[number]['Attack'],opponent_deck[opp]['Defense'],0)
        opponent_deck.pop(opp)
        if len(player_deck)>0 and len(opponent_deck)>0:
            print(f"\nNext round will begin in 3 seconds")
            time.sleep(3)
        continue
    else:
        if opponent_deck[opp]['Defense']>=player_deck[number]['Attack']:
           opponent_deck[opp]['Defense']=opponent_deck[opp]['Defense']-player_deck[number]['Attack']
           inner1(player_deck[number]['Name'],opponent_deck[opp]['Name'],player_deck[number]['Attack'],player_deck[number]['Attack'],opponent_deck[opp]['Health'])
        else:
            opponent_deck[opp]['Health']=opponent_deck[opp]['Health']+opponent_deck[opp]['Defense']-player_deck[number]['Attack']
            inner1(player_deck[number]['Name'],opponent_deck[opp]['Name'],player_deck[number]['Attack'],opponent_deck[opp]['Defense'],opponent_deck[opp]['Health'])
            opponent_deck[opp]['Defense']=0

    print()
    print("Opponent's turn: ")
    print(f"Now your opponent will attack in 3 seconds: \n")
    time.sleep(3)
    if opponent_deck[opp]['Attack'] >= (player_deck[number]['Health']+player_deck[number]['Defense']):
        inner2(player_deck[number]['Name'],opponent_deck[opp]['Name'],opponent_deck[opp]['Attack'],player_deck[number]['Defense'],0)
        player_deck.pop(number)
        if len(player_deck)>0 and len(opponent_deck)>0:
            print(f"\nNext round will begin in 3 seconds")
            time.sleep(3)
        continue
    else:
        if player_deck[number]['Defense']>=opponent_deck[opp]['Attack']:
           player_deck[number]['Defense']=player_deck[number]['Defense']-opponent_deck[opp]['Attack']
           inner2(player_deck[number]['Name'],opponent_deck[opp]['Name'],opponent_deck[opp]['Attack'],opponent_deck[opp]['Attack'],player_deck[number]['Health'])
           if len(player_deck)>0 and len(opponent_deck)>0:
            print(f"\nNext round will begin in 3 seconds")
            time.sleep(3)
           continue
        else:
            player_deck[number]['Health']=player_deck[number]['Health']+player_deck[number]['Defense']-opponent_deck[opp]['Attack']
            inner2(player_deck[number]['Name'],opponent_deck[opp]['Name'],opponent_deck[opp]['Attack'],player_deck[number]['Defense'],player_deck[number]['Health'])
            player_deck[number]['Defense']=0
            if len(player_deck)>0 and len(opponent_deck)>0:
                print(f"\nNext round will begin in 3 seconds")
                time.sleep(3)
            continue

if len(player_deck)==0:
    print()
    print("Sorry, you lost the game.")

if len(opponent_deck)==0:
    print()
    print("Congratulations, you have won the game.")