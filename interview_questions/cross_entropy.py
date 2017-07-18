"""
Define cross-entropy loss. What kinds of problems is it used in?

Write a Python function that takes in two numpy matrices, one a black-and-white
image, and the other an identically shaped set of probability values, and
returns the cross entropy loss score.
"""

import numpy as np


def cross_entropy_loss(img, probs):
    """
    Computes the cross-entropy loss. This is defined as:

        -1 * sum(y_i * log(yhat_i) + (1-y_i) * log(1-yhat_i))

    Where:
    - y_i is the actual value
    - yhat_i is the probability of being class = 1
    """

    # Firstly, flatten the arrays and compute the negative classes.
    img_flat = img.flatten()
    img_neg = 1 - img_flat

    probs_flat = probs.flatten()
    probs_neg = 1 - probs_flat

    # Next, compute loss score.
    loss = - 1 * (img_flat * np.log(probs_flat)
                  + img_neg * np.log(probs_neg))

    return sum(loss)


img = np.array([[1, 0, 1],
                [0, 1, 0],
                [1, 0, 1]])

probs = np.array([[0.9999, 0.0001, 0.9999],
                  [0.0001, 0.9999, 0.0001],
                  [0.9999, 0.0001, 0.9999]])

print(cross_entropy_loss(img, probs))
