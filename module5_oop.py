# module5_mod: This file defines a simple class that stores numbers and finds them

class NumberBox:
    # This function runs automatically when we create a new NumberBox
    def __init__(self):
        # Start with an empty list to hold numbers
        self.number_list = []

    # This function adds one number to the list
    def add_number(self, new_number):
        self.number_list.append(new_number)

    # This function looks for a number and returns its position
    def find_number(self, target_number):
        # Check if the number exists in the list
        if target_number in self.number_list:
            # Find its index (starts from 0, so add 1)
            position = self.number_list.index(target_number)
            return position + 1
        else:
            # Return -1 if the number is not found
            return -1