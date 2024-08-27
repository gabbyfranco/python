# Type Casting in Python

Python uses different datatypes of processing, use information effectively.

Sometimes you need to change the data type of a variable after you've collected values for it.

## *Integer Field* - **_123_**

## *String passed* - **_'123'_**  

A user submits a form on a website. One of the *fields* was an *integer*, but the data was passed as a *string*. This is a problem because the only way to perform calculations with the numbers saved as a string is to convert it to an *integer datatype*.

You can use *typecasting* in Python.



Python functions for type casting.

## What is **_Typecasting_**?

***Typecasting*** is the process of converting one data type to another.

There are 2 different types of type casting methods.

1. **Implicit Conversion**
 
    - performed automatically by Python's compiler to prevent data loss.
    - converts _for an example_ - an integer to a float if it picks up that the inserted value is a decimal.
    - Python will only be able to convert values if the data types are compatible. 

    - **_int_** and _**float**_ are compatible but Strings and int are not.
    - if data types are not compatible, Python will throw a type error.

2. **Explicit Conversion**

most common are:

+ string
    - used to convert any data type into a string datatype
    to use:
    ***str(11)***
    ***'11'***

+ int
    to use: 
    *int('20.5')*
    *20*


+ float
to use: 
float('50.4')
50.4

Python has many more typecasting functions and they also have a similar structure.

+ **_ord_**

    - returns an interger representing the underlying unicode character.

+ **_hex_**

    - converts a given integer to a hexadecimal string.

+ **_oct_** 

    - takes an integer and returns a string representing an oct to a number.

## **_IT IS IMPORTANT TO REMEMBER THAT DATATYPES ARE NOT UNCHANGABLE!!!_**

## **_YOU CAN CONVERT DATATYPES USING THE PROVIDED PYTHON FUNCTIONS IF YOU NEED TO_**
    
