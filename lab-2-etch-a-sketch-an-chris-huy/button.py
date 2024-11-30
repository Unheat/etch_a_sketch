'''
A program that reads whether a button has been
pressed or not
'''
import picozero
left = picozero.Pot(27)
right = picozero.Pot(28)
while True:

    a = left.read_position()
    picozero.sleep(0.1)
    print(a)
