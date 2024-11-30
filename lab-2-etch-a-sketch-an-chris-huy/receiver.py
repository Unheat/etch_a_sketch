'''
This module defines the Receiver class
which listens for serial messages from
a Pi Pico microcontroller
'''

from serial import Serial
import struct
import time


class Receiver:
    """
    This class handles communication with a Pi Pico
    """
    def __init__(self, com_port, baud_rate=9600):
        """
        Constructor--sets up the Receiver class
        Inputs: 
        * com_port: the name of the port to connect to
        * baud_rate: the baud rate (default 9600)
        Outputs: a Receiver object
        By default, this uses 16-bit values (only int compatible)
        """
        self.serial = Serial(com_port, baud_rate)
        self.serial.reset_input_buffer()
        self.serial.read_all()
        time.sleep(0.1)
        self.serial.flush()
        self.value_size = 2 # the number of bytes per value

    def read_values(self, n_values):
        """
        Read n_values from the serial port
        Inputs: n_values: the number of 16-bit values to read
        Outputs: the n values, as a list
        """
        message_length = n_values * self.value_size
        message = self.serial.read(message_length)
        values = struct.unpack('<'+'H'*n_values, message)
        return list(values)

 
    def read(self, delimiter=b'\n'):
        """
        Read from the serial port until a delimiter is reached
        Inputs: delimiter (optional) the char to stop on
        Outputs: the values unpacked or false if read failed
        """
        buffer = bytearray()
        byte = self.serial.read(1)
        buffer.append(byte[0])
        while byte != b'\n':
            buffer.append(byte[0])
        if len(buffer) % self.value_size == 0:
            # if the buffer contains a compatible number of bytes for our value size
            n_values = len(buffer) // self.value_size
            return list(struct.unpack('<'+'H'*n_values, buffer))
        else:
            # if the read failed, return False
            return False
        
if __name__ == '__main__':
    # some test code to try out the receiver class
    while True:
        receiver = Receiver("/dev/tty.usbserial-210")
        values = receiver.read_values(2)
        print("values:",values)
