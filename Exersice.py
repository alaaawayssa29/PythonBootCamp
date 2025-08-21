Fruits = ["Apple", "Banana", "Orange", "Pineapple", "Stawbbery"]
print(Fruits)
print("The first element is: ", Fruits[0])
print("The last element is: ", Fruits[-1])
Fruits[1] = "Mango"
print(Fruits)
Fruits.insert(2, "Watermelon")
print(Fruits)

fruit = input("Enter the name of fruit: ")
print(Fruits.count(fruit) != 0)

Fruits.sort()
print(Fruits)