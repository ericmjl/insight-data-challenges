"""
Question: Define gradient descent.

For the case of y = x^2 + 3x + 1, implement gradient descent in Python to find
the minima.

The function should take in
- a starting point `x`
- a precision parameter `k` that specifies how much error is allowed.
- a learning rate parameter `lr` that controls the rate of descent.
"""


def f(x):
    return x ** 2 + 3 * x + 1


def df(x):
    return 2 * x + 3


def gd(x, k, lr):
    prev_step_size = x

    while prev_step_size > k:
        # print(x)
        prev_x = x
        x += - df(prev_x) * lr
        prev_step_size = abs(x - prev_x)

    y = f(x)

    return (x, y)


x, y = gd(15, 0.000001, 0.01)
print(round(x, 3), round(y, 3))
