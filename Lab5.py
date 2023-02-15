'''
Rudy Mallamas
lab 5 
if statements
'''
#3.1
alien_color = 'red'

if alien_color == 'green':
    print('You got 5 points')
else:
    print('You got 10 points')
    
#3.2
favorite_fruits = ['apple', 'pineapple', 'cherry']

if favorite_fruits[0] == 'apple':
    print('you really like ' + favorite_fruits[0] + '!')
if favorite_fruits[1] == 'pineapple':
    print('you really like ' + favorite_fruits[1] + '!')
if favorite_fruits[2] == 'cherry':
    print('you really like ' +  favorite_fruits[2] + '!')
    
#3.3
age = 21

if age <= 10:
    print('This person is a kid.')
elif age < 20: 
    print('This person is a teenager.')
elif age < 65:
    print('This person is an adult.')
else:
    print('This person is an elder.')