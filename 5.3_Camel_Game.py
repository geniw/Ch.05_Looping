'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
print("Hello and welcome to Geni's Camel Game!") # intro/instructions
print("You will have 5 main options, and a 6th one to quit that you'll see below.")
print("The goal is to travel 150 miles without being caught by natives, dying of thirst, or your camel dying.")
print("You have 5 times you're able to drink from your canteen, so use it wisely.")
print("You also have a 1/20 chance to find an oasis where your thirst and camel's rest will be restored.")
print("Lastly if your thirst is getting low drink from your canteen, and if your camel is tired you might want to stop for the night.")
print("Now let's begin!")
Done = False
thirst = 0
drinks = 5
miles = 0
camel_tiredness = 0
natives = 20 # miles behind the player
oasis = 0
import random
while not Done:
    print("A. Drink from your canteen.") # choices
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    user_input = input("Type in what you'd like to do. ") # asking user input
    if user_input.lower() == "a" or user_input.lower() == "a. drink from your canteen" or user_input.lower() == "drink from your canteen" or user_input.lower() == "a drink from your canteen":
        if drinks > 0: # checking if they have drinks in canteen
            thirst = 0 # resetting thirst to 0 and subtracting amount of drinks in canteen
            drinks -= 1
            print("You now have", drinks, "drinks left in your canteen.")
        else:
            print("Error: You have no drinks left in your canteen!") #aren't able to drink
    elif user_input.lower() == "b" or user_input.lower() == "b. ahead moderate speed" or user_input.lower() == "ahead moderate speed" or user_input.lower() == "b ahead moderate speed":
        miles_traveled = 0 # resetting variables
        natives_traveled = 0
        miles_traveled = random.randint(5, 12) # picking random number of miles traveled
        miles += miles_traveled # adding the random number to the total
        print("You traveled",miles_traveled,"miles.") # stating how many miles they traveled that round
        print("You have a total of",miles,"miles traveled.") # stating total
        thirst += 1 # adding thirst and tiredness
        camel_tiredness += 1
        natives_traveled = random.randint(-10, 15) # same thing as above but with natives traveled
        natives -= natives_traveled
    elif user_input.lower() == "c" or user_input.lower() == "c. ahead full speed" or user_input.lower() == "ahead full speed" or user_input.lower() == "c ahead full speed":
        miles_traveled = 0 # same as what I did for option b
        natives_traveled = 0
        tired = 0
        miles_traveled = random.randint(10, 20) # increased random values
        miles += miles_traveled
        print("You traveled", miles_traveled, "miles.")
        print("You have a total of", miles, "miles traveled.")
        thirst += 1
        tired = random.randint(1, 3) # picking random number of camel tiredness
        camel_tiredness += tired # adding random number to actual variable
        natives_traveled = random.randint(-15, 12)
        natives -= natives_traveled
    elif user_input.lower() == "d" or user_input.lower() == "d. stop for the night" or user_input.lower() == "stop for the night" or user_input.lower() == "d stop for the night":
        natives_traveled = 0
        camel_tiredness = 0 # resetting camel tiredness
        print("Your camel is happy!")
        natives_traveled = random.randint(5, 15)
        natives -= natives_traveled
    elif user_input.lower() == "e" or user_input.lower() == "e. status check" or user_input.lower() == "status check" or user_input.lower() == "e status check":
        print("Miles traveled:",miles)
        print("Drinks in canteen:",drinks)
        print("The natives are",natives,"miles behind you.")
    elif user_input.lower() == "q" or user_input.lower() == "q. quit" or user_input.lower() == "quit" or user_input.lower() == "q quit":
        Done = True
    else:
        print("Not a choice!")
    if not Done and thirst == 4 or thirst == 5: # if the thirst is 4 or 5 they get the below message
        print("You're thirsty!")
    elif thirst == 6: # if thirst is 6 they die and the game ends
        print("You died of thirst!")
        Done = True
    if not Done and camel_tiredness >= 5 and camel_tiredness < 8: # if camel tiredness is greater than or equal to 5 but less than 8 they get below message
        print("Your camel is tired!")
    elif camel_tiredness >= 8: # if camel tiredness is greater than or equal to 8 then the camel dies and the game ends
        print("Your camel died!")
        Done = True
    if not Done and natives <= 0:
        print("The natives caught you!") # if natives catch up to player than the game ends
        Done = True
    elif natives < 15: # if the natives are less than 15 miles behind the player they get the below message
        print("The natives are close!")
    if not Done and miles >= 150: # if the player travels a total of 100 miles they win and game ends
        print("You won!")
        Done = True
    if not Done and not user_input.lower() == "e" or user_input.lower() == "e. status check" or user_input.lower() == "status check" or user_input.lower() == "e status check":
        oasis = random.randint(1,20) # picks a random number 1-20
    if oasis == 20: # if the number is 20 then they find an oasis and it resets thirst and camel tiredness
        print("You found an oasis!")
        thirst = 0
        camel_tiredness = 0
        oasis = 0
    else:
        oasis = 0 # resetting variable