#Loops

#For loop
# fruits = ["Apple", "Oranges", "Mangoes"]
# for fruit in fruits: #loops hrough the list and gets each as a single fruit with fruit as the variable name for each
#     print(fruit) #prints each fruit in separe lines(single fruit) as per the list

# students_heights = input("Enter student heights separated by space.\n").split()
# sum_of_heights = 0
# for height in students_heights:
#     sum_of_heights += int(height)
# number_of_students = 0    
# for students in students_heights:
#     number_of_students += 1
# averange_height = sum_of_heights / number_of_students
# print(averange_height)

#alternatively
# students_heights = input("Enter student heights separated by space.\n").split()
# sum_of_height = sum(sum_of_heights)
# no_of_students = len(students_heights)
# averange = sum_of_height / no_of_students
# print(averange)

#max
# scores = input("enter scores \n").split()
# heighest_score = 0
# for score in scores:
#     score = int(score)
#     if score > heighest_score:
#         heighest_score = score
# print(f'The highest score is {heighest_score}')

#Range function        
# for numbers in range(1, 11, 3): #NB The third digit specifies the jumps(skip) in a range
#     print (numbers)

# total = 0    
# for number in range(2, 101, 2): #NB The third digit specifies the jumps(skip) in a range
#     total += number
# print(total)

# total2 = 0    
# for number2 in range(1, 101): #NB The third digit specifies the jumps(skip) in a range
#     if number2 % 2 == 0:
#         total2 += number2    
# print(total2)

#Fizz Buzz
# for value in range (1, 101):
#     if (value % 3 == 0) and (value % 5 == 0):  
#         print("FIZZ BUZZ")    
#     elif value % 3 == 0:
#         print("FIZZ")
#     elif value % 5 == 0:
#         print("BUZZ")
#     else:
#         print(value)

#Password generator
import random
letters = ['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v',
'w', 'x', 'y', 'z', 'A','B','C','D', 'E', 'F', 'G', 'H', 
'I', 'J', 'k', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  
symbols = ['!', '#', '@', '%', '&', '*', '+', '^', '/']

print("Welcome to Strong Password Generator")
nr_letters = int(input("Enter the number of letters you want included\n"))
nr_numbers = int(input("Enter the number of number values you want included\n"))
nr_symbols = int(input("Enter the number of symbols ypu want included\n"))

password_List = []
for letter in range(1, nr_letters + 1):
    password_List += random.choice(letters)
for number in range(1, nr_numbers + 1):
    password_List += random.choice(numbers)
for symbol in range(1, nr_symbols + 1):
    password_List += random.choice(symbols)
random.shuffle(password_List)

password = ''
for char in password_List:
    password += char
print(f'Congratulations! Your new password is {password}')     