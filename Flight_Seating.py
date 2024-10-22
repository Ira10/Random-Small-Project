##### Let's make a random flight seating app 

import random

def seat_giver():

    available_list = ['a1','a2','a3','b1','b2','b3','c1','c2','c3','c4','c5','c6','c7','c8','c9']

    filled_list = []

    seats_needed = int(input("How many seats do you need? "))
    for i in range(seats_needed):
        random_seat = random.choice(available_list)
        if random_seat not in filled_list:
            print(f'You have been alloted {random_seat}')
            filled_list.append(random_seat)
            available_list.remove(random_seat)



print(seat_giver())
