#Game preparations
import random

num_player = input("Enter number of player: ")
num_player_int = int(num_player)
count = 1
list_a = []
while count <= num_player_int:
    count_str = str(count)
    player_name = input("Enter player "+count_str+" name: ")
    list_a.append(player_name)

    count += 1
print (list_a)

def dealer_pick():
    dealer = random.randrange(1,num_player_int)

    return(list_a[dealer])
print("The dealer is ",dealer_pick())