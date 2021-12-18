

'''
low = input('Set lower interval border')
high = input('Set high interval border')
third_number = input('Give a number')

a = int(low)
b = int(high)
x = int(third_number)

if x == a:
    print("The number is equal to the lower bound of the interval")

elif x == b:
    ("The number is equal to the upper bound of the interval")
    
elif x > a or x < b:
     print("The number is in the interval")
    
elif x < a: 
    print("The number is outside the interval, x < a") 

elif x > b:
    print("The number is outside the interval, x > b")
    

'''
'''
# simple answers

while True:
    
    word = input('write a random word: ')

    if 'hello' in word:
        print("Hello there, good stranger!")
    
    elif "how are you?" in word:
        print("I am fine, thanks. How are you?")

    elif 'feelins' in word:
        print("I am a machine. I have no feelings")
    print("I am a machine. I have no feelings")
    
    elif 'age' in word:
        print("I have no age. Only current timestamp")
    
    elif 
    
while True:
    text = input("Say what? ")

    if "hello" in text or "Hello" in text:
        print("Hello there, good stranger!")
    elif "how are you?" in text:
        print("I am fine, thanks. How are you?")
    elif "feelings" in text:
        print("I am a machine. I have no feelings")
    elif "age" in text:
        print("I have no age. Only current timestamp")
    else:
        print("Sorry, I don't understan you. Try hello, feelings or age")
        
'''

'''
# count to ten

counter = 0
loop = 0

while loop == 0:
    if counter <= 9:
        counter +=1
        print(counter)
    
    elif counter == 10:
        while loop == 0:
            
            counter -= 1
            print(counter)
            if counter == 1:
                loop += 1
            
                
'''                
            
'''           
       # count to user 
       
inp = input('Enter a number: ')
n = int(inp)
m = 0

while m <= n:
    m += 1
    print(m)

'''
'''
# user to user

inp = input('Enter a number: ')
a = int(inp)
inp2 = input('Enter a number: ')
b = int(inp2)
counter1 = a
counter2 = b

if a < b:
    while counter1 < b:
        counter1 += 1
        print(counter1)
        
elif b < a: 
    while counter2 < a:
        counter2 += 1
        print(counter2)
'''
'''
'''
# even odd interval

'''
inp1 = input('Enter first number: ')
inp2 = input('Enter second number: ')
a = int(inp1) 
b = int(inp2)

counter1 = a
counter2 = b

if a < b:
    while counter1 < b:
        counter1 += 1
        print(counter1)
        
elif b < a:
    while counter2 < a:
        counter2 += 1
        print(counter2)
'''

# 60k
'''
counter = 1 

while True:
    counter += 1
    print(counter)
    if counter == 60000:
        
        print('End of program')
        break

'''

# sum n

inp = input('Enter a number: ')
count = 0

if '.' in inp or ',' in inp:
    print('Number must be whole number')

else:
    N = int(inp)
    while count < N:
        count += 1
        print(count)
    
  




























