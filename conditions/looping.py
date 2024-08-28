favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']

#for loops

for idx, item in enumerate(favorites): # 'in' keyword to specify where I want to loop over; Added new function - range, to specify the number of items.
    print(idx, item) # every arrays usually starts at 0.
    
#while loops 

#specify condition to make the loop over n times. 

#DONE: declare a counter
count = 0

#DONE: enter count after while followed by < sign
#while count < len(favorites):
    #loop will run while the count is less than the length of favorites:
    #DONE: select print function
    #print('My favourite dessert is', favorites[count]) # if count is not incorporated, the code will keep looping until the compiler stops from running out of memory.
    #count += 1
    
# It's important to note that, in a standard for loop, I don't have access to the index, but I can use the enumerate function to do so.

