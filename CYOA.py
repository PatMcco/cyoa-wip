#Choose your own adventure
#Author Pat McCormick
#Scenario Wal-Mert

import time
import sys
def main():
#if anxiety reaches 5, you lose
#if patience reaches 0, you lose
#if health reaches 0, you lose
    anxiety = 1
    patience = 5
    health = 10
####Scenario Endings####
    winScenario = "Congratulations, you survived another trip to Wal-Mert\nwith your sanity intact. It could've been a lot worse. Time to go home...\n\n"
    anxietyScenario = "You suddenly feel flush and shakey, your vision narrows and you drop everything while making your way out of the store.\nYou tell yourself you should've stayed home\n Unfortunate but some days are just not great no matter what you do. \n\nAnxiety wins again."
    patienceScenario = "You've lost your patience. \nYou kick the next cart that's remotely close to your immediate path out of here.\nYou tell multiple strangers to get F***ed as you storm out.\nFlipping off the old Greeter lady as you do.\n\nWon't be showing your face here for awhile..."
    healthScenario = "That was the last straw, you've managed to contract something doctors don't have a name for.\nThe side effects of it include:\nHaving zero self-awareness\nlack of compassion for other human beings\nConsistently blocking aisles or laneways whilst going into a sort of comatose state.\n\nWal-Mert claims another...."
    karenScenario = "You feel your hair change shape. Suddenly everybody looks like they're a criminal who wants to hurt you.\nYou can only ask for a manager, complain, and threaten to call the police.\n\nYou've become a Karen. Sad..."

        
####Introduction####
    print("\nWelcome to a regular trip to Wal-Mert.\n")
    time.sleep(2)
    print("\nAnswer Y for Yes or N for No for each scenario unless otherwise specified.\n")
    time.sleep(2)
    print("The goal is to retrieve your 5 items and get out in one piece.\n\n")
    time.sleep(2)
    print("You're just pulling in the parking lot now...\n\n")
    time.sleep(2)
    print("You see a van with reverse lights on close to the main entrance.\n")
    time.sleep(2)

    check1 = input("Do you pull up close and wait for them to leave?: \n\n")
    
    if str.lower(check1) == "y":
        print("\nThe person sits there for a solid 30 seconds without moving\n")
        time.sleep(2)
        print("\n---Your anxiety level escalates slightly...\n")
        anxiety = anxiety + 1
    elif str(check1) == "n":
        print("\nYou decide not to wait and move on to a further spot.\n")
        time.sleep(2)

    time.sleep(2)
    print("\nYou park your car and head into the store.\n\n")
    time.sleep(2)
    print("Somebody is blocking the entrance witha cart.\n\n")
    time.sleep(2)
    print("They're on their phone looking the other way.\n")
    time.sleep(2)
    check2 = input("\nYou have 3 choices: \n 1. Squeeze between the cart and door and ignore them. \n\n 2. Stand there until they realise they're blocking the way. \n\n 3. Say EXCUSE ME YOU'RE BLOCKING THE DOOR\n\n Choose 1, 2, or 3:\n ")
    if check2 == str(1):
        time.sleep(2)
        print("\nThey didn't even notice you and now there's a black stain from the cart on your pants\n\n---Your anxiety increases mildly and you're already regretting this trip.\n")
        anxiety = anxiety + 2
    elif check2 == str(2):
        time.sleep(2)
        print("\nAfter a solid 15 seconds they see you in the corner of their eye and move\nthe cart about a foot out of the way, not bothered at all \n\n---Your patience dwindles slightly.\n")
        patience = patience - 1
    elif check2 == str(2):
        time.sleep(2)
        print("\nThe person is visibly shocked and drops their phone, the gap opens and they don't realise what\nhappened until you're already well into the store.\n")

       ########level check#########
    if anxiety >= 5:
        print(anxietyScenario)
        time.sleep(10)
        sys.exit()
    elif patience == 0:
        print(patienceScenario)
        time.sleep(10)
        sys.exit()
    elif health == 0:
        print(healthScenario)
        time.sleep(10)
        sys.exit()
    ####Part 1 Item 1####
    time.sleep(2)
    print("\nYou make your way towards your first item.\n")
    time.sleep(2)
    print("\nYou get close to the aisle you need to go down.\n")
    time.sleep(2)
    print("\nSomeone is currently blocking it with their entire frikkin family and doesn't look to be moving soon.\n")
    time.sleep(2)
    check3 = input("\nYou can either cut through the next aisle with the arrows facing the wrong way OR\ngo all the way around.\n\nDo you cut through? \n")
    if str.lower(check3) == "y":
        time.sleep(2)
        print("\nAs you cut through the aisle, a rather large woman looks at you.\nShe proceeds to turn her cart and gaze towards\nthe chocolate bars and shows no sign of moving.\n")
        time.sleep(2)
        print("\nYou can say Excuse me I just need to get by OR \ngo full tilt and throw your shoulder into her in an attempt to penetrate the wall of self rightousness\n")
        check3a = input("\nChoose 1 or 2: \n")
        if check3a == str(1):
            print("\nYour Excuse Me wasn't very effective.\n\nYou attempt to squeeze past and as you are about to pass in front of her she sneezes aggressively.\n\nYou sprint out of the aisle.\n")
            anxiety = anxiety + 1
            patience = patience - 2
            health = health - 3
            time.sleep(3)
            print("\n---Your health, anxiety and patience just took a severe hit.\n")
        elif check3a == str(2):
            print("\nYou throw all of your weight into a head down shoulder tackle just as\nshe moves to grab a Bag of Halloween Candy and you go bouncing off the opposing aisle.\nYou make it through but not cleanly.\n")
            patience = patience - 1
            health = health - 2
            time.sleep(3)
            print("\n---Your patience is wearing thin and you suddenly feel off...\n")
    elif str.lower(check3) == "n":
        time.sleep(2)
        print("\nYou take the long way around through some coughing NPCs and pass some tempting impulse buys.\n\nYou manage to you arrive at your first item and grab it.\n")
        health = health - 1


       ########level check#########
    if anxiety >= 5:
        print(anxietyScenario)
        time.sleep(10)
        sys.exit()
    elif patience == 0:
        print(patienceScenario)
        time.sleep(10)
        sys.exit()
    elif health == 0:
        print(healthScenario)
        time.sleep(10)
        sys.exit()

