# O.vandenBosch - 9/3/21
# Voting system


def vote():
    
    # Amount of votes per candidate at beginning
    can_a = 0
    can_b = 0
    can_c = 0
    vote = ""
    letters = ['a', 'b', 'c']


    # Checking if END keyword has not been called
    
    

    while vote != "end":
        vote = input("Which candidate would you like to vote for, A, B or C? ")
        print('\n')
        vote = vote.lower()
        if vote == 'end':
            break
        # User validation
        while vote not in letters:
            vote = input("You did not enter a valid amount. Please enter A, B or C? ")
            print('\n')
        
            
        # Adds votes
        if vote.lower() == "a":
                can_a += 1   
        elif vote.lower() == "b":
                can_b += 1
        elif vote.lower() == "c":
                can_c += 1
    
    print(f"Candidate A has {can_a} votes.")
    print(f"Candidate B has {can_b} votes.")
    print(f"Candidate C has {can_c} votes.")

vote()