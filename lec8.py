'''
Rudy Mallamas

Functions
Lec 8
'''

#Funtions are like methods think back to Java Classes.
def my_function(a,b):
    result = a+b 
    
    return result
    
print(my_function(1,2))
print(my_function(1,8))


#one line of code for the same method.
def cal_plus(input1, input2):
    return input1 + input2
    
print(cal_plus(6,7))
print(cal_plus(6,70))

#arguements and params
def cal_plus2(input1, input2):
    print(input1)
    print(input2)
    result = input1 + input2
    return result
    
print(cal_plus2(input2 = 2, input1 = 7))

#this is a 'fruitful function' becasue it has a return statement
def cal_plus3(input1, input2=0):
    print(input1)
    print(input2)
    result = input1 + input2
    return result
    
print(cal_plus3(2, 3))
print(cal_plus3(input2 = 2, input1 = 7))

#params are loal and only exist inside their functions
#print(input1)

#function riddled with logic errors
'''
def cal_abs(a):
    if a > 0:
        return a
    else:
        return -a
    
print(cal_abs('0'))
'''
#same function but made better
def cal_abs2(a):
    if type(a) is str:
        return('wrong data type')
        
    elif a >= 0:
        return a
    else:
        return -a
    
print(cal_abs2(0))
print(cal_abs2('a'))

def cal_sigma(m, n):
    result =0
    for i in range(n,m+1):
        result = result + i
    return result
    
print(cal_sigma(9, 8))

def cal_pi(m, n):
    result =1
    for i in range(n, m+1):
        result = result + i
    return result
    
print(cal_pi(9, 8))

def cal_f(m):
    if m == 0:
        return 1
    else:
        return m * cal_f(m-1)
    
print(cal_f(5))
    
    
def cal_p(m,n):
    return cal_f(m)/cal_f(m-n)
    
print(cal_p(5, 3))