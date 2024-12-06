# Hot key to run is CTRL + F5

# Simple Flashcard Tester - Samantha Song - started 2024.12.05
# Tests all flashcards and updates/records # of times correct/incorrect
# Takes in a CSV file with at least 5 columns:
#   side1 - side of the flashcard
#   side2 - side of the flashcard
#   side3 ... side# - sides of flashcard
#   corr - # of times tester has gotten the answer correct
#   incorr - # of times the tester has gotten the answer incorrect
#   prev_corr - boolean - did tester get the answer correct last time?
#       prev_corr is used for if tester made a mistake on previous flashcard

# Imports
import keyboard
import time
import pandas as pd

# # Global Variables
db = pd.read_csv('flashcards.csv')
print(db) 
time_delay = 0.25

# Sets range of flashcards to test
start_ind = 0
end_ind = db.shape[0]
ids = range(start_ind, end_ind)

# Sets the front and back of flashcards via sides (side1, side2, etc)
fc_front = [0]
fc_back = [1]

# Flashcards - Last 3 columns must always be correct, incorrect, and prev_corr
corr = db.shape[0] - 3
incorr = db.shape[0] - 2
prev_corr = db.shape[0] -1


# Tests all flashcards based on test_ids and test_set
def test_all(test_ids, test_set, front, back):
    # End if there are no Flashcards to test
    if len(test_ids) == 0:
        print("There are no flashcards to test")
        return 1
    # Test all Flashcards in set one by one unless tester exits (corr/incorr keep progress)
    # Number of tested flashcards - can change if tester makes a mistake
    num_test = 0
    # Start on front side f
    front_side = True
    while num_test <= len(test_ids):
        # Allows tester to fix previous mistake if not the first card
        if num_test > 0:
            print("Press \'b\' to return to previous flashcard.\n")

        # Check to see if a mistake was made on last FC end otherwise
        if num_test == len(test_ids):
            print("\nPress the SPACE BAR to complete the test.\n\n")
            while True: 
                # If tester chooses to end the session prematurely
                if keyboard.is_pressed('q'):
                    return 3
                # If tester made a mistake on the previous FC
                # Index will automatically be last index - has not yet been updated
                if keyboard.is_pressed('b'):
                    print("Showing the previous flashcard")
                    prev_prev_corr = test_set[index][prev_corr]
                    if prev_prev_corr == True:
                        test_set[index][corr] -= 1
                    else:
                        test_set[index][incorr] -= 1
                    num_test -= 1
                    front_side = True
                    break
                if keyboard.is_pressed('space'):
                    # Once all FC have been tested - finish test session
                    print("You have completed all the flashcards in this set.")
                    return 2

        # Makes it easier to go back if a mistake was made
        index = test_ids[num_test]

        # Prints Front Side
        if front_side == True:
            for side in front:
                print(str(test_set[index][side]))
        # Prints Back Side
        else:
            for side in back:
                print(str(test_set[index][side]))
        print("\nPress \'f\' if you were incorrect.")
        print("Press \'j\' if you were correct.")
        print("\nPress the SPACE BAR to flip the card.")
        print("\nTo end the session, press \'q\'")
        print("\n\n")

        # Wait on each flashcard until tester gets them correct or incorrect
        time.sleep(time_delay)
        while True: 
            # If tester chooses to end the session prematurely
            if keyboard.is_pressed('q'):
                return 3
            # If tester made a mistake on the previous FC
            if keyboard.is_pressed('b') and num_test > 0:
                print("Showing the previous flashcard")
                prev_index = index - 1
                prev_prev_corr = test_set[prev_index][prev_corr]
                if prev_prev_corr == True:
                    test_set[prev_index][corr] -= 1
                else:
                    test_set[prev_index][incorr] -= 1
                num_test -= 1
                front_side = True
                break
            # Tester gets the flashcard Incorrect
            if keyboard.is_pressed('f'):
                print("You got this flashcard incorrect")
                # Update Incorrect and Last Correct
                test_set[index][incorr] += 1
                test_set[index][prev_corr] = False
                num_test += 1
                front_side = True
                break
            # Tester gets the flashcard Correct
            if keyboard.is_pressed('j'):
                print("You got this flashcard correct!")
                # Update Correct and Last Correct
                test_set[index][corr] += 1
                test_set[index][prev_corr] = True
                num_test += 1
                front_side = True
                break
            # Tester flips the flashcard
            if keyboard.is_pressed('space'):
                front_side = not front_side
                break
        # Print both sides?
    # Once all FC have been tested - finish test session
    print("You have completed all the flashcards in this set.")
    return 2


# Tests flashcards
test_all(ids, db, fc_front, fc_back)

# Write updated data to new csv
db.to_csv('flashcards.csv')