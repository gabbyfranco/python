# Namespaces & scopes

The official Python documentation defines *__namespace__* as mapping from naes to objects, and *__scope__* is he textual region of a python program where the *__namespace__* is directly accessible.

Modules are a type of *__namespace__*.

Four main types of scopes defined in Python:

+ local
 * first search for a variable
+ Enclosed
 * defined inside an enclosing or nested functions.
+ GLobal 
 * defined as the uppermost level or simply outside functions
+ Built-in
 * keywords present in the built-in module.

*__Scope resolution__* follows what is known commonly as the *__LEGB rule__*.