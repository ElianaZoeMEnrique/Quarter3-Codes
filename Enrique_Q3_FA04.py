import numpy as np

names = ["Me", "Lia", "Jake"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

total_steps = steps.sum(axis=1)

max_index = np.argmax(total_steps)
min_index = np.argmin(total_steps)

for i in range(len(names)):
    print(f"{names[i]} - Total Steps: {total_steps[i]} steps")

print(f"\nHighest total steps: {names[max_index]} with {total_steps[max_index]} steps in total")

difference = total_steps[max_index] - total_steps[min_index]
print(f"Difference between the highest and lowest total: {difference} steps")
