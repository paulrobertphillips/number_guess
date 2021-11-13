# Number Guess Game Powered By Docker
Paul R Phillips<br>
11/13/2021

**Description**<br>
I have built a very simple number guessing game in Python. The algorithm itself
generates a random number 1 through 10, and has the player guess what number that is.
The player has infinite number of tries to get it right, but can also quit after the
first attempt. If the player quits the program displays the correct answer. 

**Environment**<br>
The Python script is powered by Docker; that is, its entirety lives in the Docker-based virtual
environment. Docker handles the storage of cumulative score and number of attempts from
the previous game. A volume has been mounted in the Docker image so that the game can persist.

**Development**<br>
I have included a series 
