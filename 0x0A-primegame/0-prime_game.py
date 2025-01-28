#!/usr/bin/python3
"""
module: 0-prime_game
description: Maria and Ben are playing a game.
"""


def isWinner(x, nums):
    """ @description.
    Args:
        x (int): number of rounds.
        nums (List): array of diff. nums.
    Returns:
        name of player that won most rounds.
    """
    # input check
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    ben = 0
    maria = 0
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben = ben + 1
        else:
            maria = maria + 1
    if ben == maria:
        return None
    if ben > maria:
        return "Ben"
    else:
        return "Maria"


def rm_multiples(ls, x):
    """ removes multiples of primes.
    Args:
        ls: list of numbers
        x: rounds.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
