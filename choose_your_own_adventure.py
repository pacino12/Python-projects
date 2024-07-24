name = input("Type your name: ")
print("Warm welcome", name, "to this adventure")
answer = input(
    "You are on a dirt roard, It has come to an end and you can go lef or right . which way would you like to go:").lower()
if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim . Type walk to walk around or swim to swim accross: ")
    if answer == "swim":
        print("You swim across and got eaten by alligator.")
    elif answer == "walk":
        print("You walk for many miles and run out of water and then die.")

elif answer == "right":
    answer = input(
        "You come to a brige , It looks wobbyly, Do you wanna cross it or head back? (cross or back) ").lower
    if answer == "back":
        print(
            "You go  back to a main road. Now you can decide to drive to the left or right ")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a Stranger. Do you talk to them (Yes or No)").lower()
        if answer == "yes":
            print("You Talked to the stranger and they hand you a Gold and you Win")
        elif answer == "no":
            print("You Ignored the strasnger and they feel offended and you Loose")
        else:
            print("Not a valid option YOU LOOSE")

    print()
else:
    print("Not a valid option you loose")
print("Thank you for playing", name,)
