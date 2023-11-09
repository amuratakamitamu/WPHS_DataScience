import random
song_title_name = ["Song1", "Song2", "Song3", "Song4", "Song5", "Song6"]
song_genre_name = ["Rock", "Pop", "HipHop", "EDM", "Pop", "HipHop"]
rock = 0
pop = 0
hiphop = 0
EDM = 0
log_title = []
log_genre = []
n = int(input("How many songs do you want to play?"))
for i in range(n):
    random2 = random.randint(0, 3)
    title = song_title_name[random2]
    genre = song_genre_name[random2]
    log_title.append(title)
    log_genre.append(genre)
    if genre == "Rock":
        rock += 1
    elif genre == "Pop":
        pop += 1
    elif genre == "HipHop":
        hiphop += 1
    elif genre == "EDM":
        EDM += 1
print(" ")
print("Number of rock songs played is " + str(rock))
print("Number of pop songs played is " + str(pop))
print("Number of hiphop songs played is " + str(hiphop))
print("Number of EDM songs played is " + str(EDM))
print(" ")
print("The experimental probability of rock is " + str(rock / n))
print("The experimental probability of pop is " + str(pop / n))
print("The experimental probability of hiphop is " + str(hiphop / n))
print("The experimental probability of EDM is " + str(EDM / n))
print(" ")
print("Our playlist is: ")
for i in range(n):
    print(str(log_title[i]) + ", " + str(log_genre[i]))
