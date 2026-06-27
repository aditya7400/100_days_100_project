import art , os
import random as rd



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def win_or_loose(player,dealer):
    dealer_score = f"Dealer: {dealer} score: {sum(dealer)}"
    player_score = f"Player: {player} score: {sum(player)}"
    if sum(player) > 21:
        print(dealer_score,player_score,sep="\n")
        print("you loose")
    elif sum(player) < sum(dealer):
        print(dealer_score, player_score, sep="\n")
        print("you loose")
    elif sum(player) > sum(dealer):
        print(dealer_score, player_score, sep="\n")
        print("you won")
    else:
        print(dealer_score, player_score, sep="\n")
        print("draw")

def play(player , dealer, cards):
    hit_or_stand = input("You want to hit or stand ['y' for hit and 'n' for stand]: ")
    if hit_or_stand == "y":
        player.append(rd.choice(cards))
        print(f"Player: {player} score: {sum(player)}")
        if sum(player) > 21:
            print("you loose")
            return
        play(player,dealer,cards)

    else:
        win_or_loose(player,dealer)

exit_game = False
while not exit_game:

    want_to_play= input("Do you want to play the game of Black Jack['y' or 'n']: ")
    if want_to_play == 'y':
        os.system('cls')
        print(art.logo)
        player = rd.choices(cards,k=2)
        dealer = rd.choices(cards,k=2)
        if sum(dealer)<= 13:
            dealer.append(rd.choice(cards))

        print(f"your cards are {player}")
        print(f"Dealers first hand is {dealer[0]}")
        play(player,dealer,cards)
    else:
        exit_game = True