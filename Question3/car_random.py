import turtle
import random
from flower import *

# Function to generate random length for the car
def generate_random_length():
    return random.randint(100, 200)  # Adjust the range as needed

# Function to draw the Car
def drawcar():
    # Generate random length for the car
    rec_length = generate_random_length()

    # Rest of the drawing code...

def main():
    turtle.speed(1)  # Adjust the speed as needed
    drawcar()
    # Details about the car...
    turtle.done()

main()
