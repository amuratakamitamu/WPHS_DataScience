import math
bool2 = input("Do you know the length of the hypotenuse?")
if bool2 == "yes":
    a = int(
        input("Without units, what is the length of the hypotenuse of the triangle?"))
    b = int(
        input("Without units, what is the length of the hypotenuse of the triangle?"))
    ans = math.sqrt(math.pow(a, 2) - math.pow(b, 2))
    print("Leg = " + str(ans))
elif bool2 == "no":
    a = int(input("Without units, what is the length of the legs of the triangle?"))
    b = int(input("Without units, what is the length of the other leg of the triangle?"))
    ans = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    print("Hypotenuse = " + str(ans))
else:
    print("WARNING: Write down  yes  or  no")
