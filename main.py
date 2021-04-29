# O.vandenBosch - 9/3/21
# Cloned from repository on GitHub https://github.com/ovandenbosch/Election-Booth
# Voting system

''' Specific keywords - ADMIN --> sends you to the admin screen

'''
import os
import time
voteValue = 1


def voteFunc(value):

    # Amount of votes per candidate at beginning
    can_a = 0
    can_b = 0
    can_c = 0
    
     
    
    vote = ""
    letters = ['a', 'b', 'c', 'corrupt', 'admin', 'end']
    overall = [0, 0, 0]

    # Checking if END keyword has not been called

    while vote != "end":

        voteFunc.overall = overall
        # Getting input
        vote = input("Which candidate would you like to vote for, A, B or C? ")
        print('\n')

        # Allows both A or a for example
        vote = vote.lower()

        # User validation cross checking against list
        while vote not in letters:
            vote = input(
                "You did not enter a valid amount. Please enter A, B or C? ")
            print('\n')


        # Checking if end keyword again
        if vote == 'end':
            break
        
        if vote == 'admin':
            attempt_num = 0
            Logged_in = False
            while attempt_num < 3:
                os.system('Clear')
                password = input("What is the password: ")
                if password == 'VOTING 101':
                    Logged_in = True
                    break
                
                elif attempt_num == 3:
                    print("You have entered the wrong password too many times!")
                    time.sleep(3)

                else:
                    print('Your password was incorrect')
                    attempt_num += 1
                    print(attempt_num)
                    
            if Logged_in == True:
                load.loaded = False
                admin()
                value = admin.value
                if load.loaded == True:              
                    can_a = load.varNames[0]
                    can_b = load.varNames[1]
                    can_c = load.varNames[2]
                Logged_in = False
        
       
        
        # Adds votes - uses value keyword as we don't know whether the value will be 1 or 100,000
        if vote.lower() == "a":
            can_a += value
            value = 1
        elif vote.lower() == "b":
            can_b += value
            value = 1
        elif vote.lower() == "c":
            can_c += value
            value = 1
        
        overall = [can_a, can_b, can_c] 
        voteFunc.overall = overall     
        os.system('clear')
        
    # Refers to display function
    display(overall)
    

 

# Saves vote data to a text file
def save(allVotes):
    with open("votes.txt", "w") as voteFile:
        for voteitem in allVotes:
            voteFile.write(f"{voteitem}, \n")

# Loads existing data from a text file
def load():
    with open("votes.txt", "r") as voteFile:
        can_a = 0
        can_b = 0
        can_c = 0
        load.varNames = [can_a, can_b, can_c]
        i = 0
        items = voteFile.readlines()
        for voteitem in items:
            voteitem = int(voteitem[0].split(', \n')[0])

            load.varNames[i] = voteitem
            i+=1
    
    load.loaded = True
    time.sleep(3)

# Function to change votes
def change():
    time.sleep(3)
    

# Displays votes to screen
def display(allVotes):
    choices = ["Candidate A", "Candidate B", "Candidate C"]
    i = 0
    totalvotes = 0
    for item in allVotes:
        print(f"{choices[i]} has {item} votes.")
        totalvotes += item
    
    print(f"Total votes: {totalvotes}")
  

def admin():
    os.system("Clear")
    print(" VOTING SYSTEM ")
    
    # Initialise our admin value object
    admin.value = 1

    choice = int(input('''
    Pick an option

    1. Save Data
    2. Load Data from text file
    3. Display current vote count
    4. Alter current votes
    5. Return to voting
    
    '''))

    if choice == 1:
        save(voteFunc.overall)

    if choice == 2:
        load()

    if choice == 3:
        os.system('Clear')
        display(voteFunc.overall)
        time.sleep(3)

    if choice == 4:
        change()

    if choice == 5:
        os.system('Clear')

    # To corrupt system, hacker must enter 6
    if choice == 6:
        admin.value = 122
        
        


# Calling function and stopping if any errors
if __name__ == '__main__':
    try:
        voteFunc(voteValue)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    except RuntimeError:
        print('Runtime Error')
    finally:
        print("Have a good day")