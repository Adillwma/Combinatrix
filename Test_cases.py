from Combinatrix import calc_permutations_combinations



# Test Cases
def run_test_cases(test_cases):
    for idx, test_case in enumerate(test_cases, 1):
        n, r, allow_repetitions, expected_combs, expected_perms = test_case
        combinations, permutations = calc_permutations_combinations(n, r, allow_repetitions)
        print(f"Test Case {idx}: n={n}, r={r}, Repetitions Allowed={allow_repetitions}")
        print(f"Function found {combinations} combinations. Expected {expected_combs}. {'PASS' if combinations == expected_combs else 'FAIL'}")
        print(f"Function found {permutations} permutations. Expected {expected_perms}. {'PASS' if permutations == expected_perms else 'FAIL'}")
        print()

test_cases = [
        # Format:
        # (number_of_possible_choices, number_of_choices_to_make, allow_repetitions, expected_combinations, expected_permutations)

        # Test cases with repetitions allowed
        (10, 4, True, 715, 10000),  # A combination lock with four rings, each ring has 10 possible choices (0-9)
        (5, 3, True, 35, 125),   # Three different dice, each with 5 sides (1-5)
        (2, 5, True, 6, 32),   # Five coin tosses, each toss has 2 possible outcomes (heads or tails)
        
        # Test cases with repetitions not allowed
        (6, 2, False, 15, 30),  # Picking 2 balls from a bag containing 6 different colored balls
        (7, 3, False, 35, 210),  # Selecting a committee of 3 members from a group of 7 candidates
        (3, 3, False, 1, 6),  # Filling three positions with three distinct letters (A, B, C)

        # Edge cases
        (0, 0, True, 0, 0),   # Zero possible choices, zero choices to make (repetitions allowed)
        (1, 0, False, 0, 0),  # One possible choice, zero choices to make (repetitions not allowed)
        (10, 10, True, 92378, 10000000000), # Ten possible choices, selecting all ten choices (repetitions allowed)
        (8, 8, False, 1, 40320),  # Eight possible choices, selecting all eight choices (repetitions not allowed)
    ]

run_test_cases(test_cases)
