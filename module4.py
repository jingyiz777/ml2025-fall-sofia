# 1. Ask the user how many numbers they want
how_many_string = input("How many numbers? ")
total_count = int(how_many_string)

# 2. Make an empty list to hold the numbers
number_list = []

# 3. Use a loop to ask one by one
for i in range(total_count):
    
    # This way, we can ask for "number 1", "number 2", etc.
    prompt = "Enter number " + str(i + 1) + ": "
    
    one_number_string = input(prompt)
    one_number = int(one_number_string)
    
    # Add this number to the list
    number_list.append(one_number)

# 4. Ask the user which number they want to find
number_to_find_string = input("Enter the number to find: ")
number_to_find = int(number_to_find_string)

# 5. Check if the number is in the list
if number_to_find in number_list:
    # If it is, find its spot
    # .index() finds the spot (but starts counting from 0)
    position_from_zero = number_list.index(number_to_find)
    
    # The problem wants us to start counting from 1, so we add 1
    print(position_from_zero + 1)
else:
    # If it's not in the list, print -1
    print("-1")