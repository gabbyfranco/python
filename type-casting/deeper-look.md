# Type casting, a deeper look

There are some scenarios in which a given value's data type needs to be changed to some other data type.

This process is known as type casting.

Another, more informal way to refer to it is "data type conversion".

The simplest example of converting data could be the following comparison:

_print(10 == 10)_

In the above piece of code, I'm asking Python if the number 10 is equal to the number 10, and I'll get the boolean value of **_True_** printed, confirming that indeed, they are the same.

What if I do this?

_print(10 == 10.00)_

Again, the boolean value of *_True_* is output on the screen.

Now, you might complain that, well, **_10_** is not **_technically_** equal to 10.0 - because, one might argue, the first number is an integer, and the second number is a float. You would be right - although these are the same numbers, they are not the same data types.

However, Python here perfoms what's known as **_"implicit type conversion"_**.

To understand how this works, I'll slightly tweak the previous example. Instead of asking Python to compare the two numbers and return if they are the same or not, I'll ask Python to print the result of adding these two numbers together.

_print(10 + 10.0)_

The printed result is **_20.0_**.

This output allows me to conclude that **_when Python runs operations involving integers and floats, it implicitly converts the integers type to a float, and then completes the operation_**.

To really drive this point home, I can extend my previous example, using the **_type()_** function:

_print(type(10 + 10.0))_

The output is **_<class 'float'>_**, so this confirms my conclusion.

Let me know show you a small program in Python, working with numbers:

*user_num_1 = input('First number is: ')*
*user_num_2 = input('Second number is: ')*
*user_sum = user_num_1 + user_num_2*
*print(user_sum)*

When I run this program, I could, for example, provide the first number's value as **_5_**, and the second number's value also as **_5_**, expecting that the printed **_user_sum_** value will be **_10_**.

However, when I do exactly that, the number **_55_** gets printed instead.

Why was this not working?

Well, the answer is pretty simple: everything that a user types in, is converted, by Python, to the string data type.

This means that, although I typed numbers into these two inputs, what was saved in ***user_num_1*** and ***user_num_2*** were actually strings.

Effectively, it's exactly the same as if I just did this:

*user_num_1 = "5"*
*user_num_2 = "5"*
*user_sum = user_num_1 + user_num_2*
*print(user_sum)*

This time, the output of printing ***user_sum*** is still ***"55"***, but this comes at no surprise.

In order to have my Python code work as I intended, I need to perform ***explicit type conversion***.

In other words, I have to convert the value of ***"5"*** to the value of ***5***.

Here's my updated code:

*user_num_1 = input('First number is: ')*
*user_num_2 = input('Second number is: ')*
*user_sum = float(user_num_1) + float(user_num_2)*
*print(user_sum)*

What I'm doing here is, I'm making sure that my program can handle even accepting floats as inputs, and still work correctly.

In other words, I'm making sure that if a user provided, say, the float value of **5.5** as both the first and second numbers when running the above code, the output would not throw an error. Instead, it will be the expected ***11.0***.

What if I decide to output some words to the user, telling them what happened?

Here's an attempt at doing that:

*_num_1 = input('First number is: ')_*
*_num_2 = input('Second number is: ')_*
*_user_sum = float(num_1) + float(num_2)_*
*_print("The sum of: " + num_1 + " and " + num_2 + " is " + user_sum)_*

If I run the above code, it will throw the following error:

**_Traceback (most recent call last):_**
  **_File "<string>", line 4, in <module>_**
**_TypeError: can only concatenate str (not "float") to str_**

What this means is, I cannot concatenate a string and a float like that. In other words, although Python's implicit type conversion works when I use the + operator on strings and integers, it does not work on strings and floats.

The solution to this is to perform explicit type conversion, as follows.

*_n1 = input('First number is: ')_*
*_n2 = input('Second number is: ')_*
*_user_sum = float(n1) + float(n2)_*
*_print("The sum of " + str(n1) + " and " + str(n2) + " is " + str(user_sum))_*

This time, the output is: **_The sum of 5.5 and 5.5 is 11.0_**.

In Python, it's easy to perform explicit conversions, and sometimes they are very useful. You'll learn more about how this works as you get more experience in Python.