import turtle
import time
import random

WIDTH, HEIGHT = 700, 500 # Constant Values therefore Capital Letters
COLOURS = ['red', 'green', 'blue', 'orange', 'yellow', 'pink', 'purple', 'black', 'brown', 'cyan']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric... Try Again!')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10. Please try again")

def race(colours):
    turtles = create_turtles(colours)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colours[turtles.index(racer)] # gives index of turtle object in turtle list and uses that index to find out the colour of the turtle in the colours list

def create_turtles(colours):
    turtles = []
    spacingx = WIDTH // (len(colours) + 1)
    for i, colour in enumerate(colours):
        racer = turtle.Turtle()
        racer.color(colour)
        racer.shape('turtle')
        racer.left(90) # sets orientation of turtle to face up
        racer.penup() # tracer lines won't follow turtle
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20 ) # (i+1 so that the first turle position isn't placed at the edge of the canvas)
        racer.pendown() # tracer lines will follow turtle
        turtles.append(racer)

    return turtles



def init_turtle():
    screen = turtle.Screen() # Initialises Screen
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLOURS)
colours = COLOURS[:racers]

winner = race(colours)
print(winner)
print("The winner is the turtle with the colour:", winner)
time.sleep(5)
