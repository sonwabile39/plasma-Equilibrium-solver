#program to print out a sequence with an increment of 7 starting with the number from user
#Sonwabile Baartman
#06 march 2023
number=int(input("Enter the start number:\n"))
if number>-6 and number<93:
    for x in range(number,number+7):
        print(str(x),rjust(2),end="")
        