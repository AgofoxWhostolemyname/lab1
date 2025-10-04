import os
import time

COLOR_PREFIX = '\u001b[48;5;'
WHITE_CODE = 15
RESET = '\u001b[0m'

def draw_flag(blue=27):
    leftside = 5 * 3
    middle = 8
    rightside = 10 * 3
    length = 53
    
    for i in range(11):
        if i < 4:
            left = f'{COLOR_PREFIX}{WHITE_CODE}m{" " * leftside}'
            mid = f'{COLOR_PREFIX}{blue}m{" " * middle}'
            right = f'{COLOR_PREFIX}{WHITE_CODE}m{" " * rightside}'
            print(f'{left}{mid}{right}{RESET}')
        elif 4 <= i <= 6:
            print(f'{COLOR_PREFIX}{blue}m{" " * length}{RESET}')
        else:
            left = f'{COLOR_PREFIX}{WHITE_CODE}m{" " * leftside}'
            mid = f'{COLOR_PREFIX}{blue}m{" " * middle}'
            right = f'{COLOR_PREFIX}{WHITE_CODE}m{" " * rightside}'
            print(f'{left}{mid}{right}{RESET}')

time.sleep(1)
for frame in range(10):
    os.system('cls')
    
    intensity = 27 + (frame % 3) * 10 
    
    draw_flag(blue=intensity)
    time.sleep(0.4)

os.system('cls')
draw_flag()
print("Оригинальный флаг Финляндии")