"""
What is bootstrap resampling? When do you use it?

Implement bootstrap resampling in Python.
"""

from random import choice


def bootstrap_resample(array, n):
    return [choice(array) for i in range(n)]
