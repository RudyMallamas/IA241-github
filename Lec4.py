'''
lec4
disct and tuple
'''
my_tuple = 'a', 'b', 'c', 'd', 'e'
print(type(my_tuple))

print(my_tuple[0:2])

#can no longer change the values of a tuple after its been made

'''
my_tuple[0] = 'f'
print(my_tuple)
values cannot be changed
'''

#unique and can be changed
my_car = { 'Color':'Velocity Blue', 
'Maker':'Ford', 
'Model':'Mustang', 
'Year':2020}
#Dictionary
print(my_car['Year'])
print(my_car.items())
print(my_car.keys())
print(my_car.values())
print(my_car.get('Model'))
my_car['VIN'] = 123456789
print(my_car)
my_car['Year'] = 2024
my_car['VIN'] = 1
print(my_car)
print(  len(my_car))
print('Velocity Blue' in my_car.values())