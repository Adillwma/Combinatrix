# Combinatrix

## Overview
With Combinatrix, you can now effortlessly calculate the number of ways to arrange or select items from a set of choices in your Python projects. Combinatrix is a simple Python library that provides functions to calculate the number of permutations and combinations of a set of items. The library is useful in various scenarios, including probability, statistics, and cryptography.

Combinatrix contains a single function called `calc_permutations_combinations`, which takes the number of possible choices, the number of choices to make, and an optional flag to allow repetitions, and returns the number of combinations and permutations.

## Function: `calc_permutations_combinations`
```python
def calc_permutations_combinations(number_of_possible_choices, number_of_choices_to_make, allow_repetitions=True)
```

### Parameters

- `number_of_possible_choices` (int): Total number of possible choices.
- `number_of_choices_to_make` (int): Number of choices to make.
- `allow_repetitions` (bool, optional): If `True`, repetition of a choice is allowed. Defaults to `True`.

### Returns

(tuple): A tuple containing two integers - (combinations, permutations).


## Permutations and Combinations

### Permutations

A permutation is an arrangement of items in a specific order. In the context of Combinatrix, a permutation represents the number of ways we can select `r` items from a set of `n` items when repetitions are not allowed. The formula to calculate permutations is:

```
nPr = n! / (n - r)!
```

where `n` is the total number of items, `r` is the number of items to select, and `!` represents the factorial function.

### Combinations

A combination, on the other hand, represents the number of ways we can select `r` items from a set of `n` items when repetitions are allowed. The formula to calculate combinations is:

```
nCr = (n + r - 1)! / (r! * (n - 1)!)
```

where `n` is the total number of items, `r` is the number of items to select, and `!` represents the factorial function.




# Combinatorics: Combinations and Permutations
Combinatorics is a branch of mathematics that deals with the study of discrete structures and the enumeration of arrangements and selections. Combinatorics is concerned with counting and arranging objects or events. It has applications in computer science, cryptography, probability, statistics, and various other areas. This code focuses on two fundamental priciples in combinatorics: combinations and permutations.

**2. Combinations:**
Combinations refer to the selection of items from a set without considering the order. The number of combinations of `k` objects chosen from a set of `n` distinct objects is denoted by C(n, k) or "n choose k."

**2.1. Combinations Equation:**
The formula for combinations is given by:
```
C(n, k) = n! / (k! * (n - k)!)
```
where:
- `n!` is the factorial of `n`, i.e., the product of all positive integers from 1 to `n`.
- `k!` is the factorial of `k`.
- `(n - k)!` is the factorial of the difference between `n` and `k`.

**3. Permutations:**
Permutations refer to the arrangement of items from a set in a specific order. The number of permutations of `k` objects chosen from a set of `n` distinct objects is denoted by P(n, k) or "n P k" or "nPk."

![Permutations](Images/4-digit_combination_padlock.jpg)

**3.1. Permutations Equation:**
The formula for permutations is given by:
```
P(n, k) = n! / (n - k)!
```
where:
- `n!` is the factorial of `n`.
- `(n - k)!` is the factorial of the difference between `n` and `k`.

**4. Relationship between Combinations and Permutations:**
The relationship between combinations and permutations can be expressed as follows:
```
P(n, k) = k! * C(n, k) 
```
This relationship shows that permutations can be obtained by multiplying combinations with `k!`.

**5. Applications of Combinatorics:**
Combinatorics plays a crucial role in computing probabilities of events and handling discrete probability distributions. Combinatorial techniques are used in designing cryptographic algorithms, generating secure keys, and analyzing cryptographic systems' properties. In network theory, combinatorics helps in analyzing connectivity, paths, and cycles in graphs.


















## Test Cases
The library includes a set of test cases to verify the correctness of the `calc_permutations_combinations` function. These test cases cover various scenarios, including edge cases. The function is tested with both combinations and permutations calculations, with and without repetitions.


## License
Combinatrix is distributed under the MIT License. See the [LICENSE](LICENSE) file for more details.


## Contributions

Contributions to Combinatrix are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or a pull request on the [GitHub repository](https://github.com/adillwma/combinatrix).

---
