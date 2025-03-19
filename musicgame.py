import random

def load_high_scores(filename="musicgamehighscores.txt"):
    high_scores = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, points = line.strip().split()
                high_scores.append({"name": name, "points": int(points)})
    except FileNotFoundError:
        pass
    return high_scores

def display_high_scores(high_scores):
    print("High Scores:")
    print("{:<10} {:<10}".format("Name", "Points"))
    for score in high_scores:
        print("{:<10} {:<10}".format(score['name'], score['points']))

def update_high_scores(high_scores, name, points):
    high_scores.append({"name": name, "points": points})
    high_scores.sort(key=lambda x: x["points"], reverse=True)
    return high_scores[:5]

def update_high_scores(high_scores, name, points):
    high_scores.append({"name": name, "points": points})
    high_scores.sort(key=lambda x: x["points"], reverse=True)
    return high_scores[:5]

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

high_scores = update_high_scores(high_scores, name, points)
display_high_scores(high_scores)
save_high_scores(high_scores)
