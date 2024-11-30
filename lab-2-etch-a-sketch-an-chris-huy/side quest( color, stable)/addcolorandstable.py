'''
Write a docstring here
pot2x function purpose is to 
'''

from turtle import Turtle
from receiver import Receiver

def pot2px(potvalue, min_px_val, max_px_val):
    """
    Maps a potentiometer value to a pixel value, as a float.
    Potentiometer values fall between 0 and 65535.
    * When the potentiometer value is 0, the function 
      should return min_px_val.
    * When the potentiometer value is 65535, the 
      function should return max_px_val.
    * If the potentiometer value is somewhere between 0 and 65535, 
      the function should return a float pixel value that is proportionally 
      between min_px_val and max_px_val.
    """
    portion_potentiometer = potvalue / 65535
    pixel_value = min_px_val + portion_potentiometer * (max_px_val - min_px_val)
    return float(pixel_value)

def setup_turtle(screen_width, screen_height):
    """
    Creates a turtle object, sets the screen size, and returns the turtle.
    """
    bob = Turtle()
    screen = bob.getscreen()
    screen.setup(screen_width, screen_height)
    return bob

def change_color(bob, n):
    """
    Changes the color of the turtle based on the index provided.
    """
    list_color = ["black", "red", "green", "blue", "purple"]
    bob.color(list_color[n])

class Stabilizer:
    def __init__(self, size=5, threshold=2): #threshold is the fluctuate range that keep 1 value if the turtle shaky like (207,208,206,205,...) -> make every data = 207 as it is inital value 
        """
        Initializes the stabilizer with a moving average filter and dead zone threshold.
        :param size: Number of values for moving average (higher means more smoothing).
        :param threshold: Minimum change in value to update position.
        """
        self.size = size
        self.threshold = threshold
        self.x_values = []
        self.y_values = []
        self.last_x = None
        self.last_y = None

    def stable_value(self, new_value, values_list):
        """
        Updates and returns the smoothed value using a moving average.
        """
        values_list.append(new_value)
        if len(values_list) > self.size:
            values_list.pop(0)  # Keep only the most recent 'size' values
        return sum(values_list) / len(values_list)

    def get_stable_position(self, x_pot, y_pot, min_px, max_px):
        """
        Returns the stabilized x and y position for the turtle.
        """
        # Smooth values using moving average
        x_smoothed = self.stable_value(x_pot, self.x_values)
        y_smoothed = self.stable_value(y_pot, self.y_values)

        # Map potentiometer values to pixel coordinates
        x_px = pot2px(x_smoothed, min_px, max_px)
        y_px = pot2px(y_smoothed, min_px, max_px)

        # Dead zone filtering to reduce jitter
        if self.last_x is None or abs(x_px - self.last_x) > self.threshold: #abs mean return absolute value
            self.last_x = x_px
        else:
            x_px = self.last_x  # No significant change, keep previous value

        if self.last_y is None or abs(y_px - self.last_y) > self.threshold:
            self.last_y = y_px
        else:
            y_px = self.last_y  # No significant change, keep previous value

        return x_px, y_px

def main():
    """
    Main function to set up the turtle and manage movement based on stabilized potentiometer input.
    """
    bob = setup_turtle(800, 800)
    rec = Receiver("/dev/tty.usbserial-110")  # Replace with actual port

    # Initialize stabilizer for smoothing
    stabilizer = Stabilizer(size=5, threshold=2)

    # Initial states
    pen_state = 0
    color_state = 0
    color_index = 0
    bob.penup()

    while True:
        # Read values from the receiver
        values = rec.read_values(4)  # Receiving x, y, pen_state, color_state from control.py
        x_pot, y_pot, new_pen_state, new_color_state = values

        # Get stabilized x and y positions
        x, y = stabilizer.get_stable_position(x_pot, y_pot, -400, 400)

        # Update pen state if it changed
        if new_pen_state != pen_state:
            pen_state = new_pen_state
            if pen_state == 1:
                bob.pendown()
            else:
                bob.penup()

        # Update color if the color state changed
        if new_color_state != color_state:
            color_state = new_color_state
            if color_index == 4:
                color_index = 0  # Reset to the first color
            else:
                color_index += 1
            change_color(bob, color_index)

        # Move turtle to the new stabilized position
        bob.goto(x, y)

if __name__ == '__main__':
    main()
