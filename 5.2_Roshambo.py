'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
done = False
win = 0
loss = 0
import random
while not done:
    print('If you\'d like to quit enter y.')
    quit = input("Do you want to quit? ")
    if quit == "y":
            done = True
            print('Wins:', win)
            print('Losses:', loss)
    else:
        print('Enter 1 for rock, 2 for paper, or 3 for scissors.')
        choice = int(input("Please enter your choice: "))
        computer = random.randint(1, 3)
        if computer == 1:
            print('The computer chose: rock')
            if choice == 3:
                loss+=1
                print('Sorry, you lost this time.')
                continue
            elif choice == 2:
                win+=1
                print('Woohoo, you won!')
                continue
            else:
                print('Tie!')
                continue
        elif computer == 2:
            print('The computer chose: paper')
            if choice == 1:
                loss += 1
                print('Sorry, you lost this time.')
                continue
            elif choice == 3:
                win += 1
                print('Woohoo, you won!')
                continue
            else:
                print('Tie!')
                continue
        else:
            print('The computer chose: scissors')
            if choice == 2:
                loss += 1
                print('Sorry, you lost this time.')
                continue
            elif choice == 1:
                win += 1
                print('Woohoo, you won!')
                continue
            else:
                print('Tie!')
                continue











