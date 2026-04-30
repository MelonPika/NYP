import random

height = random.randint(1, 199)
height_m = height / 100
height_cm = height % 100
print(f'{height}cm is {height_m}m and {height_cm}cm.')