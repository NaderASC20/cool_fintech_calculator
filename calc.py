# Restaurant Tip Calculator
# Created by Nader Daruvala and Tia Hannah

print('-' * 50)
total = float(input("What is the total bill cost? ")) # Total cost of the bill
percent = int(input("What is your desired tip percent? (exclude % symbol please!) ")) / 100 # Percent tip as a decimal, ex. .20 = 20%
people = int(input("How many people were seated at your table? (Including you) ")) # Number of people at the table
server = int(input("How would you rate your server out of 5")) 
print('-' * 50 + "\n\n\n")

# Simple calculator
def tip_simple(total, percent = .15, people = 1):
    tip = total * percent
    split = tip / people
    return ("=" * 50) + "\n" + f"You're total tip is: ${tip}".center(50) + "\n" + f"That is equal to ${split} per person!".center(50) + "\n" + ("=" * 50)

# 5 = 25%  / 4 = 20%  / 3 = 15%  / 2 = 10% / 1 = 5%

def server_tip(server):
    if server == 5:
        return total * .25
    elif server == 4:
        return total  
    elif server == 3:
        return total 
    elif server == 2
        return total 
    elif server == 1 
        return total    
   
    
print(tip_simple(total, percent, people))