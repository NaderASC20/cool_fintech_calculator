# Created by Nader Daruvala and Tia Hannah
# Restaurant Tip Calculator

print('-' * 50)
total = float(input("What is the total bill cost? ")) # Total cost of the bill

people = int(input("How many people were seated at your table? (Including you)?  ")) # Number of people at the table
while people < 1:
    people = int(input("Please include yourself! Try again. How many people were at your table? ")) # Number of people at the table

server = int(input("How would you rate your server out of 5? (1 - 5 only) "))
while server < 1 or server > 5:
    server = int(input("Your input was not valid! Try again. How would you rate your server (1 - 5 only) ")) # Number of people at the table

# Percent = # Function call
print('-' * 50 + "\n\n")
# Simple calculator


def tip_calc(total, server, people):
    tip = server_tip(total, server)
    split = tip / people
    cost = total + tip
    return ("=" * 50) + "\n" + f'Total cost: ${cost}'.center(50) + "\n" + f"Total tip: ${tip}".center(50) + "\n" + f"Each person pays ${split} for tip!".center(50) + "\n" + ("=" * 50) + "\n"

def server_tip(total, server):
    ratings = {
        5 : .25 * total,
        4 : .20 * total,
        3 : .15 * total,
        2 : .10 * total,
        1 : .05 * total
    }

    return ratings[server]

print(tip_calc(total,server,people))