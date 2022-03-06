import random
hads = random . randint (1, 99)
print (hads)
user_num = input()
while user_num != 'd':
    if user_num == 'k':
        hads = random.randint(1, hads)
        print (hads)
        user_num = input()
    elif user_num == 'b':
        hads = random.randint(hads, 99)
        print (hads)
        user_num = input()
    
