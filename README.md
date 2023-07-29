# Combinatrix
 Derive possible combinations and permutations


# Combinatrix

## Overview

Combinatrix is a Python library that provides functions for calculating permutations and combinations of choosing items from a given set of possible choices. It is particularly useful in scenarios where you need to count the number of ways to arrange or select elements from a set. The library contains a single function called `calc_permutations_combinations`, which takes the number of possible choices, the number of choices to make, and an optional flag to allow repetitions, and returns the number of combinations and permutations.

## Installation

To use Combinatrix, simply copy the `combinatrix.py` file into your project directory or any location accessible by your Python environment.

## Function: `calc_permutations_combinations`

### Signature

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

## Test Cases

The library includes a set of test cases to verify the correctness of the `calc_permutations_combinations` function. These test cases cover various scenarios, including edge cases. The function is tested with both combinations and permutations calculations, with and without repetitions.

## Example Usage

```python
import combinatrix

# Calculate combinations and permutations with repetitions allowed
combinations, permutations = combinatrix.calc_permutations_combinations(10, 4, True)
print(f"Combinations: {combinations}, Permutations: {permutations}")

# Calculate combinations and permutations without repetitions
combinations, permutations = combinatrix.calc_permutations_combinations(6, 2, False)
print(f"Combinations: {combinations}, Permutations: {permutations}")
```

The above code will output:

```
Combinations: 715, Permutations: 10000
Combinations: 15, Permutations: 30
```

## License

Combinatrix is distributed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

Combinatrix is authored by Adill Al-Ashgar.

## Contributions

Contributions to Combinatrix are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or a pull request on the [GitHub repository](https://github.com/username/repo).

---
With Combinatrix, you can now effortlessly calculate the number of ways to arrange or select items from a set of choices in your Python projects. Happy coding!