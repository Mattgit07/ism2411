#Module 10 - Reflection
#1. what suprised me the most about python lists was how easy it is to change them by adding, removing or sorting items. I also didnt expect to be able to use negative indexes to access items from the end of a list.
# 2. When I worked as a cashier at Publix, python lists could have been useful for organizing and analyzing daily sales. Instead of manually calculatinf totals and averages in Excel, I coudl use a list and python funcitons to calculate  evertrhing automatically.
# 
# excercise 1 --build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))
#excercise 2 --index practice
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])
#ecxercise 3 -- slicing
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])
#xcercise 4 -- modify
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)
#excercise 5 --tuple comparison
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("TypeError caught: Tuples cannot be changed.")
    print("Tuples are useful for coordinates because they keep the values unchanged")

    print(coords)
    #excercise 6 -- average of a list of sales
    sales = [100, 250, 75, 480, 200]
    total = sum(sales)
    count = len(sales)
    average = total / count
    print("Total:", total)
    print("Count:", count)
    print("Average:", average)
    print("Best:", max(sales))
    print("Worst:", min(sales))
    #excercise 7 - accumulator pattern
    prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original prices:", prices)
print("Discounted prices:", discounted)
#excercise 8 -- filter above threshold
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", sum(high_sales) / len(high_sales))
