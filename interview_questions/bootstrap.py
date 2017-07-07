from random import choice


def bootstrap_resample(array, n):
    return [choice(array) for i in range(n)]
