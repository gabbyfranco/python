# Method Resolution Order

It's important to know that Python has many types of inheritance.

The categorization types of based on the number of parents and child classes as well as the hierarchical order, including simple inheritance.

There 5 types of inheritance:

1. *__Simple Inheritance__*
    
2. *__Multiple Inheritance__*

    - Involves a child class inheriting from more than one parent.

3. *__Multi Level Inheritance__*

    - Inheritance taking place on several levels.

4. *__Hierarchical Inheritance__*

    - concerns how several sub classes inherit from a common parent.

5. *__Hybrid Inheritance__*

    - Mixes characteristics of the others.  

*__Method Resolution Order__* or *__M.R.O__* determines the order in which given method or attributes is passed is through in a search of the hierarchy of classes for its resolution or in other words, from where it belongs.

The order of resolution is called *__linearization__* of a class.

The default order in python is bottom to top, left to right when imagining the *__inheritance__* of these python classes in a tree structure.

The object is first searched in the class of that object and then in its *__super class__*.

