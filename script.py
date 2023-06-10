# Tearlaments Coding Suite - By Gabriel Netz 
# @Gabriel_Netz on Twitter
# metafy.gg/@Gabriel_Netz for coaching
# check out TheDisciplesTCG Youtube/Twitter/Instagram :D

import requests
import json
import pprint
import defines
import random
import copy

def getDeck(file):
    with open(file) as f:
        deck = f.read().splitlines()

    deck.pop(0)
    deck.pop(0)
    decksize = deck.index("#extra")
    deck = deck[:decksize]

    cards = []

    # Step 2: API Calls
    for card in deck:
        response = requests.get(f"https://db.ygoprodeck.com/api/v7/cardinfo.php?id={card}")
        info = json.loads(response.text)
        info = info["data"][0]
        if "Monster" in info["type"]:
            bonus = False
            if info["name"] in defines.good_mills_list:
                bonus = True 
            cards.append({"Name": info["name"], "Attribute": info["attribute"],"Type": info["race"], "CardType": info["type"], "GoodMill" : bonus})
        else:
            bonus = False
            if info["name"] in defines.good_mills_list:
                bonus = True
            cards.append({"Name": info["name"], "CardType": info["type"], "GoodMill" : bonus})
    random.shuffle(cards)
    return cards

def draw(deck,n):
    random.shuffle(deck)
    drawn_cards = deck[0:n]
    del deck[:n]
    return deck, drawn_cards

def mill(deck,n):
    deck, mill = draw(deck,n)
    millScore = 0
    for card in mill:
        if card["GoodMill"] == True:
            millScore += 1
    return deck, mill, millScore


runs = []
deck_complete = getDeck('tear1.ydk')
for i in range(0,1000):
    deck = copy.copy(deck_complete)
    deck, hand = draw(deck,5)

    deck, mill_output, millScore = mill(deck, 5)
    runs.append(millScore)

for value in set(runs):
    print(f"{value} = {runs.count(value)/1000}")

    







































# Step 3: Actual Logic

# def getScore(card,comparison):
#     score = 0
#     for key in card:
#         if card[key] == comparison[key]:
#             score = score + 1
#     return score


# for card in deckmonsters:
#     monsterbridges[card] = []
#     for key in deckmonsters:
#         score = getScore(deckmonsters[card],deckmonsters[key])
#         if score == 1:
#             print(f"Card {card} bridges with {key}")
#             monsterbridges[card].append(key)
#             print(monsterbridges[card])
            

# pprint.pprint(monsterbridges)
# # Right Now, monster-bridges is a dict with all cards that connect to each other. Now, we want to output all the cards each card can search

# f = open("output.txt", "a")
# f.truncate(0)
# for card in monsterbridges:
#     for key in monsterbridges[card]:
#         for target in monsterbridges[key]:
#             print(f"Banish {card} ---> Reveal {key} ---> Add {target}")
#             f.write(f"Banish {card} ---> Reveal {key} ---> Add {target}\n" )