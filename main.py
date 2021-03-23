# O.vandenBosch - 9/3/21
# Cloned from private repository on GitHub https://github.com/ovandenbosch
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
        # Getting input
        vote = input("Which candidate would you like to vote for, A, B or C? ")
        print('\n')
        # Allows both A or a for example
        vote = vote.lower()
        # Checking if end keyword again
        if vote == 'end':
            ## exits the while loop and goes to the print statements below
            break
            
        # User validation cross checking against list
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
    
    # Printing votes
    print(f"Candidate A has {can_a} votes.")
    print(f"Candidate B has {can_b} votes.")
    print(f"Candidate C has {can_c} votes.")

    askagain = input('Would you like to go again, [y,n]')
    if askagain == 'y':
        vote()


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