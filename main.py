# O.vandenBosch - 9/3/21
# Cloned from repository on GitHub https://github.com/ovandenbosch/Election-Booth
# Voting system

''' Specific keywords:
    1. ADMIN -> Sends you to an admin screen
    2. END -> Stops the program and logs all votes
    3. CORRUPT -> Adds 100000 votes to the next vote

'''
from __future__ import print_function, unicode_literals
from PyInquirer import prompt
import os
import time

# Initialise starting values
candidate_a = 0
candidate_b = 0
candidate_c = 0
voteValue = 1
names_array = []

# Main voting function
def voteFunc(value, can_a, can_b, can_c, names):
    os.system('clear')

    # Initialise variables
    vote = ""
    letters = ['a', 'b', 'c', 'corrupt', 'admin', 'end']
    overall = [can_a, can_b, can_c]

    # Getting input
    vote = input("Which candidate would you like to vote for, A, B or C? ")
    print('\n')

    # Allows both A or a for example
    vote = vote.lower()

    # User validation cross checking against list
    while vote.lower() not in letters:
        vote = input(
            "You did not enter a valid amount. Please enter A, B or C? ")
        print('\n')
    
    # Corrupt function
    if vote.lower() == 'corrupt':
        value = 100000
        voteFunc(value, can_a, can_b, can_c)
    
    # Calling admin function
    elif vote.lower() == 'admin':
        attempt_num = 1
        Logged_in = False
        os.system('clear')
        # User has 3 attempts to get password right
        while attempt_num <= 3:
            
            questions = [
                            {
                                'type': 'password',
                                'message': 'Enter your password',
                                'name': 'password'
                            }
                        ]
            # Uses external module called Pyinquirer to create a nice prompt            
            password = prompt(questions)

            # User is logged in
            if password['password'] == 'VOTING 101':
                Logged_in = True
                break
            
            # Application stops if someone gets 3 passwords wrong
            elif attempt_num == 3:
                os.system('clear')
                print("You have entered the wrong password too many times! This application will now stop!!")
                time.sleep(2)
                break

            else:
                os.system('clear')
                print('Your password was incorrect, please try again...')
                attempt_num += 1
                
        # Only works if user is logged in
        if Logged_in == True:
            # Calling admin function
            os.system('clear')
            admin(overall, can_a, can_b, can_c, names)
            Logged_in = False
        
    # Adds votes - uses value keyword as we don't know whether the value will be 1 or 100,000
    elif vote.lower() == "a":
        # Getting name
        firstname = input("What is your first name? ")
        surname = input("What is your surname? ")
        can_a += value
        value = 1
        names.append(f"{firstname} {surname} - Candidate A")
        voteFunc(value, can_a, can_b, can_c, names)

    elif vote.lower() == "b":
        # Getting name
        firstname = input("What is your first name? ")
        surname = input("What is your surname? ")
        can_b += value
        value = 1
        names.append(f"{firstname} {surname} - Candidate B")
        voteFunc(value, can_a, can_b, can_c, names)

    elif vote.lower() == "c":
        # Getting name
        firstname = input("What is your first name? ")
        surname = input("What is your surname? ")
        can_c += value
        value = 1
        names.append(f"{firstname} {surname} - Candidate C")
        voteFunc(value, can_a, can_b, can_c, names)

    # End function to display all votes and stop the program
    elif vote.lower() == 'end':
        overall = [can_a, can_b, can_c]
        display(overall, names)

# Save vote data to a text file
def save(allVotes, can_a, can_b, can_c, names):
    # Open file for votes
    with open("votes.txt", "w") as voteFile:
        for voteitem in allVotes:
            # Write information
            voteFile.write(f"{voteitem}, \n")

    # Open file for names
    with open("names.txt", "w") as nameFile:
        for name in names:
            nameFile.write(f"{name}, ")

    overall = [can_a, can_b, can_c]
    # Return to admin screen
    print("Data has been successfully saved...")
    time.sleep(2)
    admin(overall, can_a, can_b, can_c, names)

