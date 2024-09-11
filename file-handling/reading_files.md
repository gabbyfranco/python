# Reading Files

Python offers several built-in functions that make this easier.

There are 3 :

+ read()
    + returns the entire contents of the file as a string that will contain all the characters.
    + can also pass in an integer to return
+ readline()
    + returns a single line as a string.
+ readlines()
    + reads the entire contents of the file and returns it in an ordered list.

Files are stored in directories and they have paths.

***Absolute Paths:***
    + contains leading forward/, or drive label
    + includes all the information you need to locate a file, whether you are in that files directory or not.
    + 

***Relative Paths:***
    + normally don't contain any reference to the root directory and  normally relative to the calling file. 
    + only includes the information you need to locate a file in your current working directory.