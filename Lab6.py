'''
Rudy Mallamas
lab 5 
For statements
'''

#3.1
for i in range(6):
    if i != 3:
        print(i)
    
#3.2
result = 1
for i in range(1, 6): 
    result = result * i
    
print(result)

#3.3
num = 0
for i in range(1, 6):
    num += i

print(num)

#3.4*
product = 1
for i in range(3, 9):
    product *= i
    
print(product)

#3.5*
numerator = 1
for i in range(1, 8):
    numerator *= i

denominator = 1
for j in range(1, 3):
    denominator *= j

result = numerator / denominator
print(result)


#3.6
result = 0 

for word in 'This is my 6th string'.split():
    result = result + 1

print(result)

#3.7
my_tweet = {
"favorite_count":1138, 
"lang": "en", 
"coordinates": (-75, 40), 
"entities": {"hashtags": ["Preds", "Pens", "SingIntoSpring"]} 
}

count = 0 

for i in my_tweet["entities"]["hashtags"]:
    count = count +1
    
print(count)


    
    
