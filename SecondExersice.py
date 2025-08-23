Prices = {
    "apple": 3,
    "orange":5,
    "mango":7,
    "pineapple":10,
    "watermelon":5
}
fruit = input("Enter the name of the fruit: ")
if fruit in Prices:
    print("The price is:", Prices.get(fruit))
else:
    print("Sorry, this fruit is not available!!")