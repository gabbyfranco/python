# What are data structures?
This reading introduces you to data structures. So far, you have only stored small bits of data in a variable. This was either an integer, Boolean or a string. 

But what happens if you need to work with more complex information, such as a collection of data like a list of people or a list of companies? 

Data structures are designed for this very purpose.

Data structures in Python

A data structure allows you to organize and arrange your data to perform operations on them. Python has the following built-in data structures: ***List, dictionary, tuple and set.*** These are all considered ***non-primitive*** data structures, meaning they are classed as objects, this will be explored later in the course. 

Along with the built-in data structures, Python allows users to create their own. Data structures such as Stacks, Queues and Trees can all be created by the user. 

Each data structure can be designed to solve a particular problem or optimize a current solution to make it much more performant.

## Mutability and Immutability

Data Structures can be mutable or immutable. The next question you may ask is, what is mutability? Mutability refers to data inside the data structure that can be modified. For example, you can either change, update, or delete the data when needed. A list is an example of a mutable data structure. The opposite of mutable is immutable. An immutable data structure will not allow modification once the data has been set. The tuple is an example of an immutable data structure.

# Choosing and using data structures

## Which data structure to choose?

The tricky part for new developers is understanding which data structure is suited to the required solution. Each data structure offers a different approach to storing, accessing and updating the information stored inside it. There can be many factors to select from, including ***size***, ***speed*** and ***performance***. The best way to try and understand which one is more suitable is through an example.

### Example: Employees list

In this example, there's a list of employees that work in a restaurant. You need to be able to find an employee by their employee ID - an integer-based numeric ID. The function ***get_employee*** contains a ***for*** loop to iterate over the list of employees and returns an employee object if the ID matches. 

*employee_list = [(12345, "John", "Kitchen"), (12458, "Paul", "House Floor")]*

*def get_employee(id):*
    *for employee in employee_list:*
        *if employee[0] == id:*
            *return {"id": employee[0], "name":* *employee[1], "department": employee[2]}*

*print(get_employee(12458))*

In this code, ***employee_list*** is a list of tuples. The code runs well and will return the user Paul, as its ID, 12458, is matched. The challenge comes when the list gets bigger. 

Instead of two employees, you may have 2000 or even 20,000. The code will have to iterate over the list sequentially until the number is matched. 

You could optimize the code to split the search, but even with this, it still lacks in performance in comparison to other data structures, such as the dictionary.

*employee_dict = {*
    *12345: {*
        *"id": "12345",*
        *"name": "John",* 
        *"department": "Kitchen"*
    *},*
    *12458: {*
       *"id": "12458",*
       *"name": "Paul",* 
       *"department": "House Floor"*    
    *}*
*}*

*def get_employee_from_dict(id):*
    *return employee_dict[id];*


*print(get_employee_from_dict(12458));*

Notice how, in this code block, if you change the data structure to use a dictionary, it will allow you to find the employee. The main difference is that you no longer need to iterate over the list to locate them. If the list expands to a much larger size, the seek time to find the employee stays the same. 

This is a prime example of how to choose the right data structure to suit the solution. 

Both work well, but the trade-off to be considered is that of time and scale. The first solution will work well for smaller amounts of data, but loses performance as the data scales. 

The second solution is better suited to large amounts of data as its structure allows for a constant seek time allowing large amounts of data to be accessed at a constant rate.

This example shows that there is no one size fits all solution and careful consideration should be given to the choice of data structure to be used depending on the constraints of the solution.
