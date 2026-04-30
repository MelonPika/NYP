import random

height = random.randint(1, 199)
height_m = height // 100        # retires an integer
height_cm = height % 100        # modulus or remainder operator
print(f'{height}cm is {height_m}m and {height_cm}cm.')


'''
2/1 --> 2.0 (division will returen a float)
'''