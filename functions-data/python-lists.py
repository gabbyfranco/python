#LISTS

# DONE: declare lists
list1 = [1, 2, 3, 4, 5] # In order to declare a list, I start by typing list 1 as my variable. For my values, I type in 1, 2, 3, 4, and 5 within brackets and separate the number values with commas because it's to help separate items in a list.

# DONE: list strings
list2 = ['A', 'B', 'C'] # Strings are A, B, and C with '' or ""

# DONE: list different datatypes
list3 = ['Hello', 1, True, 40.22] # This can have a String, boolean, float, or an integer
# Type doesn't really matter. It's just going to be stored in the same way.

list4 =[1, [2, 3, 4], 5, 6] # This is valid too :)

# Another way to add items to a list

# Use the insert function 

# * sign and click on Run  
print(*list1) # after clicking RUN the entire list gets printed out. 

for x in list1:
    print('Value:', x)