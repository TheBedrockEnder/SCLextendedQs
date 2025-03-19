import random
HighScore = open("musicgamehighscores.txt", "r+")
HighScoreRead = HighScore.read()

print("Welcome to the music game!")

name = input("Enter your name: ")

Music = [["Aritst A", "Song A", "Song A 2"],["Artist B", "Song B", "Song B 2"],["Artist C", "Song C", "Song C 2"]]

Guess_Number = 0
Guess = ""
points = 0
while Guess_Number < 2:
    if Guess_Number == 0:
        Music_copy = [list(artist) for artist in Music]
        Music_random = (random.choice(Music_copy))
        if len(Music_random) == 0:
            continue
        Music_artist = Music_random.pop(0)
        Song = random.randint(0, len(Music_random)-1)
        print("Artist: ", Music_artist, "Song: ", Music_random[Song][0])
    Guess = input("What is the name of the song? ")
    if Guess == Music_random[Song]:
        print("Correct!")
        if Guess_Number == 0:
            points += 3
        else:
            points += 1
        Guess_Number = 0
    else:
        Guess_Number += 1
        print("Wrong! you have ", 2-Guess_Number, "guesses left")

print ("Game over! You got ", points, "point(s)")

HighScore.write(name + " " + str(points) + "\n")
print("High Scores = \n", HighScoreRead)