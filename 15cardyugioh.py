#--------
#Aiden Krahn
#TenCardYuGiOh
#December ??? 2022
#--------

import random
#start with lists header---
#what a monster looks like
#[atk, def, lvl, name, ifdefpos]
gy1 = []#had to be put in right order, don't worry about it
gy2 = []

#listofcards
FireGrass = [700, 600, 2, 'FireGrass', 0]
KagemushaoftheBlueFlame = [800, 400, 2, 'KagemushaoftheBlueFlame', 0]
Gokibore = [1200, 1400, 4, 'Gokibore', 0]
SkullServant = [300, 200, 1, 'SkullServant', 0]
Niwatori = [900, 800, 3, 'Niwatori', 0]
LordofD = [1200, 1100, 4, 'LordofD', 0]
HungryBurger = [1000, 950, 4, 'HungryBurger', 0]
Anteatereatingant = [1000, 250, 4, "Anteatereatingant", 0]
GreatLongNose = [950, 1700, 3, "GreatLongNose", 0]
AxeRaider = [1700, 1150, 4, "AxeRaider", 0]
CelticGuardian = [1400, 1200, 4, "CelticGuardian", 0]
FeralImp = [1300, 1400, 4, "FeralImp", 0]
HornImp = [1300, 1000, 4, 'HornImp', 0]
HitotsumeGiant = [1200, 1000, 4, 'HitotsumeGiant', 0]
ShiningFriendship = [750, 500, 2, 'ShiningFriendship', 0]
SaggitheDarkClown = [600, 1500, 3, 'SaggitheDarkClown', 0]
MammothGraveyard = [1200, 800, 3, 'MammothGraveyard', 0]
Kuriboh = [300, 200, 1, 'Kuriboh', 0]
BeaverWarrior = [1200, 1500, 3, 'BeaverWarrior', 0]
BattleOx = [1700, 1000, 4, 'BattleOx', 0]
VorseRaider = [1700, 1200, 4, 'VorseRaider', 0]
WormDrake = [1400, 1500, 4, 'WormDrake', 0]
BirdFace = [1600, 1600, 4, 'BirdFace', 0]
DodododwarfGogogoglove = [0, 1600, 4, 'DodododwarfGogogoglove', 0]
ToadallyAwesome = [1400, 800, 3, 'ToadallyAwesome', 0]
LittleD = [1100, 700, 2, 'LittleD', 0]#innuendos are funny.
ShadowGhoul = [1300, 200, 3, 'ShadowGhoul', 0]
BlueEyesWhiteDragon = [3000, 2500, 8, 'BlueEyesWhiteDragon', 0]
Exodia = [1000, 1000, 3, 'Exodia', 0]
BlackLusterSoldier = [3000, 2500, 8, 'BlackLusterSoldier', 0]

monsterzone1 = []
spellzone1 = []#remnants of
monsterzone2 = []
spellzone2 = []#a bygone era
deck1 = [AxeRaider, SkullServant, Anteatereatingant, FireGrass,
         KagemushaoftheBlueFlame, Kuriboh, SaggitheDarkClown, HornImp,
         HitotsumeGiant, ShiningFriendship, VorseRaider, ShadowGhoul,
         ToadallyAwesome, BirdFace, Exodia]
deck2 = [Gokibore, LordofD, HungryBurger, GreatLongNose, CelticGuardian,
         Niwatori, FeralImp, BattleOx, MammothGraveyard, BeaverWarrior, LittleD,
         DodododwarfGogogoglove, WormDrake]



hand1 = []#What's in the hand. stuff from deck will be added later
hand2 = []


#defenitions Header---

def dotheglobalsummoncounter():
    global summoncounter
    summoncounter = 0#resets summoncounter

def drawphase():
    print("Draw Card.")
    hand1.append(deck1.pop(0))
#draws a card
def standbyphase():
    print("Wait")
