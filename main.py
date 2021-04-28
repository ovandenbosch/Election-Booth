# O.vandenBosch - 9/3/21
# Cloned from repository on GitHub https://github.com/ovandenbosch/Election-Booth
# Voting system

''' Specific keywords - ADMIN --> sends you to the admin screen

'''
import os
import time


def vote():

    # Amount of votes per candidate at beginning
    can_a = 0
    can_b = 0
    can_c = 0
    
    # We need to set the initial value because if system is corrupted, value will change to 100,000
    value = 1
    vote = ""
    letters = ['a', 'b', 'c', 'corrupt']
    overall = [0, 0, 0]

    # Checking if END keyword has not been called

    while vote != "end":
        # Getting input
        vote = input("Which candidate would you like to vote for, A, B or C? ")
        print('\n')

        # Allows both A or a for example
        vote = vote.lower()

        # Checking if end keyword again
        if vote == 'end':

            ## exits the while loop and goes to the print statements below
            break
        
        if vote == 'admin':
            admin()

       

        # User validation cross checking against list
        while vote not in letters:
            vote = input(
                "You did not enter a valid amount. Please enter A, B or C? ")
            print('\n')

        # Adds votes - uses value keyword as we don't know whether the value will be 1 or 100,000

        if vote.lower() == "a":
            can_a += value
        elif vote.lower() == "b":
            can_b += value
        elif vote.lower() == "c":
            can_c += value
        
        overall = [can_a, can_b, can_c]

    # Refers to log function
    log(overall)

    # Asking the user if they would like to start the system again after calling end.
    askagain = input('Would you like to go again, [y,n]')
    if askagain == 'y':
        vote()



def save(allVotes):
    with open("votes.txt", "w") as voteFile:
        for voteitem in allVotes:
            voteFile.write(f"{voteitem}, \n")

# Logs votes to screen
def log(allVotes):
    choices = ["Candidate A", "Candidate B", "Candidate C"]
    i = 0
    totalvotes = 0
    for item in allVotes:
        print(f"{choices[i]} has {item} votes.")
        totalvotes += item
    
    print(f"Total votes: {totalvotes}")

 # Handling what happens if someone corrupts the system
def corrupt(value):
    # Setting the vote to 100,000
    value = 100000
    vote = input(
        "You have corrupted the system you naughty person! Choose who you want to give 100,000 votes to: "
    )
    

def admin():
    os.system("Clear")
    print(" VOTING SYSTEM ")

    choice = int(input('''
    Pick an option

    1. CORRUPT
    2. SAVE
    3. LOAD
    4. EDIT
    
    '''))

    if choice == 1:
        corrupt(value)

# Calling function and stopping if any errors
if __name__ == '__main__':
    try:
        vote()
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    except RuntimeError:
        print('Runtime Error')
    finally:
        print("Have a good day")