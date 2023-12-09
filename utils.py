# import re

# f1 = open('SARS-COV-19.fasta', 'r')
# f2 = open('SARS-COV-19-processed.fasta', 'w')

# for line in f1.readlines():
#     if not line.startswith('>'):
#         f2.write(line)
# f1.close()
# f2.close()

# Read content from the input file
with open("SARS-COV-19-ref-denovo-shortest.fasta", 'r') as file:
    long_string = file.read()

# Break the long string into multiple lines
max_line_length = 70
broken_lines = [long_string[i:i + max_line_length] for i in range(0, len(long_string), max_line_length)]
formatted_content = '\n'.join(broken_lines)

# Write the modified content back to the output file
with open("SARS-COV-19-ref-denovo-shortest copy.fasta", 'w') as file:
    file.write(formatted_content)