####PArt 2 Item 2####
    time.sleep(3)
    print("\nYour next item is just across the main racetrack. There are\n 3 other people in this aisle in a zig-zag pattern all with carts.\n")
    time.sleep(2)
    check4 = input("\nYou can get the item quicker by leaving your cart where it is,\nyou'll be quick afterall. Do you leave your cart?: \n")
    time.sleep(2)
    if str.lower(check4) == "y":
        time.sleep(1)
        print("\nYou make your way through the obstacle of old ladies complaining they've never seen bacon so expensive.\nAs you're coming to the end of the aisle you don't look both ways and get bumped by a small child.\nHe looks at you and then runs away.\nYou look down and see a wet spot where his face collided with your leg.\n You sigh, grab your item and make your way back to your cart.\n")
        health = health - 1
    else:
        time.sleep(2)
        print("\nYou take your cart and take the long way around again.\n On your way you hit up a hand sanitizer station.\n---You feel less gross. You grab your second item.")
    health = health + 1

       ########level check#########
    if anxiety >= 5:
        print(anxietyScenario)
        time.sleep(10)
        sys.exit()
    elif patience == 0:
        print(patienceScenario)
        time.sleep(10)
        sys.exit()
    elif health == 0:
        print(healthScenario)
        time.sleep(10)
        sys.exit()

