foods = []
prices = []
total = 0

while True:
    food = input("Enter the food name ( q means Queit) : ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price {food}$ : "))
        foods.append(food)
        prices.append(price)

print("------Your Cart-----")
for food in foods:
    print(food, end=" ")




for price in prices:
    total += price

print()
print(f"Your Total Bil ${total}")
     
     

     
    