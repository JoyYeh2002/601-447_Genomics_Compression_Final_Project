# EN.601.447 Computational Genomics: Sequences
# Joy Yeh
# Step04: Load in the Pickle file (with a smaller array) and save to an .fna
# Updated 12/05/2023

import pickle

def create_fna_file(input_string, long_strings, file_name='output.fna'):
    # Concatenate the input string and the long strings with newline characters
    final_string = input_string + ''.join(long_strings)

    # Save the concatenated string to an .fna file
    with open(file_name, 'w') as fna_file:
        fna_file.write(final_string)

    print(f'File "{file_name}" created successfully.')

if __name__ == "__main__":

    # Specify the path to target FASTA file
    data_path = 'C:/Users/joy20/Folder/FA_2023/601-447_Genomics/601-447_Computational_Genomics/Final_Project/data/'
    data_path_hirgc = 'C:/Users/joy20/Folder/FA_2023/601-447_Genomics/601-447_Computational_Genomics/Final_Project/HiRGC/'
    pickle_file_path = data_path + "pair.pickle"

    # Obtain the contents char array
    with open(pickle_file_path, 'rb') as f:
        t_info = pickle.load(f)
        t_content = pickle.load(f)
        r_info = pickle.load(f)
        r_content = pickle.load(f)

    # Save it to my path for Python testing
    create_fna_file(t_info, t_content, data_path + 'small_chr10.fna')
    create_fna_file(r_info, r_content, data_path + 'small_chrY.fna')
    
    # Save it to the HiRGC path 
    create_fna_file(t_info, t_content, data_path_hirgc + 'small_chr10.fna')
    create_fna_file(r_info, r_content, data_path_hirgc + 'small_chrY.fna')



    