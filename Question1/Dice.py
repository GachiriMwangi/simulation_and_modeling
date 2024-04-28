import random

# Function to roll a die
def roll_die():
    rand_num = random.random()
    if rand_num < 1/6:
        return 1
    elif rand_num < 2/6:
        return 2
    elif rand_num < 3/6:
        return 3
    elif rand_num < 4/6:
        return 4
    elif rand_num < 5/6:
        return 5
    else:
        return 6

# Dictionary to store the frequency of each face
frequency = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Roll the die 1000 times
for _ in range(1000):
    result = roll_die()
    frequency[result] += 1

# Displayin the results in a tabulated form
print("Face\tFrequency\tPercentage")
print("---------------------------------")
for face in frequency:
    percentage = (frequency[face] / 1000) * 100
    print(f"{face}\t{frequency[face]}\t\t{percentage:.1f}%")
