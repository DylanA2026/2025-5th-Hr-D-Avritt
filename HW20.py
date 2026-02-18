#Name: Dylan Avritt
#Class: 5th Hour
#Assignment: HW20

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class Items:
    def __init__(self, stock, price, weight):
        self.stock = stock
        self.price = price
        self.weight = weight

    def doubleCost(self):
        self.price *=  2

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
Banana = Items(10,1,0.2)
HamburgerMeat = Items(30,20,10)
Strawberry = Items(40,5,2)
#3. Print the stock of all three objects and the cost of the second store item.
print(f"Banana Stock: {Banana.stock}, Hamburger Meat: {HamburgerMeat.stock}, Straberry stock: {Strawberry.stock}" )
print(f"Hamburger Meat Price: {HamburgerMeat.price}")

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
HamburgerMeat.doubleCost()
print(f"Hamburger Meat New Price: {HamburgerMeat.price}")
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
Strawberry.stock *= 1/4
print(f"New Strawberry Stock: {Strawberry.stock}")
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del Banana

try:
    print("Banana Stock: ", Banana.stock)
except:
    print("We don't have any more Bananas!!!")