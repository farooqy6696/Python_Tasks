#3. Grocery List Manager

file = open("Day8Tasks/grocery.txt", "w")

n = int(input("How many grocery items? "))

for i in range(n):
    item = input("Enter item: ")
    file.write(item + "\n")

file.close()

print("Grocery items saved succesfully. ")