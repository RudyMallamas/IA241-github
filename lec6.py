'''
Lec 6
for loop
range function
'''

for num in [1,2,3]:
    if num>1:
        print(num)
    
for word in 'this is lec6'.split():
    print(word)
    for c in word:
        print(c)

#range() function generates arithmatic progressions
#range(m) generates progression from 0 to m-1
for i in range(5):
    print(i)
#range(n,m) generates progression from n to m-1
for i in range(1,5):
    print(i)
    
for i in range(1,5,2):
    print(i)
    
#algorithms, Back to CS again!
num_list = [213, 321, 123, 312]
max_item = num_list[0]
for num in num_list:
    if max_item <= num:
        max_item = num
print(max_item)
