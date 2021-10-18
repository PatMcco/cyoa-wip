#Choose your own adventure
#Author Pat McCormick
#Scenario Wal-Mert

import time

def main():
#if anxiety reaches 5, you lose
#if patience reaches 0, you lose
#if health reaches 0, you lose
    anxiety = 1
    patience = 5
    health = 10

    winScenario = print("Congratulations, you survived another trip to Wal-Mert\nwith your sanity intact. It could've been a lot worse.")
    anxietyScenario = print("You suddenly feel flush and shakey, your vision narrows and you drop everything while making your way out of the store, you tell yourself you should've stayed home.")
    patienceScenario = print("You've lost your patience. \nYou kick the next cart that's remotely close to your \nimmediate path out of here and tell multiple strangers to get F***ed as you \nstorm out flipping off the old Greeter lady.")
    healthScenario = print("That was the last straw, you've managed to contract something\ndoctors don't have a name for and the side effects of it include\nhaving zero self-awareness, lack of compassion for other human beings\n and consistently seeking out the nearest manager.")

        

    print("Welcome to the Anxious Person Wal-Mert Shopping Simulator\n")
    #time.sleep(3)
    print("Answer Y for Yes or N for No for each scenario.\n")
    #time.sleep(1)
    print("You see a van with reverse lights on close to the main entrance.\n")
    #time.sleep(1)

    check1 = input("Do you pull up close and wait for them to leave?: ")
    
    if str.lower(check1) == "y":
        print("The person sits there for a solid 30 seconds without moving\n")
        time.sleep(1.5)
        print("---Your anxiety level escalates slightly...\n")
        anxiety = anxiety + 1
    elif str(check1) == "n":
        print("You decide not to wait and move on to a further spot.\n")

    #time.sleep(1)
    print("You park your car and head into the store, somebody is blocking the entrance with\na cart and they're on their phone looking the other way.\n")
    #time.sleep(3)
    check2 = input("You have 3 choices: \n 1. Squeeze between the cart and door and ignore them. \n 2. Stand there until they realise they're blocking the way. \n 3. Say EXCUSE ME YOU'RE BLOCKING THE DOOR\n Choose 1, 2, or 3:\n ")
    if check2 == str(1):
        print("They didn't even notice you and now there's a black stain from the cart on your pants\n---Your anxiety increases mildly and you're already regretting this trip.\n")
        anxiety = anxiety + 2
    elif check2 == str(2):
        print("After a solid 15 seconds they see you in the corner of their eye and move\nthe cart about a foot out of the way, not bothered at all \n\n---Your patience dwindles slightly.\n")
        patience = patience - 1
    elif check2 == str(3):
        print("The person is visibly shocked and drops their phone, the gap opens and they don't realise what\nhappened until you're already well into the store.\n")
#level check
    if anxiety >= 5:
        print(anxietyScenario)
    elif patience == 0:
        print(patienceScenario)
    elif health == 0:
        print(healthScenario)

    print("You make your way towards your first item.\n")
    check3 = input("You get close to the aisle you need to go down\nbut someone is currently blocking it with\ntheir entire family and doesn't look to be moving soon.\nYou can either cut through the next aisle with the arrows\nfacing the wrong way or go all the way around.\nDo you cut through? ")
    if str.lower(check3) == "y":
        print("As you cut through the aisle, a rather large woman looks at you.\nShe proceeds to turn her cart and gaze towards\n the chocolate bars and shows no sign of moving.")
        time.sleep(2)
        print("You can say Excuse me I just need to get by OR \ngo full tilt and throw your shoulder into her in an attempt to penetrate the wall of self rightousness")
        check3a = input("Choose 1 or 2: ")
        if str(check3a) == 1:
            print("Your Excuse Me wasn't very effective.\nYou attempt to squeeze past and as you are about to pass in front of her\n she sneezes aggressively. You sprint out of the aisle.\n")
            anxiety = anxiety + 1
            patience = patience - 2
            health = health - 3
            print("---Your health, anxiety and patience just took a severe hit.")
        elif str(check3a) == 2:
            print("You throw all of your weight into a head down shoulder tackle just as\nshe moves to grab a Bag of Halloween Candy and you go bouncing off the opposing aisle.\nYou make it through but not cleanly.")
            patience = patience - 1
            health = health - 2
    else: print("You take the long way around, through some coughing NPCs\nand some tempting impulse buys you arrive at your first item.")
    health = health - 1

    #level check
    if anxiety >= 5:
        print(anxietyScenario)
    elif patience == 0:
        print(patienceScenario)
    elif health == 0:
        print(healthScenario)
    
    print("Your next item is just across the main racetrack. There are\n 3 other people in this aisle in a zig-zag pattern all with carts.")
    check4 = input("You can get the item quicker by leaving your cart where it is,\nyou'll be quick afterall. Do you leave your cart?: ")


        


main()


#   if anxiety == 0:
#       print(anxietyScenario)
#   elif patience == 0:
#       print(patienceScenario)
#    elif health == 0:
#       print(healthScenario)