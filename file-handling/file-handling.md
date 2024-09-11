# File Handling in Python 

Python has several built in functions to create and manipulate files.

File handling includes opening, , and writing files amongst other operations.

***It's important to learn how to work with files.***

Whether you're working with data on your computer, on the web or in the cloud, it will most likely be saved in some type of file.

There are two types of file handling functions in Python.- Open & Close.

The *__Open__* function is used for reading, writing, and creating files. It accepts two arguments:

1. The file name and/or the file location
2. The mode
    - indicates what action is required such as reading, writing or creating.
    - specifies if you want the file output in text or binary format.

    - First you have ***r*** which is used to open and read a file in text
    - ***rb*** opens and reads a file in binary format.
    - ***r+*** opens the file for both reading and writing 
    - ***w*** opens the file for writing.
        - ***w*** will overwrite the existing file.
    - ***a*** opens files for editing or appending data.

The *__Close__* function is used for closing the open file connection, know that it __does not__ take any arguments.   

There's one more way to open and close a file in Python and that's with the ***Open*** function.
The advantage of using it is that *it closes the file automatically.*

In Python, you generally handle files in two ways, either in text or binary format.

***Text Format:*** more user friendly because humans can read.
***Binary Format:*** You won't be able to read files in binary formats, but they are much more compact and therefore result in better performance.

Python uses text as the default format for file handling. So just passing in any mode for reading or writing a file will automatically set it to a text format.

To set the file handling to binary, you need to pass the letter b along with either the read or write option. _for example,_ you write open the file name and *__rb__* to read a file in binary format or *__ab__* to append or add to a file in binary format.