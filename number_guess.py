# Import needed Packages
from random import randrange

print(" _____     ____    ____        ____    ____            ____    ____________      _____________    ____________       __________     ____ \n"+
      "|     \   |    |  |    |      |    |  |    \          /    |  |     ____   \    |             |  |     ____   \     /          \   |    |\n"+
      "|      \  |    |  |    |      |    |  |     \        /     |  |    |    |   \   |     ________|  |    |    |   \   |      ___   |  |    |\n"+
      "|       \ |    |  |    |      |    |  |      \      /      |  |    |____|    |  |    |________   |    |____|    |    \   \   |__|  |    |\n"+
      "|    \   \|    |  |    |      |    |  |    \  \    /  /    |  |             /   |             |  |             /       \   \       |    |\n"+
      "|    |\        |  |    \      /    |  |    |\  \  /  /|    |  |     ____    \   |     ________|  |     __     /     __   \   \     |____|\n"+
      "|    | \       |  |     \____/     |  |    | \  \/  / |    |  |    |    |    |  |    |________   |    |  \    \    |  |___\    \    ____ \n"+
      "|    |  \      |   \              /   |    |  \    /  |    |  |    |____|   /   |             |  |    |   \    \   |            |  |    |\n"+
      "|____|   \_____|    \____________/    |____|   \__/   |____|  |____________/    |_____________|  |____|    \____\   \__________/   |____|\n")

# Try to read in score file from /data
# If it doesn't exist yet then skip
try:
    # Note: don't add a dot the the beginning of the path otherwise debug mode will have access to
    # searchpath to data directory as well
    scoreFile = open("/data/score.txt", "r")

    score = int(scoreFile.read())
except:
    # Otherwise initialize score
    score = 0

# Try to read in attemptsfile from /data
try:
    # Import attempts taken
    attemptsFile = open("/data/attempts.txt", "r")

    lastAttempts = int(attemptsFile.read())
except:
    # Otherwise initialize attempts from last game
    lastAttempts = 0

# Initialize current game's attempt counter
attempts = 0

# Display current score
print("Welcome!\nCurrent score for game is: " + str(score))
print("Last number of attempts to win were: " + str(lastAttempts))

# Initialize responses
guess_responses = ["Wrong answer!"] * 10

# Create guess range and responses
possible_guesses = dict(zip(range(1,11),guess_responses))

# Generate correct answer
right_answer = randrange(1, 10, 1)

# Recode correct answer in dictionary
possible_guesses[right_answer] = "You guessed right!"

# Initialize game status
still_playing = 1

# Game status loop
while still_playing == 1:

    # Grab a response from user
    player_response = input("Guess a number between 1 and 10: ")
    attempts += 1
    # Attempt to convert string to number
    # If it breaks, tell user to provide a number
    try:
        player_response = int(player_response)
        
        # Control for response range; should be 1:10
        if (player_response > 1) | (player_response <= 10):

            # Retrieve response to user's guess
            answer_response = possible_guesses[player_response]
            
            # Control for correct answer
            if "right" in answer_response:
                print(answer_response)
                print("You attempted " + str(attempts) + " times to guess right!")
                still_playing = 0

                # Increase score by 1, and write to file
                score += 1
                scoreFile = open("/data/score.txt", "w")
                scoreFile.write(str(score))

                # Close file
                scoreFile.close()

                # Write number of attempts to file
                attemptsFile = open("/data/attempts.txt", "w")
                attemptsFile.write(str(attempts))

                # Close file
                attemptsFile.close()
            else:
                print(answer_response)
                
                # Ask user if they want to try again
                attempt_inquiry = input("Guess again? Pick 'yes' or 'no': ")
                
                if attempt_inquiry == "no":
                    
                    # Change game status
                    still_playing = 0
                    
                    # Display correct answer
                    print("The right answer was: " + str(right_answer))
               
    except:
        print("Please provide a number between 1 and 10!")
