import math

def calculate_sin(degrees):
    radians = math.radians(degrees)
    return math.sin(radians)

limit = int(input("How many times to calculate: "))

for i in range(1, limit+1):
    print(f'\nSet {i}')
    angel = float(input("Enter the angel: "))
    sin_value = calculate_sin(angel)
    s_v = f'{sin_value:.4f}'
    print(f'The Sin value of {angel}° is {s_v}')