#standbyphase is useless
def main1phase():
    mph = True
    
    print("This is your hand-", hand1)
    print("This is your field-", monsterzone1)
    print("This is the enemies field-", monsterzone2)
    print(f"Your life points {lp1} and opponents life points {lp2}")

    while mph == True:#allows you to to a lot of inputs
        action = input("What will you do?(inspect, summon, change position(cs), or end.)  ")
        if action == "inspect":
            print("Your field-", monsterzone1)
            print("Opponents field-", monsterzone2)
            
        elif action == "cs":
            if len(monsterzone1) == 0:
                print("Nothing to defend.")
                
            else:
                varsol = int(input("What monster changes position?  "))
                varsol2 = input("Defend or attack position?  ")
                defend1(varsol, varsol2)
            
        elif action == "summon":
            
            if summoncounter == 0:#checks to see how many times you've summoned this turn
                normalsummon1()
                
            else:
                print("Can't summon.")
                
        elif action == "end":
            mph = False
        
        else:
            print("Sorry, what was that?")


def battlephase():
    bph = True#same as ebattlephase
    print(f"Enemy-{monsterzone2}")
    print(f"You-{monsterzone1}")
    print("Battle Phase")
    while bph == True:
        action = input("What will you do?(battle or end.)  ")
        if action == "battle":
            atk1()#see atk1
            
        elif action == "end":
            newdef = True
            
            while newdef == True:
                newatk = int(input("What cards are in attack position?(write 7 if none)  "))
                #because doing it automatically is 10 headaches in one.
                if newatk > len(monsterzone1):
                    newdef = False
                    
                else:
                    monsterzone1[newatk][4] = 0
                    alldone = input("Any others?(y/n)  ")
                    #changes list element based on input
                    if alldone == "N" or alldone == "n":
                        newdef = False
                        
                    elif alldone == "y" or alldone == "Y":
                        newdef = True
                        
                    else:
                        print("What was that again?  ")
                        
            bph = False
        else:
            print("Sorry, what was that?")
    

def main2phase():
    mph = True
    #literally the same as main!phase
    print("This is your hand-", hand1)
    print("This is your field-", monsterzone1)
    print("This is the enemies field-", monsterzone2)
    print(f"Your life points {lp1} and opponents life points {lp2}")

    while mph == True:
        action = input("What will you do?(inspect, summon, change position(cs), or end)  ")
        if action == "inspect":
            print("Your field-", monsterzone1)
            print("Opponents field-", monsterzone2)
            
        elif action == "cs":
            if len(monsterzone1) == 0:
                print("Nothing to defend.")
                
            else:
                varsol = int(input("What monster changes position?  "))
                varsol2 = input("Defend or attack position?  ")
                defend1(varsol, varsol2)
            
        elif action == "summon":
            
            if summoncounter == 0:
                normalsummon1()
                
            else:
                print("Can't summon.")
                
        elif action == "end":
            mph = False
        
        else:
            print("Sorry, what was that again?")


def endphase():
    print("Next player's turn.")
    dotheglobalsummoncounter()
    print('''
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    
    ''')

def edrawphase():
    print("Draw a card.")
    hand2.append(deck2.pop(0))
#e-turns are the same as the ones before but reversed
def estandbyphase():
    print("Wait")

def emain1phase():
    mph = True
    
    print("This is your hand-", hand2)
    print("This is your field-", monsterzone2)
    print("This is the enemies field-", monsterzone1)
    print(f"Your life points {lp2} and opponents life points {lp1}")

    while mph == True:
        action = input("What will you do?(inspect, summon, change position(cs), or end)  ")
        if action == "inspect":
            print("Your field-", monsterzone2)
            print("Opponents field-", monsterzone1)
            
        elif action == "cs":
            if len(monsterzone2) == 0:
                print("Nothing to defend.")
                
            else:
                varsol = int(input("What monster changes position?  "))
                varsol2 = input("Defend or attack position?  ")
                defend2(varsol, varsol2)
            
        elif action == "summon":
            
            if summoncounter == 0:
                normalsummon2()
                
            else:
                print("Can't summon.")
                
        elif action == "end":
            mph = False
        
        else:
            print("Sorry, what was that again?")

