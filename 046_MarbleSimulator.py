import random
marble_name_file = ["Comet", "Bumblebee", "Cats_eye",
                    "Watermelon", "Dragonfly", "Girl_Scout", "Spiderman"]
marble_color_file = ["white", "yellow",
                     "blue", "green", "blue", "green", "red"]
white = 0
yellow = 0
blue = 0
green = 0
red = 0
number_of_marbles = int(
    input("How many marbles would you like to select from the bag?"))
marbles_selected_list = []
colors_selected_list = []
for i in range(number_of_marbles):
    random_number_picked = random.randint(0, 6)
    marble = marble_name_file[random_number_picked]
    color = marble_color_file[random_number_picked]
    marbles_selected_list.append(marble)
    colors_selected_list.append(color)
    if color == "White":
        white += 1
    elif color == "yellow":
        yellow += 1
    elif color == "blue":
        blue += 1
    elif color == "green":
        green += 1
    elif color == "red":
        red += 1
print(" ")
print("The number of white marbles selected is: " + str(white))
print("The number of yellow marbles selected is: " + str(yellow))
print("The number of blue marbles selected is: " + str(blue))
print("The number of green marbles selected is: " + str(green))
print("The number of red marbles selected is: " + str(red))
print(" ")
print("The experimental probability of white is: " +
      str(white / number_of_marbles))
print("The experimental probability of yellow is: " +
      str(yellow / number_of_marbles))
print("The experimental probability of blue is: " + str(blue / number_of_marbles))
print("The experimental probability of green is: " +
      str(green / number_of_marbles))
print("The experimental probability of red is: " + str(red / number_of_marbles))
print("" "")
print("Our selection is: ")
for i in range(number_of_marbles):
    print(str(marbles_selected_list[i]) + ", " + str(colors_selected_list[i]))
