import numpy as np

names = ["Me", "Lia", "Jake"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

total_per_day = steps.sum(axis=0)

for i in range(len(days)):
    print(f"{days[i]} - Total Steps: {total_per_day[i]} steps")

most_active_day = np.argmax(total_per_day)

print(f"\nMost active day overall: {days[most_active_day]} with {total_per_day[most_active_day]} steps in total")