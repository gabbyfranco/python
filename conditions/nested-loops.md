# Nested Loops and the effect on algorithmic complexity

**_Nested loops_** can be used to solve more complex problems.

ex.

*_outer loop_*
*_for x in range(10):_*
    *_print(x)_*
    *#inner loop*
    *for y in range(10):*
        *print(y)*

A nested for loop is written by indentation inside the outer loop.

1. It starts then step into the inner loop.
2. the inner loop will run until its range limit is met. 
3. Once the inner loop completes, it will come back to the outer loop for the next iteration 
4. step into the inner loop again.