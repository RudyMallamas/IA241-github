'''

lec 9
define class
'''

class car:
    maker = 'Toyota'
    
    #def report_maker(self):
        
     #   return self.maker
    def __init__(self, input_model):
        self.model = input_model
    def report(self):
        return self.maker, self.model

'''
my_car_instance = car('Supra')
print(my_car_instance.maker)
print(my_car_instance.model)

my_car_instance = car('AE86')
print(my_car_instance.maker)
print(my_car_instance.model)
'''

my_supra = car('Supra')
print(my_supra.maker)
print(my_supra.model)
print(my_supra.report())

my_supra.maker='Ford'

print(my_supra.report())




