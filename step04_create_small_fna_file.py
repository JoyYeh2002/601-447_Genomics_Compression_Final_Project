# EN.601.447 Computational Genomics: Sequences
# Joy Yeh
# Step04: Full workflow from .fna -> get the smaller sequences in text -> 
# save to Pickle -> save to smaller .fna

# Updated 12/05/2023

import os
import pickle
import step03_file_comparison_report as visual

# Helper: load the .fna files and return about 200 lines
def load_fna_file_content(file_name, line_idx_start, line_idx_end):
    with open(file_name) as f:
        lines = f.readlines()
    info = lines[0]
    content_subset = lines[line_idx_start:line_idx_end]
    f.close()
    return info, content_subset

def create_fna_file(input_string, long_strings, file_name='output.fna'):
    # Concatenate the input string and the long strings with newline characters
    final_string = input_string + ''.join(long_strings)

    # Save the concatenated string to an .fna file
    with open(file_name, 'w') as fna_file:
        fna_file.write(final_string)

    print(f'File "{file_name}" created successfully.')

if __name__ == "__main__":
    # 1. Get a smaller subset of file
    data_path = 'C:/Users/joy20/Folder/FA_2023/601-447_Genomics/601-447_Computational_Genomics/Final_Project/data/'
    data_path_hirgc = 'C:/Users/joy20/Folder/FA_2023/601-447_Genomics/601-447_Computational_Genomics/Final_Project/HiRGC/'
   
    target_file = data_path + "chr10.fna"
    ref_file = data_path + "chrY.fna"
    pickle_file_path = data_path + 'pair_len10.pickle'

    target_info, target_subset = load_fna_file_content(target_file, 126, 128)
    ref_info, ref_subset = load_fna_file_content(ref_file, 126, 128)

    # Specify the path to your pickle file
    with open(pickle_file_path, 'wb') as pickle_file:
        pickle.dump(target_info, pickle_file)
        pickle.dump(target_subset, pickle_file)
        pickle.dump(ref_info, pickle_file)
        pickle.dump(ref_subset, pickle_file)

    # 2. Use the Pickle from now on
    with open(pickle_file_path, 'rb') as f:
        t_info = pickle.load(f)
        t_content = pickle.load(f)
        r_info = pickle.load(f)
        r_content = pickle.load(f)

    # 3. Save to the smaller .fna
    prefix = 'tiny'
    create_fna_file(t_info, t_content, data_path + prefix + '_chr10.fna')
    create_fna_file(r_info, r_content, data_path + prefix + '_chrY.fna')
    
    # Save it to the HiRGC path 
    create_fna_file(t_info, t_content, data_path_hirgc + prefix + '_chr10.fna')
    create_fna_file(r_info, r_content, data_path_hirgc + prefix + '_chrY.fna')

    # 4. Generate html report
    out_html_name = prefix + '_chr10_chry_comparisons.html'
    visual.generate_html_report_from_pickle(data_path, pickle_file_path, out_html_name)