def ebattlephase():
    bph = True
    print("Battle Phase")
    print(f"Enemy-{monsterzone1}")
    print(f"You-{monsterzone2}")
    while bph == True:
        action = input("What will you do?(battle or end)  ")
        
        if action == "battle":
            atk2()
            
        elif action == "end":
            newdef = True
            
            while newdef == True:
                newatk = int(input("What cards are in attack position?(Write 7 if none.)  "))
                
                if newatk > len(monsterzone2):
                    newdef = False
                    
                else:
                    monsterzone2[newatk][4] = 0
                    alldone = input("Any others?(y/n)  ")
                    
                    if alldone == "N" or alldone == "n":
                        newdef = False
                        
                    elif alldone == "y" or alldone == "Y":
                        newdef = True
                        
                    else:
                        print("What was that again?  ")
            bph = False
            
        else:
            print("Sorry, what was that again?")

def emain2phase():
    mph = True
    
    print("This is your hand-", hand2)
    print("This is your field-", monsterzone2)
    print("This is the enemies field-", monsterzone1)
    print(f"Your life points {lp2} and opponents life points {lp1}")

    while mph == True:
        action = input("What will you do?(inspect, summon, change position(cs), or end)  ")
        
        if action == "inspect":
            print("Your field-", monsterzone2)
            print("Opponents field-", monsterzone1)
            
        elif action == "cs":
            if len(monsterzone2) == 0:
                print("Nothing to defend.")
                
            else:
                varsol = int(input("What monster changes position?  "))
                varsol2 = input("Defend or attack position?  ")
                defend2(varsol, varsol2)
            
        elif action == "summon":
            
            if summoncounter == 0:
                normalsummon2()
                
            else:
                print("Can't summon.")
                
        elif action == "end":
            mph = False
        
        else:
            print("Sorry, what was that again?")

def eendphase():
    print("Next player's turn.")
    dotheglobalsummoncounter()
    print('''
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    
    ''')

def normalsummon1():
    global summoncounter
    summoncounter += 1
    prompt = int(input("What card to summon?  "))
    ifset = input("Would you like to set?(y/n)  ")
    #adds list element from hand1 to monsterzone1
    if ifset == "Y" or ifset == "y":
        hand1[prompt][4] = 1
        monsterzone1.append(hand1.pop(prompt))
            #asks if you want list element 4 to be 1 or 0
    elif ifset == "N" or ifset == "n":
        hand1[prompt][4] = 0
        monsterzone1.append(hand1.pop(prompt))
        
    else:
        hand1[prompt][4] = 0
        monsterzone1.append(hand1.pop(prompt))
            
def normalsummon2():
    global summoncounter
    summoncounter += 1#same as normalsummon1()
    prompt = int(input("What card to summon?  "))
    ifset = input("Would you like to set?(y/n)  ")
    if ifset == "Y" or ifset == "y":
        hand2[prompt][4] = 1
        monsterzone2.append(hand2.pop(prompt))
            
    elif ifset == "N" or ifset == "n":
        hand2[prompt][4] = 0
        monsterzone2.append(hand2.pop(prompt))
            
    else:
        hand2[prompt][4] = 0
        monsterzone2.append(hand2.pop(prompt))
        
    
    
def spell():
    #remnants of a bygone era
    pass

        
   
