from sys import exit
inventory = []
gold = 0
health = 10
skeleton_key_have = False
# requirement for treasure room
leather_vest_have = False
# when true allows you to beat mugger encounter with no damage
sword_have = False
# true = allows to beat mugger encounter

# sets health cap
if health > 10:
    health = 10
# death / game over mechanic
if health == 0:
    gameover()
# defines game win
def gamewin():
    print("You win! (for now. I'll be working on this project more later.)")
    exit()
# defines game over
def gameover():
    print("You died. Game over.")
    exit()
# defines inn area
def inn():
    global skeleton_key_have
    print('''You walk into the inn. It's a quiet place, mostly empty. There are a couple men playing some sort of game in the corner. There's also a door in the back of the room that you heard the crier talking about.
    There's also a lass sitting on one of the benches. She looks at you and beckons you over with a finger.''')
    choice = input('''Who do you talk to?
    > ''')
    if "lass" in choice.lower():
            print('''
            You walk over to her and introduce yourself.
            'Looking for a good time, adventurer? I normally charge but... you're quite cute.''
            ''')
            sex = input("""Do you go with her? Y/N
            > """)
            if "Y" in sex.upper():
                print("""You two go upstairs and you have the best sex of your life.""")
                print("You wake up the next day with AIDS and immediately die. LOL get rekt")
                gameover()
            if "N" in sex.upper():
                "You politely decline and walk away."
                inn()
    if "men" in choice.lower():
        print('''One of them looks at you, sneers and says "fuck off, will ye?"
        ''')
        inn()
    if "leave" in choice.lower():
        city()
    if "door" in choice.lower():
        if skeleton_key_have == False:
            print("You come upon a door in the back of the room. It has a lock unlike one you've ever seen before. Maybe there's something in town that can unlock it?")
            inn()
        elif skeleton_key_have == True:
            print("You unlock the door. There's treasure beyond your wildest dreams behind it! You're rich!")
            gamewin()
# defines town crier event
def crier():
    print("You overhear the town crier saying someting")
    print('"Hear ye, hear ye! The door in the back of the inn is said to contain immense wealth, but no one has the ability to unlock it!"')
    print("That's interesting. I wonder if you can unlock the door?")
    city()
# defines bard game
def bard():
    print('''You walk over to the bard, who offers you a riddle. "Solve this and I'll give you 50 gold coins!"
    "Mary has four daughters and each of her daughters has a brother. How many children does Mary have?"
    ''')
    answer = int(input('''What is the answer to the riddle?
    > '''))
    if answer == 5:
        global gold
        gold = gold + 50
        print(f"You win 50 gold coins!")
        print(f"You now have {gold} gold coins.")
        city()

    else:
        print("Incorrect. Try again? Y/N")
        answer = input("> ")
        if answer.upper() == 'Y':
            bard()
        elif answer.upper() == 'N':
            city()
        else:
            print("I can't understand that.")
            bard()
    city()
# defines blacksmith event
def blacksmith():
    global gold
    global sword_have
    global leather_vest_have
    global skeleton_key_have
    longsword = 10
    leather_vest = 18
    skeleton_key = 55
    wares = [longsword, leather_vest, skeleton_key]
    show_wares = input('''
    Would you like to purchase anything today? Y/N
    > ''')
    if "Y" in show_wares.upper():
        print(f'''Longsword: {wares[0]}
Leather Vest: {wares[1]}
Skeleton Key: {wares[2]}''')
        player_choice = input("> ")
        if "sword" in player_choice.lower():
            if gold >= longsword:
                gold = gold - longsword
                inventory.append("Longsword")
                sword_have = True
                print(f"Your inventory now has: {inventory}")
                print(f"You now have {gold} gold.")
                blacksmith()
            else:
                print("You can't afford that.")
                blacksmith()
        elif "vest" in player_choice.lower():
            if gold >= leather_vest:
                gold = gold - leather_vest
                inventory.append("Leather Vest")
                leather_vest_have = True
                print(f"Your inventory now has: {inventory}")
                print(f"You now have {gold} gold.")
                blacksmith()
            else:
                print("You can't afford that.")
                blacksmith()
        elif "key" in player_choice.lower():
            if gold >= skeleton_key:
                skeleton_key_have = True
                gold = gold - skeleton_key
                print("This might be useful later.")
                print(gold)
                blacksmith()
            else:
                print("You can't afford that.")
                blacksmith()
        else:
            print("I don't have any of those.")
            blacksmith()

    if "N" in show_wares.upper():
        print("Okay, have a nice day!")
        city()
# defines merchant event
def merchant():
    print("""The merchant looks you up and down and scoffs. "You don't have any coin. I can tell by the rags you're wearing.
    Come back when you actually have something to trade me, peasant.""
    """)
    choice = input("""Sadly, he's right. You're broke. Maybe another time, then.
Who do you talk to next?
    > """)
    if "sailor" in choice.lower():
        sailor()
    elif choice == "old man" or "drunk" in choice.lower():
        drunk()
    elif "dog" in choice.lower():
        dog()
    elif "merchant" in choice.lower():
        merchant()
    elif "mercenary" in choice.lower():
        mercenary()
    else:
        print("I can't understand that.")
        merchant()
