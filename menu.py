from random import *

appetizers = ["Tater Tots", "Chicken Wings", "Salad", "Spring Rolls", "Chips and Salsa"]
main = ["Salmon", "Chicken Alfredo", "Quesadilla", "Rice and Beans"]
dessert = ["Chocolate Mousse", "Ice Cream", "Fruit Custard"]

x = randint(0, len(appetizers)-1)
print("appetizers: ", appetizers[x])

y = randint(0, len(main)-1)
print("main course: ", main[y])

z = randint(0, len(main)-1)
print("dessert: ", dessert[z])

for num in appetizers:
    print(num)
for num in main:
    print(num)
for num in dessert:
    print(num)