###Part 3 Item 3###
    time.sleep(3)
    print("\nYou now have 2 of 5 items. Your next closest item is in the footwear aisle.\nAs you make your way there you come across a wet floor sign.\nSeems somebody had a pretty bad accident.\n\n")
    time.sleep(2)
    print("You don't want to push your cart through the mess,\nbut going against the floor arrows is a crime punishable by public humiliation these days.\n\n")
    time.sleep(2)
    check5 = input("Do you say screw it and go around into the 'wrong way' aisle to avoid the mess?..\n\n" )
    if str.lower(check5) == "y":
        print("You maneuver the cart into the other lane, nobody seems to notice. Phew.\n\n")
        time.sleep(2)
    elif str.lower(check5) == "n":
        print("You decide to uphold the Law of Arrows.\nYour carts wheels and your shoes are now covered in a biological hazard.\n\n")
        time.sleep(2)
        print("You smell pretty rough right now and your shoes squeek with every step.\nDefinately shouldn't have done that.\n\n") 
        health = health - 3
        anxiety = anxiety + 1
        patience = patience - 1
        check5 == False
        time.sleep(2.2)

        #######level check#########
    if anxiety >= 5:
        print(anxietyScenario)
        time.sleep(10)
        sys.exit()
    elif patience == 0:
        print(patienceScenario)
        time.sleep(10)
        sys.exit()
    elif health == 0:
        print(healthScenario)
        time.sleep(10)
        sys.exit()

    print("You arrive at the footwear section, you aren't exactly sure where the item you need is.\n\n")
    time.sleep(2)
    check5  = input("You could ask someone for help or look yourself. Do you ask for help?\n\n")
    time.sleep(2)
    if str.lower(check5) == "y":
        print("You find an employee who shows you to the item.\nYou thank him as you place your 3rd item in your cart.\n\n")
        time.sleep(2)
        if check5 == False:
            print("The smell from the previous hazard is still lingering. Gross.\n\n")
        health = health - 1
    elif str.lower(check5) == "n":
        print("You were too embarassed to ask for help. You look around for 20 minutes before finding your item.\n\n")
        time.sleep(2)
        print("The smell is really getting to you and others are definately noticing. Gross\n\n")
        health = health - 2
        anxiety = anxiety + 1
        time.sleep(2.2)

        #######level check#########
    if anxiety >= 5:
        print(anxietyScenario)
        time.sleep(10)
        sys.exit()
    elif patience == 0:
        print(patienceScenario)
        time.sleep(10)
        sys.exit()
    elif health == 0:
        print(healthScenario)
        time.sleep(10)
        sys.exit()

####part 6 item 4####
    print("You've made it this far, 3 items in your cart and 2 to go. Not as easy as you thought huh.\n\n")
    time.sleep(2)
    print("Next up is something heavy but i'm sure you can manage. You make your way across the store.\n\n")
    time.sleep(2)
    print("You arrive in the section of your next item. Looks to be a top shelfer. Great...\n\n")
    time.sleep(2)
    check6 = input("You have 3 choices: \n\n1. Ask another employee to grab it for you.\n\n2. Attempt to grab it yourself, you can reach it but it's sketchy.\n\n3. Climb the shelving to get a better grip, it should hold right?\n\n")
    if check6 == str(1):
        print("You can't find an employee. Not a surprise. You do see one of those staircases on wheels though.\n\n")
        time.sleep(2)
        check6a = input("Do you attempt to do their job for them?\n\n")
        if str.lower(check6a) == "y":
            print("You roll the stairs over, unlatching the 'Employee Use Only' sign.\nClimbing the stairs and grabbing your item.\nYou notice the handle is broken and instead grab another one.\nCouldn't see that from below. Sheesh.\n\n")
            time.sleep(3)
            print("As you place the item in your cart an employee walks by and makes eye contact.\nThey keep walking without saying a word.\n\n")
            anxiety = anxiety - 1
        elif str.lower(check6a) == "n":
            print("You continue searching for an employee. Another customer sees you and offers to help.\nThey're much taller and easily grab the item.\n\n")
            time.sleep(3)
            print("The customer then starts ranting about how hard it is to find help when you need it.\nThey're face changes when they get closer to you.\nThey don't say anything but you know they noticed the smell from earlier. Oof\n\n")
            anxiety = anxiety + 1
            time.sleep(4)
    elif check6 == str(2):
        print("Big strong person huh... You grab the item and the handle breaks as you pull it off the top shelf.\n\n")
        time.sleep(2)
        print("You manage to catch it before it lands on your head but in the process pull a muscle.\n\n")
        time.sleep(2)
        print("You've acquired your 4th item, but take some damage in the process. What is this some sort of game?\n\n")
        health = health - 3
        patience = patience - 1
        time.sleep(2)
    elif check6 == str(3):
        print("You attempt to climb the shelving...\n\n")
        time.sleep(2)
        print("Your horrific smelling wet shoes slip on the edge of the rack and you fall.\n\n")
        time.sleep(2)
        print("An employee appears out of nowhere and grabs the item for you.\nAs they help you up they say:\n'We have you on camera doing this and driving through that spill earlier.\n If you complain to corporate you'll be barred from ever coming back.'\n\n")
        time.sleep(4)
        print("Now completely embarassed you quickly lean on your cart and hobble away quietly.\n\n")
        health=health - 1
        anxiety = anxiety + 1
        patience = patience - 1
        
    #level check
    if anxiety >= 5:
        print(anxietyScenario)
        time.sleep(10)
        sys.exit()
    elif patience == 0:
        print(patienceScenario)
        time.sleep(10)
        sys.exit()
    elif health == 0:
        print(healthScenario)
        time.sleep(10)
        sys.exit()
    
