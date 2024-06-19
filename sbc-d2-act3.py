from random import randint

bet = randint(100, 999)
beet = str(bet)
# print(f"The winning number is {bet}.")

user = input("Hatag Number sa Swertres (three-digit number) STRAIGHT/SCRAMBLE numbers: ")


if user == beet:
    print("Congratulations! Daug ka sa Swertres.")

elif (sorted(user) == sorted(beet)) and (user != bet):
    print("Congratulations! Daug ka sa SCRAMBLE.")

else:
    print(f"Sorry, pildi ka. The winning number was {bet}.")