# Looping Constructs

Python has two different types of **_looping constructs_** iterating over sequences.

## **_+ For Loop_**

Looping through data is a fairly common task in any programming language. The **_for_** loop makes it easy to work with any type of sequence in Python.  Let's run through some examples of **_for_** loops and the different ways you can use them.

**_favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']_**

**_for dessert in favorites:_**
    **_print('One of my favorite desserts is', dessert)_**


In the code snippet above, the for loop iterates over the contents of the favorites list and prints out a sentence with the dessert name for each item in the list.

The for loop is based on the size or length of the elements to iterate over. 


1. declare a variable called str, which is of type string
    - recall that _**a string in Python is a sequence**_ which means you can iterate over each character in the string.

*_str = 'Looping' <------- Sequence_*
*_for item<--- variable in str:_<--- sequence* 
    _*print(item)*_

You can access _any_ character in sequence by it's index.

_ex._
_print(str[0])_<-------- Index
- the first item in the sequence is 'L' and accessed with index 0.
- other items can be accessed with the following indexes.
- L = 0, o = 1, o = 2, p = 3, i = 4, n = 5, g = 6 

The For Loop is accessing it in the same way and assigning the current value to the item variable.

This allows us to access the current character to print it for output.

When the code has run, the output will be the letters of the word, looping, each letter on its own line.

## **_+ While Loop_**

On the other hand, a **_while_** loop is based upon a condition being true. Once the condition is no longer true the loop stops. The amount of times the **_while_** loop is executed is not known ahead of time as it is with the **_for_** loop. 

If you take the above **_for_** loop example and convert that to the **_while_** loop alternative, you will end up with something like this:

**_favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']_**

**_count = 0_**

**_while count < len(favorites):_**
    **_print('One of my favorite desserts is', favorites[count]);_**
    **_count += 1_**

Note that you needed to declare a **_counter_** variable. The **_counter_** variable is then compared to the length of the **_favorites_** list. As you loop through the data the **_counter_** is incremented. Once the condition **_count < len(favorites)_** is no longer true the loop will stop.

# Practicing control flow and loops

## **_Controlling loops_**
So far, you have only looped over sequences based on the length of the data you wanted to iterate over. In many cases, this is not necessary and depending on the amount of the data it can also be quite costly. You'll now examine how you can control the flow of the loop and exit out when a specific condition is met. You will also look at control statements such as **_break_**, **_continue_** and **_pass_**. 

## _**If else**_
In many cases, you may need to search for a particular item in a list. Once the item is found, there is no need to continue looping over the other results. Using the same example as before, let's assume you only need to check if the dessert "Churros" is in the list and if it is, print a single statement. 

_#Starter Code_
_favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']_

_for dessert in favorites:_
    _if dessert == 'Churros':_
        _print('Yes! One of my favorite desserts is', dessert)_      

Running the above code will output the following:

**_Yes! One of my favorite desserts is Churros_** 

But what happens if you look for a dessert and that dessert is not on the list? The code above is currently not set up to handle this. Let's look for the dessert "Pudding" which is not on the list, and also add an **_else_** statement to handle the case of when it's not found. If the dessert is not part of the list, you will print a new statement.

_#Starter Code_
_favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']_

_for dessert in favorites:_
    _if dessert == 'Pudding':_
        _print('Yes one of my favorite desserts is', dessert)_ 
    _else:_
        _print('No sorry, that dessert is not on my list')_

Running the above code will result in the following output:

**_No sorry, that dessert is not on my list_**

## Loop control statements

### **_Break_**

The code works as intended but you may notice one flaw. If you change the search term to something that is on the list like "Churros" and run it again you will get the following output:

**_Yes one of my favorite desserts is Churros No sorry, not a dessert on my list_**

This is not what you want! The dessert is on the list but it still printed out the **_else_** condition. To fix it, you need to use a control statement called **_break_**. 

Add the following:

_#Starter Code_
_favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']_

_for dessert in favorites:_
    _if dessert == 'Pudding':_
        _print('Yes one of my favorite desserts is', dessert)_
        _break_
    _else:_
        _print('No sorry, not a dessert on my list')_

Running the above code will resolve the issue. The _**break**_ statement is used to stop the loop, which in turn also stops the **_else_** condition. Without the **_break_** the loop will continue even after the **_if_** condition is satisfied.

### _**Continue**_

Similar to **_break_**, _**continue**_ can be used to control the iteration of the loop. The key difference is that it can allow you to skip over a section of the loop but then continue on with the rest. If you change your code to this, you will notice the outcome will print everything except the Churros dessert.

_#Starter Code_
_favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']_

_for dessert in favorites:_
    _if dessert == 'Churros':_
        _continue_
    _print('Other desserts I like are', dessert)_ 

### _**Pass**_

The _**pass**_ statement allows you to run through the loop in its entirety and effectively ignore that the **_if_** condition has been satisfied.