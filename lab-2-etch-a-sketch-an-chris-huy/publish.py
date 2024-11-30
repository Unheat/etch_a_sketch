'''
A program that runs on the Pico, reads the potentiometers,
and publishes their values over USB
'''

from picozero import Pot, Publisher 
from picozero import sleep
left_pot = Pot(27)  # Assuming GP27
right_pot = Pot(28) # Assuming GP28
pen_button = Button(15)  # Assuming GP15 for the button

# Setup publisher for sending data
pub = Publisher()

# Flag for pen state
pen_state = 0  # Start with pen up

while True:
    # Read potentiometer positions
    x_val = left_pot.read_position()
    y_val = right_pot.read_position()
    
    # Check if button was pressed to toggle pen state
    if pen_button.is_pressed:
        pen_state = 1 - pen_state  # Toggle between 0 and 1
        sleep(0.2)  # Debounce delay to avoid multiple toggles per press
    
    # Send x, y, and pen state to the laptop
    pub.send(x_val, y_val, pen_state)
    
    sleep(0.1)  # Send updates every 0.1 seconds
