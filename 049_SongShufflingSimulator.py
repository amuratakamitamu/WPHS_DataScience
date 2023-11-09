import random
alternative = 0
classical = 0
hiphop = 0
jpop = 0
kpop = 0
musical_theature = 0
reggae = 0
techno = 0
trap = 0
vocal_tech = 0
rock = 0
pop = 0
indie = 0
country = 0
R_B = 0
Rap = 0
number_of_songs = int(input("How many songs do you want to play?"))
log_title = []
log_genre = []
for i in range(number_of_songs):
    random_number_picked = random.randint(0, len(song_genre_file)-1)
    song = song_title_file[random_number_picked]
    genre = song_genre_file[random_number_picked]
    log_title.append(song)
    log_genre.append(genre)
    if genre == "Rock":
        rock += 1
    elif genre == "Pop":
        pop += 1
    elif genre == "Indie":
        indie += 1
    elif genre == "Country":
        country += 1
    elif genre == "R&B":
        R_B += 1
    elif genre == "Rap":
        Rap += 1
    elif genre == "Alternative":
        alternative += 1
    elif genre == "Classical":
        classical += 1
    elif genre == "Hip Hop":
        hiphop += 1
    elif genre == "J Pop":
        jpop += 1
    elif genre == "K Pop":
        kpop += 1
    elif genre == "Musical Theature":
        musical_theature += 1
    elif genre == "Reggae":
        reggae += 1
    elif techno == "Techno":
        techno += 1
    elif genre == "Trap":
        trap += 1
    elif genre == "Vocal Tech":
        vocal_tech += 1
print(" ")
print("Number of rock songs played is " + str(rock))
print("Number of pop songs played is " + str(pop))
print("Number of Indie songs played is " + str(indie))
print("Number of Country songs played is " + str(country))
print("Number of R&B songs played is " + str(R_B))
print("Number of rap songs played is " + str(Rap))
print("Number of alternative songs played is " + str(alternative))
print("Number of classical songs played is " + str(classical))
print("Number of hiphop songs played is " + str(hiphop))
print("Number of jpop songs played is " + str(jpop))
print("Number of kpop songs played is " + str(kpop))
print("Number of musical_theature songs played is " + str(musical_theature))
print("Number of reggae songs played is " + str(reggae))
print("Number of techno songs played is " + str(techno))
print("Number of trap songs played is " + str(trap))
print("Number of vocal_tech songs played is " + str(vocal_tech))
print(" ")
print("The experimental probability of rock is " + str(rock / number_of_songs))
print("The experimental probability of pop is " + str(pop / number_of_songs))
print("The experimental probability of indie is " + str(indie / number_of_songs))
print("The experimental probability of country is " +
      str(country / number_of_songs))
print("The experimental probability of R&B is " + str(R_B / number_of_songs))
print("The experimental probability of rap is " + str(Rap / number_of_songs))
print("The experimental probability of alternative is " +
      str(alternative / number_of_songs))
print("The experimental probability of classical is " +
      str(classical / number_of_songs))
print("The experimental probability of hiphop is " +
      str(hiphop / number_of_songs))
print("The experimental probability of jpop is " + str(jpop / number_of_songs))
print("The experimental probability of kpop is " + str(kpop / number_of_songs))
print("The experimental probability of musical_theature is " +
      str(musical_theature / number_of_songs))
print("The experimental probability of reggae is " +
      str(reggae / number_of_songs))
print("The experimental probability of techno is " +
      str(techno / number_of_songs))
print("The experimental probability of trap is " + str(trap / number_of_songs))
print("The experimental probability of vocal_tech is " +
      str(vocal_tech / number_of_songs))
print(" ")
print("Our playlist is: ")
for i in range(number_of_songs):
    print(str(log_title[i]) + ", " + str(log_genre[i]))