def atk1():#nested list problems.nvm. player1 battling
    atking = int(input("What monster will attack?  "))#get integers
    defing = int(input("What monster will be attacked?  "))
    global lp1#so that we can change them
    global lp2
    
    if monsterzone1[atking][4] == 0:
        monsterzone1[atking][4] = 1#my idea for how to make sure it 
        #only attacks once
        
        if len(monsterzone2) == 0:
            lp2 -= monsterzone1[atking][0]#took me too long to remember -=
            return lp2#attacks directly, damage goes to lp
            print("You attacked directly.")
            print("Your life points- {lp1}, opponents life points- {lp2}")
            
        elif monsterzone2[defing][4] == 0:
            #if defending monster is in attack pos
            if monsterzone1[atking][0] > monsterzone2[defing][0]:
                lp2 -= ( monsterzone1[atking][0] - monsterzone2[defing][0] )#pulls from first list element
                gy2.append(monsterzone2.pop(defing))
                return lp2
                print("You beat the monster!")
                print(f"Your life points- {lp1}, opponent life points- {lp2}")
                print(f"Your field- {monsterzone1}")
                print(f"Opponent field- {monsterzone2}")
                
            elif monsterzone1[atking][0] < monsterzone2[defing][0]:
                lp1 -= ( monsterzone2[defing][0] - monsterzone1[atking][0] )
                gy1.append(monsterzone1.pop(atking))
                return lp1#same as earlier, but opponents monster has higher attack
                print("The monster beat you!")
                print(f"Your life points- {lp1}, opponent life points- {lp2}")
                print(f"Your field- {monsterzone1}")
                print(f"Opponent field- {monsterzone2}")
                
            elif monsterzone1[atking][0] == monsterzone2[defing][0]:
                gy1.append(monsterzone1.pop(atking))
                gy2.append(monsterzone2.pop(defing))
                print("You beat each other.")#if monster has equal stats
                print(f"Your life points- {lp1}, opponent life points- {lp2}")
                print(f"Your field- {monsterzone1}")
                print(f"Opponent field- {monsterzone2}")
                
        elif monsterzone2[defing][4] == 1:
            #if the monster is defending
            if monsterzone1[atking][0] > monsterzone2[defing][1]:
                gy2.append(monsterzone2.pop(defing))
                print("You beat the monster")#if monster defense is lower
                print(f"Your life points- {lp1}, opponent life points- {lp2}")
                print(f"Your field- {monsterzone1}")
                print(f"Opponent field- {monsterzone2}")
            
            elif monsterzone1[atking][0] < monsterzone2[defing][1]:
                lp1 -= ( monsterzone2[defing][1] - monsterzone1[atking][0] )
                gy1.append(monsterzone1.pop(defing))
                return lp1
                print("The monster beat you.")#if monster defense is higher
                print(f"Your life points- {lp1}, opponent life points- {lp2}")
                print(f"Your field- {monsterzone1}")
                print(f"Opponent field- {monsterzone2}")
            
            elif monsterzone1[atking][0] == monsterzone2[defing][1]:
                print("Nothing happened.")#if equal, but defending
            
                
    elif monsterzone1[atking][4] == 1:
        print("Can't attack")#if attacking is defending
        pass
    else:
        pass
    
def defend1(mons, mons2):
    if mons2 == 'defend':#for change position
        monsterzone1[mons][4] = 1
    #changes 4 list element 
    elif mons2 == 'attack':
        monsterzone1[mons][4] = 0
        
    else:
        print("Sorry, try again.")
    
def defend2(mons, mons2):
    if mons2 == 'defend':
        monsterzone2[mons][4] = 1
        #same as defend1
    elif mons2 == 'attack':
        monsterzone2[mons][4] = 0
        
    else:
        print("Sorry, try again.")
    
