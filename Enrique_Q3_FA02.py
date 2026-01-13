import numpy as np

names = ["Me", "Lia", "Jake"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

for i in range(len(names)):
    print(names[i], steps[i])

print(f"\nJake's steps on Wednesday:", steps[2][2])

steps[0][3] = 5500
print("My updated steps:", steps[0])

lia_average = steps[1].mean()
print("Lia's average steps:", lia_average)