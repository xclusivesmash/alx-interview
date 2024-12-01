#!/usr/bin/python3
"""
module: 0-making_change
description: determines the fewest number of coins
needed to meet a given amount: total.
"""


def makeChange(coins, total):
    """check description above.
    Args:
        coins (array): input array with coins
        total (int): total summation based on coins.
    Returns: #coins
        - If total is 0 or less, return 0
        - If total cannot be met by any number of coins you have, return -1
    """
    # inpur check
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    # workflow
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
