import random

def check_blackjack(total):
    if sum(total) == 21 and len(total) == 2:
        return True
    else:
        return False

def check_ace(cards):
    if 11 in cards:
        return True
    else:
        return False

def draw_card(times):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if times>1:
        return random.sample(cards,times)
    if times == 1:
        return random.choice(cards)
        
flag = 0
computer = draw_card(2)
user = draw_card(2)

#to hide computer's 1st card.
show_computer = ['*']
show_computer.append(computer[1])
print(f"computer :{show_computer}, sum = {computer[1]}")
print(f"user: {user}, sum = {sum(user)}")

#to check for user or computer getting blackjack or both; and if sum of user>21 and have ace
run = True
while run == True:
    if check_blackjack(user) and check_blackjack(computer):
        print("Both have Blackjack: DRAW")
        flag = 1
        run = False
    elif check_blackjack(user) and not check_blackjack(computer):
        print(f"User: {user},sum:{sum(user)} and Computer: {computer},sum:{sum(computer)} ")
        print("User won!")      
        run = False
        flag = 1
    elif not check_blackjack(user) and check_blackjack(computer):
        print("computer won!")
        flag = 1
        run = False
    else:
        if sum(user)>21 and check_ace(user):
            user.remove(11)
            user.append(1)
            print(f"User:{user}")
            if sum(user)>21:
                print("computer won")
                flag = 1
                run = False

    if flag == 0:
        want_to_draw = input("Do you want to draw? type 'y' or 'n': ").lower()

        if want_to_draw == 'y':
            user.append(draw_card(1))
            print(f"User:{user}, sum:{sum(user)}")            
            if sum(user)>21:
                if check_ace(user):
                    user.remove(11)
                    user.append(1)
                    print(f"User:{user} and sum:{sum(user)}")
                    if sum(user)>21:
                        print(f"Computer sum: {sum(computer)}, user sum: {sum(user)}; Computer won!!")
                        flag = 1
                        run = False

        else:
            run = False


if flag == 0:
    while sum(computer) <17:
        computer.append(draw_card(1))

    print(f"Computer drew:{computer}")
info = f"Computer:{computer} sum: {sum(computer)}|| user:{user} sum: {sum(user)};"

if sum(user)<21 and flag == 0:
    if sum(computer)>21:
        print(info + "User won!!")

    elif sum(computer)>sum(user):
        print(info + "Computer won!!")

    elif sum(computer)<sum(user):
        print(info + "user won!!")

    elif sum(computer) == sum(user):
        print(f"Draw! User:{user} and computer:{computer}")