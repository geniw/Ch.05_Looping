  #Sign your name: Geni W

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = int(input("Please enter a number: "))
    total+=x
print("The total is:", total)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
start, end = 2, 100
for num in range(start, end+1):
    if num%2 == 0:
        print(num, end=" ")


'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''

var = 10
while var > -1:
      print(' ', var)
      var = var - 1
print('BLAST OFF!')





'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
for i in range(1):
      my_number = random.randint(1, 10)
      print(my_number)



'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
total = 0
pos = 0
neg = 0
zero = 0
for i in range(7):
    x = int(input("Please enter a number: "))
    if x%2 == 0 and x>0:
        pos+=1
    elif x == 0:
        zero+=1
    else:
        neg+=1
    total += x
print("The total is:", total)
print('Total positive entries', pos)
print('Total negative entries', neg)
print('Total zero entries', zero)