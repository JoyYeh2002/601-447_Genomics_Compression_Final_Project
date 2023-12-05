# EN.601.447 Computational Genomics: Sequences
# Joy Yeh
# Step05: I define some strings, and observe the intermediate compressed outputs
# CAUTION: No need for pickles in this case, since we're not using large, raw .fna files
# Updated 12/05/2023

import os
import pickle
import step03_file_comparison_report as visual
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

def create_fna_file(input_string, long_strings, file_name='output.fna'):
    # Concatenate the input string and the long strings with newline characters
    final_string = input_string + ''.join(long_strings)
    with open(file_name, 'w') as fna_file:
        fna_file.write(final_string)

    print(f'File "{file_name}" created successfully.')
    
def old_generate_small_content():
    t_content = 'TAGTCCGATTTA\nNNNNNNNNNNNN\nAAATAGTCCGAT\nTTTTTTTTTTTT'
    r_content = 'AAACCCGGGAAA\nNNNNNNNNNNNN\nAAAAAAAAAAAA\nTAGTCCGATTTA'

    # Split strings into contents with 3 elements each
    t_content = t_content.split('\n')
    r_content = r_content.split('\n')

    # Filter out empty strings
    t_content = [element for element in t_content if element]
    r_content = [element for element in r_content if element]
    
    return t_content, r_content


if __name__ == "__main__":
    # 0. Define file paths
    data_path = 'C:/Users/joy20/Folder/FA_2023/601-447_Genomics/601-447_Computational_Genomics/Final_Project/data/'
    data_path_hirgc = 'C:/Users/joy20/Folder/FA_2023/601-447_Genomics/601-447_Computational_Genomics/Final_Project/HiRGC/'
   
    percentage = 0.1
    
    # 1. Define the content (exact match)
    t_info = 'my target with ' + str(percentage) + ' mutations\n'
    r_info = 'my ref with 10 lines\n'
    
    r_content = [generate_random_sequence(81) for _ in range(10)]
    t_content = generate_mutated_list(r_content, percentage)
    
    # 2. Save to the smaller .fna, at my path and the HiRGC default path
    prefix = 'my_GPT_10'
    create_fna_file(t_info, t_content, data_path + prefix + '_tar.fna')
    create_fna_file(r_info, r_content, data_path + prefix + '_ref.fna')

    create_fna_file(t_info, t_content, data_path_hirgc + prefix + '_tar.fna')
    create_fna_file(r_info, r_content, data_path_hirgc + prefix + '_ref.fna')

    # 3. Generate html report
    out_html_name = prefix + '_tar_ref_exact_match_comparisons.html'
    visual.generate_html_report_from_vars(data_path, t_info, t_content, \
                        r_info, r_content, out_html_name)