# Loads existing data from a text file
def load(can_a, can_b, can_c, names):
    # Opens file
    with open("votes.txt", "r") as voteFile:
        items = voteFile.readlines()
        array = []
        for voteitem in items:
            voteitem = int(voteitem.split(', \n')[0])
            array.append(voteitem)

    # Open name file
    with open("names.txt", "r") as nameFile:
        newnames = []
        for item in nameFile:
            newnames.append(item)
    # Adds item to array    
    can_a = array[0]
    can_b = array[1]
    can_c = array[2]
    names = newnames

    os.system('clear')
    overall = [can_a, can_b, can_c]
    # Return to admin screen
    print("Data has been successfully loaded...")
    time.sleep(2)
    admin(overall, can_a, can_b, can_c, names)
    
# Function to change votes
def change(can_a, can_b, can_c, names):
    options = [
    {
        'type': 'list',
        'name': 'choice',
        'message': 'For which candidate would you like to change the votes for?',
        'choices': [
            'Candidate A',
            'Candidate B',
            'Candidate C',
            'Return to voting',
        ]
    }]

    # Nice prompt
    choice = (prompt(options)['choice'])

    # Allow user to specify how many votes to alter
    if choice == 'Candidate A':
        print(f"Candidate A currently has {can_a} votes")
        votenum = input("How many votes do you want to give to Candidate A? ")
        while not votenum.isnumeric():
            votenum = input("Please enter a number: ")
        
        os.system('clear')
        print(f"Successfully changed the amount of votes to {votenum}")
        can_a = votenum
        time.sleep(2)

    elif choice == 'Candidate B':
        print(f"Candidate B currently has {can_b} votes")
        votenum = input("How many votes do you want to give to Candidate B? ")
        while not votenum.isnumeric():
            votenum = input("Please enter a number: ")
        
        os.system('clear')
        print(f"Successfully changed the amount of votes to {votenum}")
        can_b = votenum
        time.sleep(2)

    elif choice == 'Candidate C':
        print(f"Candidate C currently has {can_c} votes")
        votenum = input("How many votes do you want to give to Candidate C? ")
        
        while not votenum.isnumeric():
            votenum = input("Please enter a number: ")

        os.system('clear')        
        print(f"Successfully changed the amount of votes to {votenum}")
        can_c = votenum
        time.sleep(2)


    elif choice == 'Return to voting':
        os.system('clear')

    overall = [can_a, can_b, can_c]
    # Return to admin screen
    admin(overall, can_a, can_b, can_c, names)
    
# Displays votes to screen
def display(allVotes, names):
    choices = ["Candidate A", "Candidate B", "Candidate C"]
    i = 0
    totalvotes = 0
    for item in allVotes:
        print(f"{choices[i]} has {item} votes.")
        totalvotes += int(item)
        i += 1
    
    print(f"Total votes: {totalvotes}")
    print(f"The voters details: \n {names}")

def search(names):
    choice = input("For which candidate would you like to search for? (A, B, C) ")
    values = ["A", "B", "C"]
    while choice.upper() not in values:
        choice = input("Please enter a valid candidate: ")

    array_list = []
    title = ""
    
    for name in names:
        if name[-1] == choice.upper():
            title = name[-11:]
            name = name[:-14]
            array_list.append(name)

    print(f"Showing all votes made for {title}: \n")
    for item in array_list:
        print(item)

    time.sleep(3)



# Admin screen 
def admin(overall, can_a, can_b, can_c, names):
    print(" VOTING SYSTEM \n")

    options = [
    {
        'type': 'list',
        'name': 'choice',
        'message': 'What do you want to do?',
        'choices': [
            'Save Data',
            'Load Data',
            'Display votes',
            'Alter votes',
            'Search',
            'Return to voting'
        ]
    }]
    # Prompt to choose what option you do
    
    
    os.system('clear')
    choice = (prompt(options)['choice'])
    if choice == 'Save Data':
        save(overall, can_a, can_b, can_c, names)

    elif choice == 'Load Data':
        load(can_a, can_b, can_c, names)

    elif choice == 'Display votes':
        os.system('clear')
        display(overall, names)
        print("\n\n")
        finish = input("Type anything to return back")
        # Call admin object again
        admin(overall, can_a, can_b, can_c, names)

    elif choice == 'Alter votes':
        change(can_a, can_b, can_c, names)

    elif choice == 'Search':
        search(names)

    elif choice == 'Return to voting':
        voteFunc(voteValue, can_a, can_b, can_c, names)
    
# Calling function and stopping if any errors
if __name__ == '__main__':
    try:
        voteFunc(voteValue, candidate_a, candidate_b, candidate_c, names_array)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    except RuntimeError:
        print('Runtime Error')