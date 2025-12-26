email = input("Enter the Email :")

index = email.index("@")
username = email[:index]
domain = email[index +1 :]

print(f"Your Username is {username} And Your Domain is {domain}")