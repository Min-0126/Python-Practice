import random

# end change the newline character to a different string
# It means it doesn't change the line
# Flip coin 100 times, if 0 print H else 1 print T
for i in range(100):
    if random.radnint(0, 1) == 0:
        print('H', end='')
    else:
        print('T', end='')

print()