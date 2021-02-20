import random

flips = []
def coin_flip(num):
    
    for toss_times in range(num):

        result = random.randint(1,2)
        #Only one toss
        if num == 1 and result ==1:
            if result == 1:
                print('It was Tails')
            else:
                print('It was Heads')
            
        #More than one toss    
        if result == 1:
            flips.append('T')
        elif result == 2:
            flips.append('H')
        else:
            pass   
    tail_count = flips.count('T')
    head_count = flips.count('H')
    print (f'Number of Tails:{tail_count}')
    print (f'Number of Heads:{head_count}')


flips = []
num = int(input('How many times do you want to flip?: '))
coin_flip(num)

