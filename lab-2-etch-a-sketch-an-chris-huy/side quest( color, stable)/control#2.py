'''
A program that reads inputs from the Pico as
controls for an etch-a-sketch running on a laptop.
It sends those controls over USB to the etch-a-sketch
program to control a turtle.
'''
# some useful imports, feel free to modify
from picozero import Pot, Button, Publisher
from time import sleep

# Setup potentiometers and button
left_pot = Pot(27)  # Assuming GP27
right_pot = Pot(28) # Assuming GP28
pen_button = Button(15)  # Assuming GP15 for the button
color_button = Button(14) # GP14

# Setup publisher for sending data
pub = Publisher()

# Flag for pen state
pen_state = 0  # Start with pen up
color_state = 0  # Start with no pressing color button

def read_send_position():# Send x, y, and pen state to the laptop, this function is for less code and increase readibility
    x_val = left_pot.read_position()
    y_val = right_pot.read_position()
    pub.send(x_val, y_val, pen_state, color_state)
    return


while True:
    # Read potentiometer positions
    read_send_position()
    
    # Check if button was pressed to toggle pen state
    if pen_button.is_pressed:
        while pen_button.is_pressed: #hold until the button is released ( to void turn up and down pen countinueously when holding the button)
            sleep(0.1)   
            read_send_position() #the reason why I add this line here is because when I hold my button, the whole program just freeze
                                 #and wait for me to realease it(as it stuck in the loop). I want it still send position data even when I hold the button
        pen_state = 1 - pen_state # Toggle between 0 and 1/ if on 1 -1 = 0/ if off 1 - 0 = 1
    if color_button.is_pressed:
        while color_button.is_pressed:
            sleep(0.1)
            read_send_position()    
        color_state = 1 - color_state
          

            
        
    
    
    sleep(0.1) #avoid loop too fast


