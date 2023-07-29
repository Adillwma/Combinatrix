# -*- coding: utf-8 -*-
# Combinatrix v1.0.1
# Build created on Thu Sep 8 2022
# Author: Adill Al-Ashgar


import math

def calc_permutations_combinations(number_of_possible_choices, number_of_choices_to_make, allow_repetitions=True):       
    """
    Calculate the number of permutations and combinations of a given number of choices from a given number of possible choices.
    
    Parameters:
    number_of_possible_choices (int): Total number of possible choices.
    number_of_choices_to_make (int): Number of choices to make.
    allow_repetitions (bool): If True, repetition of a choice is allowed.
    
    Returns:
    tuple: A tuple containing two integers - (combinations, permutations).
    """
    n = number_of_possible_choices
    r = number_of_choices_to_make

    if n == 0 or r == 0:
        combinations = 0
        permutations = 0

    else:
        if allow_repetitions:
            combinations = math.comb(n + r - 1, r)
            permutations = n ** r
        else:
            combinations = math.comb(n, r)
            permutations = combinations * math.factorial(r)

    return int(combinations), int(permutations)
