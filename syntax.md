## Python syntax cheat sheet

This reading provides you with a cheat sheet that can be used for quick reference.

### Spacing

#### Correct

#any ammount of whitespace on a single line is ok
x     =        1        +        2

#### Incorrect 

x = 1
+ 2

### Indentation

#### Correct 
def say_hello():
    print("Hello there!")

print(say_hello())

## OR!!!

def say_hello(): print("Hello there!")

print(say_hello())

#### Incorrect 
def say_hello():
print("Hello there!")

    def say_hello():
print("Hello there")