# defines mugger event
def mugger():
    global health
    global gold
    print("You walk down one of the side streets. A small man comes out with a knife." )
    print('"Your money, or your life!"')
    action = input("What do you do? ")
    if "run" in action.lower():
        print("You run away, but not before he manages to stick you in the side.")
        health = health - 2
        print(f"You now have {health} health.")
        city()
    elif "fight" in action.lower():
        if sword_have == True and leather_vest_have == False and health >= 6:
            print("You swing your sword at the mugger and chop his head clean off, but he manages to stab you in the chest at the same time.")
            print("You take his money.")
            health = health - 6
            print(f"You now have {health} health")
            gold = gold + 20
            print(f"You now have {gold} gold.")
            city()
        if sword_have == False or health <= 6:
            print("You try to fight the mugger but he kills you in cold blood.")
            gameover()
        if sword_have == True and leather_vest_have == True:
            print("You swing your sword at the mugger and chop his head clean off. He tries to stab you, but your vest protects you.")
            print("You take his money.")
            gold = gold + 20
            print(f"You now have {gold} gold.")
            city()
        else:
            print("You didn't act correctly. He kills you in cold blood.")
            gameover()
    city()
# defines city, hub of stage 2
def city():
    print("""Around you, you can see a couple things. There's a bard singing a song in the center of the city, as well as an inn you can enter.
    There are a few side streets that you can go down, as well as the town blacksmith.""")
    choice = input('''Where do you go?
    > ''')
    if "inn" in choice.lower():
        inn()
    elif "crier" in choice.lower():
        crier()
    elif "bard" in choice.lower():
        bard()
    elif "blacksmith" in choice.lower():
        blacksmith()
    elif "street" in choice.lower():
        mugger()
    else:
        print("I can't understand that.")
        city()
# defines sailor text
def sailor():
    print('''The man of the pair looks at you and jumps. "Whaddya want, huh?
    Haven't you heard about minding your own fuckin' business?"
    ''')
    choice = input("""Well that was rude.
    Who else do you talk to?
    > """)
    if "sailor" in choice.lower():
        sailor()
    elif choice.lower() == "old man" or "drunk" in choice:
        drunk()
    elif "dog" in choice.lower():
        dog()
    elif "merchant" in choice.lower():
        merchant()
    elif "mercenary" in choice.lower():
        mercenary()
    else:
        print("I can't understand that.")
        sailor()
# defines mercenary text, allows user to move to hub 2
def mercenary():
    print("""You walk over to the mercenary captain. He looks you over and says "Looking to
    travel with us, adventurer? You don't look like you'll make it there yourself.
    """)
    accept = input('''Do you accept? Y/N
    > ''')
    if accept.upper() == "Y":
        city()
    elif accept.upper() == "N":
        start()
    else:
        print("I can't understand that.")
        mercenary()
# defines drunk old man
def drunk():
    print("The old man who was previously screaming at the sky looks over at you and smiles."
    """
    Wwww-We got some ff-fresh meat he- *hic* I mean, an adventurer.
    He sobers up suddenly. "Let me tell you a little bit about this place.
    The creator of this land was... maybe not the greatest at his job. You could say he was
    a beginner of sorts. So keep that in mind while you wander around here. You've got 10 health, and combat
    will reduce it. You can gain back your health through various means, like drinkin' some spirits.
    Everybody here will talk to you but not everyone is friendly. And think outside the box sometimes - the answer
    will not always be obvious. Go along now!
    If the guy who made this was smarter, you'd be able to talk to me but alas, today is not that day."
    He seemingly becomes incredibly intoxicated again, and stumbles off the pier into the water.""")
    choice = input("""Who do you talk to next?
    > """)
    if "sailor" in choice.lower():
        sailor()
    elif choice == "old man" or "drunk" in choice.lower():
        drunk()
    elif "dog" in choice.lower():
        dog()
    elif "merchant" in choice.lower():
        merchant()
    elif "mercenary" in choice.lower():
        mercenary()
    else:
        print("I can't understand that.")
        drunk()
# defines dog text. i like dogs :)
def dog():
    print("The dog looks at you, then runs away.")
    choice = input("""Who do you talk to next?
    > """)
    if "sailor" in choice.lower():
        sailor()
    elif choice == "old man" or "drunk" in choice.lower():
        drunk()
    elif "dog" in choice.lower():
        dog()
    elif "merchant" in choice.lower():
        merchant()
    elif "mercenary" in choice.lower():
        mercenary()
    else:
        print("I can't understand that.")
        dog()
# defines intro sequence
def start():
    print("ZzzzzZzzzzzzzZzzzzzzz......")
    print("""
    You wake up with a start. Seems the boat has come into port.
    Around you, you see a drunk old man screaming at the sky. There's also
    two sailors, a man and a woman. They look worried, and are talking in hushed
    voices. There's a merchant that looks to be from the far away land of Asgaar, as well as a stray dog.
    Just past them, you see a group of mercenaries. They look like they're going to continue to the inner city soon.""")
    print('''
        You should probably talk to someone to get your bearings.''')
    choice = input('''Who do you choose?
    > ''')
    if "sailor" in choice.lower():
        sailor()
    elif choice == "old man" or "drunk" in choice.lower():
        drunk()
    elif "dog" in choice.lower():
        dog()
    elif "merchant" in choice.lower():
        merchant()
    elif "mercenary" in choice.lower():
        mercenary()
    else:
        print("I can't understand that.")
        start()

start()
