'''
Lec 7
While Loop
continue, break, pass
2/28/23

i = 5
while i >0:
    print(i)
    

i = 5
while i >0:
    i = i -1
    print(i)

i = 5
while i >0:
    i = i -1
    print(i)
    
    if i ==3:
        break
    print(i)
    '''
'''  
i=5
while i >0:
    i = i -1
    print(i)
    if i ==3:
        continue
    print(i)
    
    for item in ['a', 'b']:
        print(item)
        i = 5
        while i > 0:
            i = i -1
            print(i)
            
            if i ==3:
                break
'''

i = 5 
while i > 0:
    i = i -1
    
    if i ==3:
        pass
    
    print(i)
try:
    print(1/0)
    
except:
    print('error')
    
i = 5 
while i > 0:
    try:
        print(1/(i-3))
    except:
        pass
    
    i = i -1

    
