from receiver import Receiver
from time import sleep

# Initialize Receiver
rec = Receiver("/dev/tty.usbserial-10")

# Loop to receive data
while True:
    values = rec.read_values(2)  # Expecting 2 values
     # Filter out junk data
    print(values)
    sleep(0.1)  # Small delay to avoid spamming the console
