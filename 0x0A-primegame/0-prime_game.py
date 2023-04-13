#!/usr/bin/python3
"""
This module provides a solution to the Prime Game problem.
"""

def check_primes(n: int) -> List[int]:
    """
    Return a list of prime numbers between 1 and n, inclusive.
    
    Args:
        n (int): Upper bound of the range; lower bound is always 1.

    Returns:
        List[int]: A list of prime numbers between 1 and n, inclusive.
    """
    primes_list = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes_list.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes_list


def isWinner(num_rounds: int, upper_limits: List[int]) -> Optional[str]:
    """
    Determine the winner of the Prime Game.

    Args:
        num_rounds (int): Number of rounds in the game.
        upper_limits (List[int]): List of upper limits of the range for each round.

    Returns:
        Optional[str]: Name of the winner (Maria or Ben) or None if the winner cannot be found.
    """
    if num_rounds is None or upper_limits is None or num_rounds == 0 or upper_limits == []:
        return None

    maria_score = 0
    ben_score = 0
    for i in range(num_rounds):
        primes_list = check_primes(upper_limits[i])
        if len(primes_list) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'
    else:
        return None