def atk2():#what happens if player 2 battles. 
    global lp1#same as atk1 with different placements
    global lp2
    atking = int(input("Who's attacking?  "))
    defing = int(input("Who are you attacking?  "))
    
    if monsterzone2[atking][4] == 0:
        monsterzone2[atking][4] = 1
        #^changes monster to def pos so it can't attack twice
        if len(monsterzone1) == 0:
            print("Attacked directly")
            lp1 -= monsterzone2[atking][0]
            return lp1
            print("Your lifepoints- {lp2} opponent lifepoints- {lp1}")
            
        elif monsterzone1[defing][4] == 0:
            
            if monsterzone2[atking][0] > monsterzone1[defing][0]:
                lp1 -= ( monsterzone2[atking][0] - monsterzone1[defing][0] )
                gy1.append(monsterzone1.pop(defing))
                print("You beat the monster!")
                print(f"Your life points- {lp2}, opponent life points- {lp1}")
                return lp1#put lp subtract ABOVE gy append, because without you run out of list elements
                print(f"Your field- {monsterzone2}")
                print(f"Opponent field- {monsterzone1}")
                
            elif monsterzone2[atking][0] < monsterzone1[defing][0]:
                lp2 -= ( monsterzone1[defing][0] - monsterzone2[atking][0] )
                gy2.append(monsterzone2.pop(atking))
                return lp2
                print("The monster beat you!")
                print(f"Your life points- {lp2}, opponent life points- {lp1}")
                print(f"Your field- {monsterzone2}")
                print(f"Opponent field- {monsterzone1}")
                
            elif monsterzone2[atking][0] == monsterzone1[defing][0]:
                gy2.append(monsterzone2.pop(atking))
                gy1.append(monsterzone1.pop(defing))
                print("You beat each other?")
                print(f"Your field- {monsterzone2}")
                print(f"Opponent field- {monsterzone1}")
                
        elif monsterzone1[defing][4] == 1:
            
            if monsterzone2[atking][0] > monsterzone1[defing][1]:
                gy1.append(monsterzone1.pop(defing))
                print("You beat the monster!")
                print(f"Your field- {monsterzone2}")
                print(f"Opponent field- {monsterzone1}")
            
            elif monsterzone2[atking][0] < monsterzone1[defing][1]:
                lp2 -= ( monsterzone1[defing][1] - monsterzone2[atking][0] )
                gy2.append(monsterzone2.pop(defing))
                return lp2
                print("The monster beat you!")
                print(f"Your life points- {lp2}, opponent life points- {lp1}")
                print(f"Your field- {monsterzone2}")
                print(f"Opponent field- {monsterzone1}")
            
            elif monsterzone1[atking][0] == monsterzone1[defing][1]:
                print("Nothing happened.")
            
    elif monsterzone2[atking][4] == 1:
        print("Can't attack")
        pass#if monster tries to attack in def pos


#code begins-- main start
lp1 = 2000#lifepoints for player 1
lp2 = 2000#life points for player 2

#actual start
print('''
Welcome to 5 card YuGiOh!
You each start with 3 cards in your hand
There are no monsters with more than 4 levels
There are no monster effects
To find stats of a face up card, type "inspect" as an action
Don't cheat by looking at opponents cards
Type numbers instead of names of cards, starting at 0
No battling on the first turn
Cards = [attack, defense, level, name, if defending]
If you don't know the rules of YuGiOh...
I don't know, google it or something. 

Have fun! (Hopefully)
''')

random.shuffle(deck1)#literally the only time random is used. 
random.shuffle(deck2)
hand1.append(deck1.pop(0))#draw your hand
hand1.append(deck1.pop(0))
hand2.append(deck2.pop(0))
hand2.append(deck2.pop(0))
dotheglobalsummoncounter()#idk why this is here. just let it be. respect it. 

#play game forever

while True:
    print(len(deck1))
    print(len(deck2))
    drawphase()
    standbyphase()
    main1phase()
    battlephase()
    main2phase()
    endphase()#i mean... just give computer to player 2. That's assuming you have friends. 
    if lp1 <= 0 or lp2 <= 0:#only checks after each turn
        break#deal with it
    edrawphase()
    estandbyphase()
    emain1phase()
    ebattlephase()
    emain2phase()
    eendphase()
    if lp1 <= 0 or lp2 <= 0:
        break#checks if lp is less than 0, breaks and moves to if statments

if lp1 <= 0:#win condition
    print("Congratulations Player 2, You Win.")
    print("Your opponent was Obliterated.")
    
elif lp2 <= 0:
    print("Congratulations Player 1, You Win.")
    print("Your opponent was Obliterated.")
    
