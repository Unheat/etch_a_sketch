'''
Write a docstring here
Overview of each function:
- `pot2px()`: Maps a potentiometer value (0 to 65535) to a pixel coordinate within a specified range, enabling a scaled conversion for Turtle graphics movement.
  - Parameters:
    - `potvalue`: Integer value from the potentiometer.
    - `min_px_val`: Minimum pixel value for the mapped coordinate range.
    - `max_px_val`: Maximum pixel value for the mapped coordinate range.
  - Returns:
    - A float representing the mapped pixel value between `min_px_val` and `max_px_val`.

- `setup_turtle()`: Creates a Turtle object, sets up the screen dimensions, and returns the Turtle object for drawing.
  - Parameters:
    - `screen_width`: The width of the Turtle screen in pixels.
    - `screen_height`: The height of the Turtle screen in pixels.
  - Returns:
    - A configured Turtle object.

-The main() function is to run program:
    This function sets up the Turtle and continuously update potentiometer 
    inputs to control the Turtle's position on the screen, as well as a button 
    input to toggle drawing (pen up/down).

    Steps:
    1. Sets up the Turtle and screen with a size of 800x800 pixels.
    2. Initializes a connection to the serial port to receive data from the potentiometers 
        and button.
    3. Starts with the pen in the "up" state (not drawing).

    The program then enters an infinite loop where it:
        - Reads three values from the serial input:
        - `x_pot`: Value from the X-axis potentiometer.
        - `y_pot`: Value from the Y-axis potentiometer.
        - `new_pen_state`: Button state (1 for pen down, 0 for pen up).
        - Converts the potentiometer values to pixel coordinates using `pot2px()`, 
        allowing the Turtle to move within the 800x800 screen space.
        - Checks if the button state has changed:
        - If yes, it updates the pen state to either "down" (start drawing) or 
            "up" (stop drawing).
        - Moves the Turtle to the new (x, y) position on the screen.

'''

from turtle import Turtle
from receiver import Receiver    
#import mudule


def pot2px(potvalue, min_px_val, max_px_val):
    """
    maps a potentiometer value to a pixel value, as a float.
    (pixel values are typically ints, but Turtle's goto method
    can take floats)
    Potentiometer values fall between 0 and 65535.
    * When the potentiometer value is 0, the function 
        should return min_px_val.
    * When the potentiometer value is 65535, the 
        function should return max_px_val.
    * If the potentiometer value is somewhere between 0 and 65535, 
    the function should return an float pixel value that is proportionally 
    between min_px_val and max_px_val

    For example:
    * pot2px(0, -400, 400) should return -400.0
        because the potentiometer is at its minimum.
    * pot2px(65535, -400, 400) should return 400.0, 
        because the potentiometer is at its maximum.
    * pot2px(32768, -400, 400) should return a value very close to (within 1.0 px) of 0.0, 
        because 32768 is roughly halfway between 0 and 65535 (rounding up), 
        so it maps close to the midpoint between -400 and 400.

    Inputs:
        * potvalue: the potentiometer reading (int)
        * min_px_val: the minimum pixel value (int)
        * max_px_val: the max pixel value (int)

    Outputs:
        * the pixel value corresponding to the pot reading (float)

    Assumptions: You may assume that potvalue is between 0 and 65535 inclusive.
    You may assume that max_px_val > min_pix_val, and that the difference between
    them is <= 2000, but you should not assume that they are symmetric, or 
    the specific values specified in the test cases (e.g. 
    your function should work for cases other than -400, 400).

    Hint: the test file is provided in testpot2px.py. There is some 
    tolerance there--your outputs will pass if they 
    fall within +/- 1 px of the expected values in the test file.
    """
    portion_potentionmeter = potvalue/65535
    pixel_value = portion_potentionmeter*(max_px_val-min_px_val) - max_px_val 
    #calculate the portion of potentioneter from 0 to 65535. Then, converting it to pixel point 
    #then minus max_px_val as pixel run in from negative pole to positive (not 0 toward positive)
    


    return float(pixel_value) #convert to float


def setup_turtle(screen_width, screen_height):
    """
    creates a turtle object, sets the screen size, and returns the turtle
    Inputs: screen_width--the width of the screen in pixels
            screen_height--the height of the screen in pixels
    Outputs:
        a turtle object, with the screen setup to screen_width and screen_height
    """
    bob = Turtle()
    screen = bob.getscreen()
    screen.setup(screen_width, screen_height)
    return bob

def main():
    """
    You write this
    """
    bob = setup_turtle(800, 800)  #set up turtle oject and 800x800 pixel environment for the turtle to run on 
    rec = Receiver("/dev/tty.usbserial-110")  # determine serial port

    # Initial pen state is up
    pen_state = 0  
    bob.penup()

    while True:
        # Read values from the receiver
        values = rec.read_values(3)  # receiving x, y, and pen_state from "pub.send(x_val, y_val, pen_state)" in control.py
    
        
        
        x_pot, y_pot, new_pen_state = values  # assign 3 value to each

            # Convert potentiometer values to pixel coordinates
        x = pot2px(x_pot, -400, 400) # total pixel is 800x800
        y = pot2px(y_pot, -400, 400)

            # Update pen state if it changed
        if new_pen_state != pen_state:  #check if there is new state of pen (0 or 1)
            pen_state = new_pen_state   # assign new state
            if pen_state == 1:          
                bob.pendown()   # drawing
            else:
                bob.penup()     # not drawing
            
            
        bob.goto(x, y) # Move turtle to new position using provided x-cordinate and y-cordinate from pot2px 



     
    


if __name__=='__main__':  
    main()
