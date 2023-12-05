# EN.601.447 Computational Genomics: Sequences
# Joy Yeh
# Step01: Load an .fna file and display text
# Updated 12/02/2023

import os
import pickle

# 1. Laod file

# Specify the path to target FASTA file
data_path = 'C:/Users/joy20/Folder/FA_2023/601-447_Genomics/601-447_Computational_Genomics/Final_Project/data/'
target_file = data_path + "chr10.fna"
ref_file = data_path + "chrY.fna"
pickle_file_path = data_path + 'pair.pickle'

# Helper: load the .fna files and return about 200 lines
def load_fna_file_content(file_name, line_idx_start, line_idx_end):
    with open(file_name) as f:
        lines = f.readlines()
    info = lines[0]
    content_subset = lines[line_idx_start:line_idx_end]
    f.close();

    return info, content_subset


target_info, target_subset = load_fna_file_content(target_file, 126, 326)
ref_info, ref_subset = load_fna_file_content(ref_file, 126, 326)


# Specify the path to your pickle file
with open(pickle_file_path, 'wb') as pickle_file:
    pickle.dump(target_info, pickle_file)
    pickle.dump(target_subset, pickle_file)
    pickle.dump(ref_info, pickle_file)
    pickle.dump(ref_subset, pickle_file)


