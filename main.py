# O.vandenBosch - 9/3/21
# Cloned from repository on GitHub https://github.com/ovandenbosch/Election-Booth
# Voting system

''' Specific keywords - ADMIN --> sends you to the admin screen

'''
from __future__ import print_function, unicode_literals
from typing import overload
from PyInquirer import prompt
import os
import time

can_a = 0
can_b = 0
can_c = 0
voteValue = 1
def voteFunc(value, can_a, can_b, can_c):

    # Amount of votes per candidate at beginning

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

        if vote == 'corrupt':
            value = 100000
        
        if vote == 'admin':
            attempt_num = 0
            Logged_in = False
            while attempt_num < 3:
                os.system('clear')
                
                questions = [
                                {
                                    'type': 'password',
                                    'message': 'Enter your password',
                                    'name': 'password'
                                }
                            ]
                # Uses external module called Pyinquirer to create a nice prompt            
                password = prompt(questions)

                if password['password'] == 'a':
                    Logged_in = True
                    break
                
                elif attempt_num == 3:
                    print("You have entered the wrong password too many times!")
                    time.sleep(2)

                else:
                    print('Your password was incorrect')
                    attempt_num += 1
                    print(attempt_num)
                    time.sleep(1)
                    
            if Logged_in == True:
                admin(can_a, can_b, can_c, overall)
                value = admin.value

                print(can_a)
                time.sleep(3)
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
        os.system('clear')
        
    # Refers to display function
    display(overall)

    

# Saves vote data to a text file
def save(allVotes, can_a, can_b, can_c):
    with open("votes.txt", "w") as voteFile:
        for voteitem in allVotes:
            voteFile.write(f"{voteitem}, \n")
    os.system('clear')
    voteFunc(can_a, can_b, can_c, voteValue)

# Loads existing data from a text file
def load(can_a, can_b, can_c):
    
    with open("votes.txt", "r") as voteFile:
        items = voteFile.readlines()
        array = []
        for voteitem in items:
            voteitem = int(voteitem.split(', \n')[0])
            array.append(voteitem)
            
    print(array)
    time.sleep(3)
    can_a = array[0]
    can_b = array[1]
    can_c = array[2]

    voteFunc(can_a, can_b, can_c, voteValue)
       
    

# Function to change votes
def change(can_a, can_b, can_c):
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

    choice = (prompt(options)['choice'])

    if choice == 'Candidate A':
        print(f"Candidate A currently has {can_a} votes")
        votenum = input("How many votes do you want to give to Candidate A?")
        while not votenum.isnumeric():
            votenum = input("Please enter a number: ")
        
        print(f"Successfully changed the amount of votes to {votenum}")
        can_a = votenum
        time.sleep(2)

    elif choice == 'Candidate B':
        print(f"Candidate B currently has {can_b} votes")
        votenum = int(input("How many votes do you want to give to Candidate B?"))
        while not votenum.isnumeric():
            votenum = input("Please enter a number: ")
        
        print(f"Successfully changed the amount of votes to {votenum}")
        can_a = votenum
        time.sleep(2)

    elif choice == 'Candidate C':
        print(f"Candidate C currently has {can_c} votes")
        votenum = int(input("How many votes do you want to give to Candidate C?"))
        
        while not votenum.isnumeric():
            votenum = input("Please enter a number: ")
        
        print(f"Successfully changed the amount of votes to {votenum}")
        can_a = votenum
        time.sleep(2)


    elif choice == 'Return to voting':
        os.system('clear')

    voteFunc(can_a, can_b, can_c, voteValue)
    
# Displays votes to screen
def display(allVotes):
    choices = ["Candidate A", "Candidate B", "Candidate C"]
    i = 0
    totalvotes = 0
    for item in allVotes:
        print(f"{choices[i]} has {item} votes.")
        totalvotes += int(item)
        i += 1
    
    print(f"Total votes: {totalvotes}")

# Admin screen 
def admin(can_a, can_b, can_c, overall):
    os.system("clear")
    print(" VOTING SYSTEM \n")
    
    # Initialise our admin value object
    admin.value = 1

    options = [
    {
        'type': 'list',
        'name': 'choice',
        'message': 'What do you want to do?',
        'choices': [
            'Save Data',
            'Load Data',
            'Display votes',
            # 'Alter votes',
            'Alter votes',
            'Return to voting'
        ]
    }]

    choice = (prompt(options)['choice'])
    if choice == 'Save Data':
        save(allVotes=overall, can_a=can_a, can_b=can_b, can_c=can_c)

    elif choice == 'Load Data':
        load(can_a, can_b, can_c)

    elif choice == 'Display votes':
        os.system('clear')
        display(overall)
        time.sleep(3)

    elif choice == 'Alter votes':
        change(can_a, can_b, can_c)

    elif choice == 'Return to voting':
        pass

    



# Calling function and stopping if any errors
if __name__ == '__main__':
    try:
        voteFunc(voteValue, can_a, can_b, can_c)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    except RuntimeError:
        print('Runtime Error')
    finally:
        print("Have a good day")