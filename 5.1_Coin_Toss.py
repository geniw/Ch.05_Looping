'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
heads = 0
tails = 0
import random
for i in range(50):
      my_number = random.randint(0, 1)
      if my_number == 0:
          heads+=1
          print('heads')
      else:
          tails+=1
          print('tails')
print('Total number of heads:', heads)
print('Total number of tails:', tails)











