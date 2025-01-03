# Flashcard Tester - Simple Version

## Description
This is a simple flashcard tester which takes flashcards from a CSV file, and allows the user to mark each flashcard as either correct or incorrect and records how many times a flashcard is marked correct/incorrect.
In the event that the user incorrectly marks a card correct or incorrect, the user can go back to the previous card.
The amount of times the user gets a flashcard correct or incorrect is also adjusted when the user chooses to go back to the previous card.
Once all flashcards have been tested, the user has a chance to return to the last card, in case they made a mistake on the last card. 
After all flashcards are tested or the user quits prematurely, the CSV file is over written with the updated scores.

## CSV File Requirements - Flashcards
This code requires the python program to be in the same directory as the CSV file which contains the flashcards the user wants to test.
The CSV file requires at least 5 columns:
- side1 - side of the flashcard
- side2 - side of the flashcard
- side3 ... side# - sides of flashcard (optional)
- corr - # of times tester has gotten the answer correct
- incorr - # of times the tester has gotten the answer incorrect
- prev_corr - boolean - did tester get the answer correct last time?
>[!IMPORTANT]
>Last 3 columns must always be correct, incorrect, and prev_corr

>[!NOTE]
>By default, the program assumes that there are column names. Thus, the first row will not be tested.

## Adapting the Code
In the code, update the file name to the desired CSV file name ```db = pd.read_csv('<filename>.csv')```.

To test a subsection of the flashcards, the ```start_ind``` and ```end_ind``` can be updated. Both should be an integer smaller than the amount of flashcards in the CSV file.

If there are more than 2 sides to the flashcards, the sides that show up on the front and back of the flashcards can be adjusted by changing the lists ```fc_front``` and ```fc_back```.
The list of integers are the indexes for the columns in the CSV file.

The delay between button presses can also be adjusted by changing the ```time_delay``` variable.

```
# Global Variables
db = pd.read_csv('math.csv')
rows = db.shape[0] # Number of Rows - Number of flashcards
columns = db.shape[1] # Number of Columns - Number of sides + 3 (corr, incorr, prev_corr)

# EDITABLE VARIABLES
# Sets range of flashcards to test
start_ind = 0
end_ind = rows
# Sets the front and back of flashcards via sides (side1, side2, etc)
fc_front = [2, 0]
fc_back = [2, 1]
# Sets the time delay between when button presses are processed
time_delay = 0.25
```

> [!IMPORTANT]
> In addition, make sure to also update the file name at the end of the program to ensure the data is updated properly.
>```
># Write updated data to new csv
>db.to_csv('math.csv', index=False)
>```
 
