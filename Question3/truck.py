import math
import vehicles
import turtle
import flower as fl
import random

def generate_random_length():
    a = 600
    b = 100
    u = random.random()

    return a + u*(b -a) # Adjust the range as needed

# Function used to generate colors randomly
def gencolors():
    return ((random.random(),random.random(),random.random()))

# Function to draw the truck
def drawtruck():

    # Dimensions of rectangle
    # rec_length = len() # Length of truck is randomly generated
    rec_length = generate_random_length()

    rec_height = rec_length / 2

    # Dimensions of bigger trapezium
    trapezium_top = rec_length / 3
    trapezium_diagonal = -(rec_length / 1.3)

    trapezium_height = rec_length/2.4
    trapezium_length = trapezium_diagonal
    
    # Dimensions of smaller trapezium
    small_trapezium_top = trapezium_top / 1.2
    small_trapezium_bottom = small_trapezium_top * 1.816
    small_trapezium_diagonal = -(trapezium_diagonal / 2.4)

    # Area of rectangle
    rec_area = rec_length * rec_height

    # Dimensions of parallelogram
    seat_height = small_trapezium_diagonal / 3.5
    seat_length = small_trapezium_top / 5

    # Dimensions of tire.
    # Ratio of areas of rectangle and tire is 25.75
    rec_tire_area = rec_area / 20.75
    tire_radius = math.sqrt(rec_tire_area / math.pi)

    # Various coordinates used to draw
    rec_coords= [0,0]
    trapezium_coords = [0,rec_length/2.4]
    small_trapezium_coords = [trapezium_length/13,trapezium_height/1.129]
    seat_1_coords = [(small_trapezium_coords[0]*6.5),small_trapezium_coords[1]*0.386]
    tire_1_coords = [(trapezium_length/2),-(trapezium_height/4)]
    tire_2_coords = [(rec_length/1.141),-(rec_height/4)]


    # Below code for drawing rectangular upper body
    turtle.fillcolor(gencolors())
    turtle.penup()
    turtle.setheading(360)
    turtle.goto(rec_coords[0],rec_coords[1]) # rec_coords
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(rec_length)
    turtle.left(90)
    turtle.forward(rec_height)
    turtle.left(90)
    turtle.forward(rec_length)
    turtle.left(90)
    turtle.forward(rec_height)
    turtle.end_fill()


    # Drawing  trapezium
    turtle.fillcolor(gencolors())
    turtle.penup()
    turtle.setheading(180)
    turtle.goto(trapezium_coords[0],trapezium_coords[1]) # rec_coords
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(trapezium_top)
    turtle.setheading(225)
    turtle.goto(trapezium_diagonal, 0)
    turtle.setheading(360)
    turtle.goto(rec_coords[0],rec_coords[1])
    turtle.end_fill()

    # Drawing  small trapezium
    turtle.fillcolor((1.0, 0.95, 0.85))
    turtle.penup()
    turtle.setheading(180)
    turtle.goto(small_trapezium_coords[0],small_trapezium_coords[1]) # rec_coords
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(small_trapezium_top)
    turtle.setheading(225)
    turtle.forward(small_trapezium_diagonal)
    turtle.setheading(360)
    turtle.fd(small_trapezium_bottom)
    turtle.goto(small_trapezium_coords[0],small_trapezium_coords[1])
    turtle.end_fill()

    # Below code for drawing seat
    turtle.fillcolor((0.83, 0.69, 0.29))
    turtle.setheading(90)
    turtle.penup()
    turtle.goto(seat_1_coords[0],seat_1_coords[1]) # window coords
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(45)
    turtle.forward(seat_height)
    turtle.setheading(360)
    turtle.forward(seat_length)
    turtle.setheading(-135)
    turtle.forward(seat_height)
    turtle.setheading(-180)
    turtle.forward(seat_length)
    turtle.end_fill()


    # Drawing two tires
    turtle.setheading(360)
    turtle.penup()
    turtle.goto(tire_1_coords[0],tire_1_coords[1])
    turtle.pendown()
    turtle.fillcolor((0.0, 0.0, 0.0))
    turtle.begin_fill()
    turtle.circle(tire_radius)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(tire_2_coords[0],tire_2_coords[1])
    turtle.pendown()
    turtle.fillcolor((0.0, 0.0, 0.0))
    turtle.begin_fill()
    turtle.circle(tire_radius)
    turtle.end_fill()

def main():
    fl.main()

    drawtruck()
    
    #Create a Truck object for a used 2002
    #Toyota pickup with 40 000 miles, priced 
    #at $12, 000, with a 4-wheel drive.
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD') 
    
    # Writing the text on screen for details about the BMW
    boldfont=("Times",14, "bold") # Font used for writing on screen
    regfont = ("Times",12, "normal") # Regular font
    turtle.penup()
    turtle.goto(-635,325)
    turtle.right(90)
    turtle.write("USED CAR INVENTORY",font=boldfont)
    turtle.goto(-635,315)
    turtle.write('====================',font=boldfont)
    turtle.goto(-635,305)
    turtle.write('The following truck is in inventory:',font=regfont)
    turtle.goto(-635,285)
    turtle.write('Make:',font=boldfont)
    turtle.goto(-550,285)
    turtle.write(f'{truck.get_make()}',font=regfont)
    turtle.goto(-635,265)
    turtle.write('Model:',font=boldfont)
    turtle.goto(-550,265)
    turtle.write(f'{truck.get_model()}',font=regfont)
    turtle.goto(-635,245)
    turtle.write('Mileage:',font=boldfont)
    turtle.goto(-550,245)
    turtle.write(f'{truck.get_mileage()}',font=regfont)
    turtle.goto(-635,225)
    turtle.write('Price:',font=boldfont)
    turtle.goto(-550,225)
    turtle.write(f'{truck.get_price()}',font=regfont)
    turtle.goto(-635,205)
    turtle.write('Drive type:',font=boldfont)
    turtle.goto(-540,205)
    turtle.write(f'{truck.get_drive_type()}',font=regfont)
    turtle.done()

    # print('USED CAR INVENTORY')
    # print('=====================')
    # #Display the truck's data.
    # print('The following truck is in inventory:')
    # print('Make:', truck.get_make())
    # print('Model:', truck.get_model())
    # print('Mileage:', truck.get_mileage())
    # print('Price:', truck.get_price())
    # print('Drive type:', truck.get_drive_type())
    # print()

#Call the main function
# main()
    