import random

flips = []
def coin_flip(num):
    
    for i in range(num):
        result = random.randint(1,2)
        
        if result == 1:
            flips.append('T')
        elif result == 2:
            flips.append('H')
        else:
            break   
    tail_count = flips.count('T')
    head_count = flips.count('H')
    print (f'Number of Tails:{tail_count}')
    print (f'Number of Heads:{head_count}')


flips = []
num = int(input('How many times do you want to flip?: '))

coin_flip(num)

