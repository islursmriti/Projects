import random
def play():
    user = input("enter your choice 'r' for rock  'p' for paper  's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    print(f"I got {computer}")
    if user == computer:
        #print(f"I got {computer}")
        return 'it\'s a tie'
    if is_win(user, computer):
        return 'You won!!'
    return 'You lost!!'
    
def is_win(player, opponent):
    #r>s p>r s>p
    if (player=='r' and opponent=='s') or (player=='p' and opponent=='r') or (player=='s' and opponent=='p'):
        return True
print (play())