import art
import os
def take_input():
    name = input("Name: ")
    bid = int(input("Bid Amount: $"))
    bid_data[name] = bid
def print_final_result():
    bid_list = []
    for key in bid_data:
        bid_list.append(bid_data[key])
    max_bid = max(bid_list)
    name = ""
    for key,value in bid_data.items():
        if value == max_bid:
            name += key
    print(f"{name.capitalize()} is the winner.\nBid Amount: ${max_bid}")
print(art.logo)
print("This is a Secret Auction Program")
bid_data = {}
exit_program = False
#if os.name == 'nt' else 'clear'
while not exit_program:

    take_input()


    yes_or_no = input("Any other person left to bid [type 'yes' or 'no']: ")

    if yes_or_no == "no":
        print_final_result()
        exit_program = True
    else:
        os.system('cls')