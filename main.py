from __future__ import print_function, unicode_literals
from re import L
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import date, datetime
import time
from pytz import timezone
from PyInquirer import prompt
import requests


# config -------------------------------------------------------------------#
load_dotenv()
DB_KEY = os.getenv("DB_KEY")
client = MongoClient(f"mongodb+srv://Oliver:{DB_KEY}@voters.9miwx.mongodb.net")
db = client.main
votes = db.votes

BST = timezone("Europe/London")
tz = datetime.now(BST)
timenow = tz.strftime('%H:%M:%S %d/%m/%Y')
value = 1
#-------------------------------------------------------------------------------------#

# Vote function
def vote(value):
    os.system('clear')

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
        admin()

    elif vote == "END":
        display()

    elif vote == "A" or "B" or "C":
        name = input("What is your full name? ")
        votes.insert_one({"name": name, "vote": vote, "time": timenow})

    

def display():
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
    VOTING TOTALS:

    Candidate A: {a}
    Candidate B: {b}
    Candidate C: {c}

    Total votes: {a+b+c}
    """)

def corrupt():
    os.system('clear')
    choice = input("Which candidate would you like to corrupt? ")
    choices = ["A", "B", "C"]
    while choice.upper() not in choices:
        choice = input(
        "You did not enter a valid amount. Please enter A, B or C? ")
    print('\n')

    votenum = input(f"How many votes do you want to give to {choice.upper()}? \
    If your choice is more than 10 it may take some time because the program will generate fake names! ")
    while not votenum.isnumeric():
        votenum = input("Please enter a number: ")


    for i in range(0, int(votenum)):
        req = requests.get("https://api.namefake.com")
        res = req.json()
        name = res["name"]
        votes.insert_one({"name": name, "vote": choice.upper(), "time": timenow})

    os.system('clear')
    print(f"Successfully added {votenum} votes to {choice.upper()}. You are a naughty little person 👿! ")
    time.sleep(3)

def admin():
    print(" VOTING SYSTEM \n")

    options = [
    {
        'type': 'list',
        'name': 'choice',
        'message': 'What do you want to do?',
        'choices': [
            'Display votes',
            'Alter votes',
            'Search',
            'Return to voting'
        ]
    }]
    # Prompt to choose what option you do
    
    
    os.system('clear')
    choice = (prompt(options)['choice'])    

    if choice == 'Display votes':
        os.system('clear')
        display()
        print("\n\n")
        finish = input("Type anything to return back: ")
        # Call admin object again
        admin()

    elif choice == 'Alter votes':
        pass

    elif choice == 'Search':
        pass

    elif choice == 'Return to voting':
        pass


vote(value)