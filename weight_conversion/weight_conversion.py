weight = float(input("Enter You Weight : "))
unit = input(" Kilogram or Pounds? ( K Or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"

elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"

else:
    print(f"{unit} is Not Valid")

print(f"Your Weight is : {weight} {unit}")