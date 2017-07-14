def f(x):
    return x ** 2 - 2 * x


def df(x):
    return 2 * x - 2


def gd(x, k, lr):
    y = f(x)

    for _ in range(k):
        x_prop = x - df(x) * lr  # propose a new x to move to
        if f(x_prop) > y:
            break
        else:
            x = x_prop
            y = f(x)
            lr = lr * 0.999999999

    return (x, y)


x, y = gd(10, 20000, 0.001)
print(round(x, 3), round(y, 3))
