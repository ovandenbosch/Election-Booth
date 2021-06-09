from __future__ import print_function, unicode_literals
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import date, datetime
import time
from pytz import timezone
from PyInquirer import prompt
import requests
import colorama
from colorama import Fore, Back, Style


# config -------------------------------------------------------------------#
load_dotenv()
DB_KEY = os.getenv("DB_KEY")
client = MongoClient(f"mongodb+srv://Oliver:{DB_KEY}@voters.9miwx.mongodb.net")
db = client.main
votes = db.votes
colorama.init(autoreset=True)
BST = timezone("Europe/London")
tz = datetime.now(BST)
titletime = tz.strftime('%a %d %b, %H:%M:%S')
# Get terminal width so we can display title nicely
cl = os.get_terminal_size().columns
spaces = cl - 35

def title():
    print(f"{Back.GREEN}{Fore.BLACK}VOTING SYSTEM {' ' * spaces} {titletime}")
#-------------------------------------------------------------------------------------#

# Vote function
def start():
    os.system('clear')
    # Responsive title 
    title()

    # Getting input
    user_input = input("Which candidate would you like to vote for, A, B or C? ")
    print('\n')
    choices = ['A', 'B', 'C', 'CORRUPT', 'ADMIN', 'END']

    # User validation cross checking against list
    while user_input.upper() not in choices:
        user_input = input(
            "You did not enter a valid amount. Please enter A, B or C? ")
        print('\n')

    vote = user_input.upper()

    if vote == "CORRUPT":
        corrupt()

    elif vote == "ADMIN":
        # Validation
        attempt_num = 1
        Logged_in = False
        os.system('clear')
        title()
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
            admin()
            Logged_in = False

    elif vote == "END":
        display()

    elif vote == "A" or "B" or "C":
        name = input("What is your full name? ")
        timenow = tz.strftime('%H:%M:%S %d/%m/%Y')
        votes.insert_one({"name": name, "vote": vote, "time": timenow})
        start()
   
def display():
    os.system('clear')
    title()
    a = 0
    b = 0
    c = 0
    for item in votes.find():
        if item["vote"] == "A":
            a += 1

        elif item["vote"] == "B":
            b += 1

        elif item["vote"] == "C":
            c += 1
    
    print(f"""
{Fore.GREEN}VOTING TOTALS:

{Fore.CYAN}Candidate A: {a}
{Fore.CYAN}Candidate B: {b}
{Fore.CYAN}Candidate C: {c}

{Fore.GREEN}Total votes: {a+b+c}
    """)

def corrupt():
    os.system('clear')
    title()
    choice = input("Which candidate would you like to corrupt? ")
    choices = ["A", "B", "C"]
    while choice.upper() not in choices:
        choice = input(
        "You did not enter a valid amount. Please enter A, B or C? ")
    print('\n')

    votenum = input(f"How many votes do you want to give to {choice.upper()}? \nIf your choice is more than 10 it may take some time because the program will generate fake names! ")
    while not votenum.isnumeric():
        votenum = input("Please enter a number: ")


    for i in range(0, int(votenum)):
        req = requests.get("https://api.namefake.com")
        res = req.json()
        name = res["name"]
        timenow = tz.strftime('%H:%M:%S %d/%m/%Y')
        votes.insert_one({"name": name, "vote": choice.upper(), "time": timenow})

    os.system('clear')
    print(f"Successfully added {votenum} votes to {choice.upper()}. You are a naughty little person 👿! ")
    time.sleep(3)

def search():
    os.system('clear')
    title()
    choices = ["A", "B", "C"]
    choice = input("For which candidate would you like to view who voted for them? ")
    while choice.upper() not in choices:
        choice = input("Please enter a valid amount: ")

    os.system('clear')
    print(f"Showing all people that voted for {choice.upper()}:")
    print("----------------------------------------------- \n")

    counter = 1
    for item in votes.find():
        if item["vote"] == choice.upper():
            print(f"{counter}. {item['name']} voted at {item['time']}")
            counter += 1
    
    print("----------------------------------------------- \n")
    if counter == 2:
        num = "person"

    else:
        num = "people"
    print(f"{counter -1} {num} voted for {choice.upper()}")

    finish = input("\nPress enter to return... ")

def alter():
    title()
    display()
    choice = input("Which candidate would you like to change the votes for? ")
    choices = ["A", "B", "C"]
    while choice.upper() not in choices:
        choice = input(
        "You did not enter a valid amount. Please enter A, B or C? ")
    print('\n')

    votenum = input(f"How many votes do you want {choice.upper()} to be changed to? ")
    while not votenum.isnumeric():
        votenum = input("Please enter a number: ")

    counter = 0
    for item in votes.find({"vote": choice.upper()}):
        counter += 1

    if counter < int(votenum):
        to_add = int(votenum) - counter
        print(f"{Fore.RED}{to_add} votes will be added...")
        for i in range(0, int(votenum)):
            req = requests.get("https://api.namefake.com")
            res = req.json()
            name = res["name"]
            timenow = tz.strftime('%H:%M:%S %d/%m/%Y')
            votes.insert_one({"name": name, "vote": choice.upper(), "time": timenow})

        print(f"{Fore.GREEN}Votes successfully added ...")
        
    
    elif counter > int(votenum):
        to_remove = counter - int(votenum)

        while to_remove < 0:
            votenum = input("As you are trying to decrease the amount of votes, please make sure that there are enough votes to be removed... ")
            to_remove = counter - int(votenum)


        print(f"{Fore.RED}{to_remove} votes will be removed...")
        print(to_remove)
        for i in range(0, to_remove):
            votes.delete_one({"vote": choice.upper()})

        print(f"{Fore.GREEN}Votes successfully removed ...")

def daybyday():
    x = votes.find_one()
    print("x", x)
    time.sleep(3)

def admin():
    os.system('clear')
    title()

    options = [
    {
        'type': 'list',
        'name': 'choice',
        'message': 'What do you want to do?',
        'choices': [
            'Display votes',
            'Alter votes',
            'Search who voted for who',
            'Day by day totals',
            'Return to voting'
        ]
    }]
    # Prompt to choose what option you do
    
    
    choice = (prompt(options)['choice'])    

    if choice == 'Display votes':
        os.system('clear')
        display()
        print("\n\n")
        finish = input("Type anything to return back: ")
        # Call admin object again
        admin()

    elif choice == 'Alter votes':
        alter()

    elif choice == 'Search who voted for who':
        search()
        admin()

    elif choice == 'Day by day totals':
        daybyday()

    elif choice == 'Return to voting':
        start()

if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    except RuntimeError:
        print("Runtime Error")
