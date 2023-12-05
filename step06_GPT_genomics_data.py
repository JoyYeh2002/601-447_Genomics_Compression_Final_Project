# EN.601.447 Computational Genomics: Sequences
# Joy Yeh
# Step06: Create a genomics data, then add some small variations at %
#
# Updated 12/05/2023

import random

# Helper: Function to generate a random DNA sequence of length n
def generate_random_sequence(length):
    return ''.join(random.choice('ACGT') for _ in range(length))

# Helper: Create a {percentage} mutated list in .fna format
def generate_mutated_list(original_list, percentage):
    # Function to randomly mutate a given character
    def mutate_character(char):
        return random.choice('ACGT'.replace(char, ''))

    # Function to mutate a given string with the specified percentage
    def mutate_string(original_string, mutation_percentage):
        mutation_count = int(len(original_string) * mutation_percentage)
        mutation_indices = random.sample(range(len(original_string)), mutation_count)
        mutated_string = list(original_string)

        for index in mutation_indices:
            mutated_string[index] = mutate_character(original_string[index])

        return ''.join(mutated_string)

    # Generate mutated list
    mutated_list = [mutate_string(original, percentage) for original in original_list]
    return mutated_list



# Create a list of 10 elements, each being a random sequence of length 81
string_list = [generate_random_sequence(81) for _ in range(10)]
percentage = 0.1
mutated_list = generate_mutated_list(string_list, percentage)
