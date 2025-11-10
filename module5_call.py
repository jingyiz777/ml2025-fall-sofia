# module5_call: This is the main program that uses our NumberBox class

# 1. Bring in (import) our NumberBox blueprint from the other file
from module5_mod import NumberBox

# 2. Make a new NumberBox to store numbers
box = NumberBox()

# 3. Ask how many numbers the user wants to enter
how_many = int(input("How many numbers? "))

# 4. Use a loop to get each number one by one
for i in range(how_many):
    # i starts at 0, so we show i+1 to the user
    one_number = int(input("Enter number " + str(i + 1) + ": "))
    box.add_number(one_number)

# 5. Ask which number to find
to_find = int(input("Enter the number to find: "))

# 6. Use the class method to search for it
result = box.find_number(to_find)

# 7. Print the answer
print(result)