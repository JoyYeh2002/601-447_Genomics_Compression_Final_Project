# EN.601.447 Computational Genomics: Sequences
# Joy Yeh
# Step02: Load in the Pickle file and implement lossless
# Updated 12/02/2023

import pickle

# Load the character array from the pickle file
# Specify the path to target FASTA file
data_path = 'C:/Users/joy20/Folder/FA_2023/601-447_Genomics/601-447_Computational_Genomics/Final_Project/data/'
AAA_target_file = data_path + "chr10.fna"
AAA_ref_file = data_path + "chrY.fna"
AAA_pickle_file_path = data_path + "pair.pickle"


# Obtain the contents char array
with open(AAA_pickle_file_path, 'rb') as pickle_file:
    t_info = pickle.load(pickle_file)
    t_content = pickle.load(pickle_file)
    r_info = pickle.load(pickle_file)
    r_content = pickle.load(pickle_file)


# Char array sizes are 200 for taret and reference
# Find all the differences
