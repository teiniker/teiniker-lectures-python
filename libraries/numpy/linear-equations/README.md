# NumPy: Solving Linear Equations

We can solve a system of linear equations in Python using NumPy's `linalg.solve` 
method. 

Suppose we have the following system of linear equations:

$$
3x + 2y + z = 1 \\
2x - 2y + 4z = -2 \\
-x + \frac{1}{2}y - z = 0
$$

In matrix form, this can be expressed as: $AX = B$

where  

$$
A = \begin{bmatrix}3 & 2 & 1 \\ 2 & -2 & 4 \\ -1 & 0.5 & -1\end{bmatrix}, 
\quad X = \begin{bmatrix}x \\ y \\ z\end{bmatrix}, 
\quad B = \begin{bmatrix}1 \\ -2 \\ 0\end{bmatrix}
$$


In Python, we can represent this system using NumPy arrays and 
solve it as follows:

```python
import numpy as np

# Define matrix A (coefficients) and vector B (constants)
A = np.array([[3, 2, 1],
              [2, -2, 4],
              [-1, 0.5, -1]])

B = np.array([1, -2, 0])

# Solve the system AX = B
solution = np.linalg.solve(A, B)

print("Solution:", solution)
```


```
Solution: [ 1. -2. -2.]
```

* `np.linalg.solve(A, B)` computes the solution efficiently.
     The solution represents values for \( x, y, z \) respectively.

* If the system might not have a unique solution, consider using 
    `numpy.linalg.lstsq(A, B, rcond=None)` for a least-squares solution.
* For symbolic math, we can use `sympy`.

