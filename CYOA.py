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

    winScenario = ("Congratulations, you survived another trip to Wal-Mert\nwith your sanity intact. It could've been a lot worse.")
    anxietyScenario = ("You suddenly feel flush and shakey, your vision narrows and you drop everything while making your way out of the store, you tell yourself you should've stayed home.")
    patienceScenario = ("You've lost your patience. \nYou kick the next cart that's remotely close to your \nimmediate path out of here and tell multiple strangers to get F***ed as you \nstorm out flipping off the old Greeter lady.")
    healthScenario = ("That was the last straw, you've managed to contract something\ndoctors don't have a name for and the side effects of it include\nhaving zero self-awareness, lack of compassion for other human beings\n and consistently seeking out the nearest manager.")

        

    print("\nWelcome to the Anxious Person Wal-Mert Shopping Simulator\n")
    time.sleep(2)
    print("\nAnswer Y for Yes or N for No for each scenario.\n")
    time.sleep(1)
    print("\nYou see a van with reverse lights on close to the main entrance.\n")
    time.sleep(1)

    check1 = input("Do you pull up close and wait for them to leave?: ")
    
    if str.lower(check1) == "y":
        print("\nThe person sits there for a solid 30 seconds without moving\n")
        time.sleep(1.5)
        print("\n---Your anxiety level escalates slightly...\n")
        anxiety = anxiety + 1
    elif str(check1) == "n":
        print("\nYou decide not to wait and move on to a further spot.\n")

    time.sleep(1)
    print("\nYou park your car and head into the store.\nSomebody is blocking the entrance with\na cart and they're on their phone looking the other way.\n")
    time.sleep(1)
    check2 = input("\nYou have 3 choices: \n 1. Squeeze between the cart and door and ignore them. \n 2. Stand there until they realise they're blocking the way. \n 3. Say EXCUSE ME YOU'RE BLOCKING THE DOOR\n Choose 1, 2, or 3:\n ")
    if check2 == str(1):
        time.sleep(1)
        print("\nThey didn't even notice you and now there's a black stain from the cart on your pants\n---Your anxiety increases mildly and you're already regretting this trip.\n")
        anxiety = anxiety + 2
    elif check2 == str(2):
        time.sleep(1)
        print("\nAfter a solid 15 seconds they see you in the corner of their eye and move\nthe cart about a foot out of the way, not bothered at all \n\n---Your patience dwindles slightly.\n")
        patience = patience - 1
    elif check2 == str(3):
        time.sleep(1)
        print("\nThe person is visibly shocked and drops their phone, the gap opens and they don't realise what\nhappened until you're already well into the store.\n")

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
    
    time.sleep(1)
    print("\nYou make your way towards your first item.\n")
    check3 = input("You get close to the aisle you need to go down\nbut someone is currently blocking it with\ntheir entire family and doesn't look to be moving soon.\nYou can either cut through the next aisle with the arrows\nfacing the wrong way or go all the way around.\nDo you cut through? ")
    time.sleep(1)

    if str.lower(check3) == "y":
        time.sleep(1)
        print("\nAs you cut through the aisle, a rather large woman looks at you.\nShe proceeds to turn her cart and gaze towards\nthe chocolate bars and shows no sign of moving.")
        time.sleep(1)
        print("\nYou can say Excuse me I just need to get by OR \ngo full tilt and throw your shoulder into her in an attempt to penetrate the wall of self rightousness")
        check3a = input("\nChoose 1 or 2: ")
        if check3a == str(1):
            time.sleep(1)
            print("\nYour Excuse Me wasn't very effective.\nYou attempt to squeeze past and as you are about to pass in front of her she sneezes aggressively.\nYou sprint out of the aisle.\n")
            anxiety = anxiety + 1
            patience = patience - 2
            health = health - 3
            print("\n---Your health, anxiety and patience just took a severe hit.")
        elif check3a == str(2):
            time.sleep(1)
            print("\nYou throw all of your weight into a head down shoulder tackle just as\nshe moves to grab a Bag of Halloween Candy and you go bouncing off the opposing aisle.\nYou make it through but not cleanly.")
            patience = patience - 1
            health = health - 2
            print("\n---Your patience is wearing thin and you suddenly feel off...\n")
        elif check3a == str(3):
            time.sleep(1) 
            print("\nYou take the long way around,    through some coughing NPCs\nand some tempting impulse buys you arrive at your first item.")
            health = health - 1


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
    
    print("\nYour next item is just across the main racetrack. There are\n 3 other people in this aisle in a zig-zag pattern all with carts.")
    check4 = input("\nYou can get the item quicker by leaving your cart where it is,\nyou'll be quick afterall. Do you leave your cart?: ")
    time.sleep(1)
    if str.lower(check4) == "y":
        time.sleep(1)
        print("\nYou make your way through the obstacle of old ladies complaining they've never seen bacon so expensive.\nAs you're coming to the end of the aisle you don't look both ways and get bumped by a small child.\nHe looks at you and then runs away.\nYou look down and see a wet spot where his face collided with your leg.\n You sigh, grab your item and make your way back to your cart.")
        health = health - 1
    else:
        time.sleep(1)
        print("\nYou take your cart and take the long way around again.\n On your way you hit up a hand sanitizer station.\n---You feel less gross.")
    health = health + 1

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

    


        


main()


#   if anxiety == 0:
#       print(anxietyScenario)
#   elif patience == 0:
#       print(patienceScenario)
#    elif health == 0:
#       print(healthScenario)