# Inputs in Python(Inputs & Outputs)

## *Inputs*

The input function is designed to get  data from a source of inputs and can be used in different ways.

### ex.

*email = input ('Please enter your email address:')*

## *Print Arguments*

*#comma separated*
*print (1, 2, 3)*
*1 2 3*

*#arithmetics*
*print(1 + 3)*
*4*

*#string concatenation*
name = 'John'

Python's print function also has reserved keywords that can be parsed as additional arguments.

These include:

### *objects* 
    - It is values that are printed onscreen
    
### *sep*
    - which defines how the objects being printed or separated using commas or strings.

### *end*
    - defines what gets printed at the end.

### *files*
    - specifies where values get printed to, and by default it is STD out.

### *flush*
    - Boolean expressions to flush the buffer, which essentially just moves the data from a temporary storage to the computers permanent memory storage.

## *Print parameters*

*print('Hello', 'you!', sep=', ')*

## *Direct formatting*

*a = 10*
*b = 5*
*ans = a + b*
*print('Adding the value of{} and {} = {}. format(a, b, ans))*

Python allows for direct formatting inside the print statement. You can also control the order by specufying the numbers inside the curly brackets.

