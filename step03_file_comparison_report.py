# EN.601.447 Computational Genomics: Sequences
# Joy Yeh
# Step03: Implement the HTML report from Pickle file
# Updated 12/05/2023

import pickle

def file_comparison(file1_array, file2_array):
    index_to_highlight = []
    shorter = min(len(file1_array), len(file2_array))
    longer = len(file2_array) if shorter == len(file1_array) else len(file1_array)
    
    for i in range (shorter):
        if (file1_array[i] != file2_array[i]):
            index_to_highlight.append(i)
    
    for i in range (shorter, longer):
        index_to_highlight.append(i)
        
    return index_to_highlight
    
def generate_report(file1_name, file1_lines, file2_name, file2_lines, differences):
    lines_with_highlight_file1 = add_line_numbers_with_highlight(file1_lines, file2_lines, differences)
    lines_with_highlight_file2 = add_line_numbers_with_highlight(file2_lines, file1_lines, differences)

    html_code = f'''
    <html>
    <head>
        <title>File Comparison</title>
        <style>
            .container {{
                display: flex;
            }}
            .file {{
                flex: 1;
                padding: 10px;
                border: 1px solid #ccc;
            }}
            .file h2 {{
                text-align: center;
                font-size: 18px;
            }}
            .file pre {{
                white-space: pre-wrap;
            }}
            .file .difference {{
                background-color: yellow;
            }}
            .file-name-box {{
                text-align: center;
                padding: 5px;
                background-color: #f0f0f0;
                border: 1px solid #ccc;
            }}
            .footer {{
                text-align: center;
                margin-top: 20px;
            }}
            h1 {{
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <h1>File Comparison</h1>
        <div class="footer">
            <p>Number of differences: {len(differences)}</p>
        </div>
        <div class="container">
            <div class="file">
                <div class="file-name-box">
                    <h2>{file1_name}</h2>
                </div>
                <pre>{lines_with_highlight_file1}</pre>
            </div>
            <div class="file">
                <div class="file-name-box">
                    <h2>{file2_name}</h2>
                </div>
                <pre>{lines_with_highlight_file2}</pre>
            </div>
        </div>
        
    </body>
    </html>
    '''

    return html_code

def get_difference_index(line1,line2):
    result = []
    shorter = min(len(line1), len(line2))
    longer = len(line2) if shorter == len(line1) else len(line1)
    
    for i in range(shorter):
        if line1[i] != line2[i]:
            result.append(i)
            
    for i in range(shorter,longer):
        result.append(i)
    return result

def listToString(s):
    str = ""
    for ele in s:
        str += ele
    return str

def add_line_numbers_with_highlight(lines1, lines2, differences):
    lines_with_highlight = []
    count = -1
    for i, line in enumerate(lines1, start=1):
        count = count + 1
        if i == len(lines2) + 1:
            break
        if i - 1 in differences:
            temp = []
            index_to_highlight = get_difference_index(line, lines2[i - 1])
            for j, char in enumerate(line, start = 0):
                if j in index_to_highlight:
                    temp.append('<span class="difference">{}</span>'.format(char)) 
                else:
                    temp.append(char)     
            lines_with_highlight.append('{:>4}: {}'.format(i, listToString(temp)))
        else:
            lines_with_highlight.append('{:>4}: {}'.format(i, line))
    
    temp = lines1 if len(lines1) > len(lines2) else []
    for i in range(count, len(temp)):
        cur = '<span class="difference">{}</span>'.format(temp[i])
        lines_with_highlight.append('{:>4}: {}'.format(i + 1, cur))
    
    return '\n'.join(lines_with_highlight)


def generate_html_report_from_pickle(data_path, pickle_path, output_html_name):
    # Obtain the contents char array
    with open(pickle_path, 'rb') as f:
        t_info = pickle.load(f)
        t_content = pickle.load(f)
        r_info = pickle.load(f)
        r_content = pickle.load(f)

    differences = file_comparison(t_content, r_content)
    html_code = generate_report(t_info, t_content, r_info, r_content, differences)
    
    with open(data_path + output_html_name, 'w') as file:
        file.write(html_code)

    print(f'File "{output_html_name}" created successfully.')


def generate_html_report_from_vars(data_path, t_info, t_content, r_info, r_content, output_html_name):
    differences = file_comparison(t_content, r_content)
    html_code = generate_report(t_info, t_content, r_info, r_content, differences)
    
    with open(data_path + output_html_name, 'w') as file:
        file.write(html_code)

    print(f'File "{output_html_name}" created successfully.')


if __name__ == "__main__":
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
        
    data_path = 'C:/Users/joy20/Folder/FA_2023/601-447_Genomics/601-447_Computational_Genomics/Final_Project/data/'
    target_file = "target_sample.txt"
    ref_file = "ref_sample.txt"
  
    differences = file_comparison(t_content, r_content)
    html_code = generate_html_report(t_info, t_content, r_info, r_content, differences)
    
    with open(data_path + 'FASTA_sample_comparison_report02.html', 'w') as file:
        file.write(html_code)
