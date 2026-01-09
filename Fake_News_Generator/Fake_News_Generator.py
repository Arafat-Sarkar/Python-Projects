import random

subjects = [
    "Shakib Khan",
    "Shakib All Hasan",
    "Tarek Rahman",
    "Shekh Hasina",
    "Auto Rickshaw Driver from Dhaka",
    "Dr. Mohammmed Younus"
]


actions = [
    "lunches",
    "cancels",
    "dance with ",
    "eats",
    "deaclares  war on",
    "oders",

]

place_Of_Things =[
    "Inside Dhaka",
    "Dhaka Mohammadpur",
    "Dhaka Airport",
    "inside parliament",
    "Gazipur Rail Station"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_of_thing = random.choice(place_Of_Things)

    hadline = f"BREAKING NEWS: {subject} {action}{ place_of_thing}"

    print("\n" + hadline)

    user_input= input("\nDo You Want Another Headline? (yes/no)").strip().lower()
    if user_input == "no":
        break


print("\nThanks For Using Fake News Generator. Have Fun Day")