####PArt 7 Item 5####

    print("You've made it this far and your last item is on the way to the register.\n\n")
    time.sleep(3)
    print("You grab it as you reach the register line-up.\n It was an .88 cent chocolate bar, never leave without it.\n\n")
    time.sleep(2)
    print("You now have all 5 items, the last choice you have to make is using the self-checkout\n or going to the one open register.\n\n")
    time.sleep(2)
    check7 = input("Do you use the self-checkout?\n\n")
    if str.lower(check7) == "y":
        time.sleep(2)
        print("You roll your cart to the first open self-checkout.\n\n")
        time.sleep(2)
        print("As you begin unloading your items, you hear complaining\n\n")
        time.sleep(2)
        print("The complaining is about self-checkouts taking jobs away..of course.\n\n")
        time.sleep(2)
        print("The argument seems sound, unemployment rates ARE very high.\n\n")
        time.sleep(2)
        check7a = input("Do you chime in on the argument? It's a slipper slope...\n\n")
        if str.lower(check7a) == "y":
            print("'You're right and why am I paying full-price for doing all of the work?!?!\n\n")
            time.sleep(2)
            print("Your vision starts narrowing on a single point...\n\n")
            time.sleep(2)
            print("You feel the sudden urge to speak to someone in charge\n\n")
            time.sleep(2)
            print("You have forgotten completely why you came here\n\n")
            time.sleep(2)
            print("You try speaking but the only words that come out are...\n\n")
            time.sleep(3)
            print("LET ME SPEAK TO THE MANAGER\n\n")
            time.sleep(2)
            print(karenScenario)
        elif str.lower(check7a) == "n":
            print("Probably smart to keep your mouth shut.\n\nNothing good could come from arguing in Wal-Mert.")
            time.sleep(2)
            print("You finish the transaction and head out the door...\n\n")
            time.sleep(2)
            print(winScenario)
    elif str.lower(check7) == "n":
        time.sleep(2)
        print("You decide to wait for the one cash register open.\n\n")
        time.sleep(2)
        print("The Lady behind you has her mask down below her nose.\n\n")
        print("All of a sudden she sneezes, and you feel the back of your neck\nwas the main point of impact.\n\n")
        health = health - 2
        time.sleep(2)
            #level check
        if anxiety >= 5:
            print(anxietyScenario)
            time.sleep(10)
            sys.exit()
        elif patience == 0:
            print(patienceScenario)
            time.sleep(10)
            sys.exit()
        elif health == 0:
            print(healthScenario)
            time.sleep(10)
            sys.exit()
        print("You put your hood up incase a second barrage comes...\n\n")
        time.sleep(2)
        print("You get your groceries rung through, pay, and head out the door...\n\n")
        time.sleep(2)
        print("It was quite the trip but overall pretty normal for Wal-Mert. Maybe try BostBo next time...\n\n")
        time.sleep(2)
        print(winScenario)

        




main()


#   if anxiety == 0:
#       print(anxietyScenario)
#   elif patience == 0:
#       print(patienceScenario)
#    elif health == 0:
#       print(healthScenario)