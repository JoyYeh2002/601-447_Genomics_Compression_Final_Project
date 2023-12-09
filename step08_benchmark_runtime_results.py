import matplotlib.pyplot as plt

k_values = [20, 17, 15, 13, 10, 7, 5, 3]
true_reference_timers = [0.238438, 0.250855, 0.225368, 0.178706, 0.196066, 0.217290, 0.222972, 0.341166]
de_novo_reference_timers = [0.271383, 0.275554, 0.272780, 0.192409, 0.212978, 0.227403, 0.265550, 0.704068]

plt.figure(figsize=(12, 8))
bar_width = 0.7

bars1 = plt.bar([k - bar_width / 2 for k in k_values], true_reference_timers, bar_width, color='green',label='True Reference')
bars2 = plt.bar([k + bar_width / 2 for k in k_values], de_novo_reference_timers, bar_width, color='purple',label='De Novo Reference (shorter)')

plt.xlabel('Length of Hash Map tuple (k)')
plt.ylabel('Total Compression Timer (minutes)')
plt.title('Total Compression Timer for Different k-values')
plt.xticks(k_values)
plt.legend()

# Adding data values on top of the bars
for bar1, bar2 in zip(bars1, bars2):
    plt.text(bar1.get_x() + bar1.get_width() / 2, bar1.get_height(), f'{bar1.get_height():.3f}', ha='center', va='bottom')
    plt.text(bar2.get_x() + bar2.get_width() / 2, bar2.get_height(), f'{bar2.get_height():.3f}', ha='center', va='bottom')
    plt.text(bar1.get_x() + bar1.get_width() / 2, bar1.get_height(), f'{bar1.get_height():.3f}', ha='center', va='bottom')
    plt.text(bar2.get_x() + bar2.get_width() / 2, bar2.get_height(), f'{bar2.get_height():.3f}', ha='center', va='bottom')

plt.show()
