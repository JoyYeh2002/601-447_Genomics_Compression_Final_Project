import matplotlib.pyplot as plt

k_values = [20, 17, 15, 13, 10, 7, 5, 3]
true_reference_sizes = [4101354, 4058103, 4028245, 3983556, 4082246, 4514315, 4448777, 4229516]
de_novo_reference_sizes = [4971299, 4978661, 4979084, 4989019, 5051944, 5748357, 5596283, 5274602]

plt.figure(figsize=(12, 8))
bar_width = 0.8

bars1 = plt.bar([k - bar_width / 2 for k in k_values], true_reference_sizes, bar_width, label='True Reference')
bars2 = plt.bar([k + bar_width / 2 for k in k_values], de_novo_reference_sizes, bar_width, label='De Novo Reference (shorter)')

plt.xlabel('Length of Hash Map tuple (k)')
plt.ylabel('Compressed Archive Size (bytes)')
plt.ylim([3e6, 6e6])
plt.title('SARS-COVID 19 Compressed Archive File Sizes across k-values')
plt.xticks(k_values)
plt.legend()

# Labeling the numbers on top of the bars
for bar1, bar2 in zip(bars1, bars2):
    plt.text(bar1.get_x() + bar1.get_width() / 2, bar1.get_height(), str(bar1.get_height()), ha='center', va='bottom')
    plt.text(bar2.get_x() + bar2.get_width() / 2, bar2.get_height(), str(bar2.get_height()), ha='center', va='bottom')

plt.show()
