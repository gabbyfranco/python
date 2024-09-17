# # DONE: filter list
menu = ['frappuccino', "hot chocolate", "latte", "espresso", "americano", "cappuccino", "cortado", "mocha"]

# # DONE: type def and name of function
def find_coffee(coffee): #coffee perimetre will be the coffee from my list
    if coffee[0] == 'f':
        return coffee


# # DONE: USE a map
# # DONE: create map_coffee to filter coffee
# map_coffee = map(find_coffee, menu)
# # DONE: print map_coffee
# print(map_coffee)

# # DONE: iterate through the map object 
# for x in map_coffee:
#     print(x)

# How to get the output with the filter function?

# DONE: declare variable and assign filter function
filter_coffee = filter(find_coffee, menu)

# DONE: print out variable 
print(filter_coffee) 

# TODO: iterate through the filter object
for x in filter_coffee:
    print(x)