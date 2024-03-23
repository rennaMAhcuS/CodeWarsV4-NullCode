from itertools import permutations

def calculate_midpoints(sequence):
    midpoints = [(sequence[i] + sequence[i + 1]) / 2 for i in range(0, len(sequence) - 1, 2)]
    return midpoints

def permutation_midpoint_mapping(n):
    initial_sequence = list(range(1, n + 1))
    all_permutations = list(permutations(initial_sequence))
    midpoint_mappings = []

    for perm in all_permutations:
        sequence = list(perm)
        while len(sequence) > 1:
            sequence = calculate_midpoints(sequence)
            midpoint_mappings.append(sequence)

    return midpoint_mappings

# Example usage
n = 3
result = permutation_midpoint_mapping(n)
print("Midpoint mappings for permutations:", result)
