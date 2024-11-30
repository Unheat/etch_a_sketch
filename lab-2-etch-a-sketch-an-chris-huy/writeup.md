# Lab 2 Report: Etch-a-Sketch
## Name 1, Name 2 Huy Tran, Chris, An Dang
## Date: 

## Introduction
In a few sentences, describe what you built at a high level and why. It is okay to draw on the project instructions, but do not copy sentences word for word.

In this project, we are going to realize a digital version of the Etch-a-Sketch using a Raspberry Pi Pico microcontroller. The ultimate objective will be to provide a drawing interface through which users are allowed to interactively control the turtle graphics program running on a computer by rotating the potentiometers and pressing buttons on the Pico. Projects like this offer a great avenue for exploring physical computing as it involves integrating hardware inputs to drive digital actions on-screen.


## Problem Statement
Describe the main problems that you needed to solve to implement this project. This is not asking what challenges you encountered--rather, what were the core problems you needed to write solutions for? In particular, define the main goals of the project in terms of inputs and outputs.

The basic problem we were trying to solve was to provide a mapping of physical input from potentiometers and buttons on the Pico to the control of a drawing interface with accuracy on a computer. More precisely, we had to translate the values from potentiometers into precise x and y coordinates for a turtle graphic so that it could move around and be controlled smoothly. We also had to provide a mechanism using a button so that we would be able to turn the drawing pen up and down much like on a classic Etch-a-Sketch.



## Solution
Describe the algorithms you used to solve the problems and subproblems you defined above. You do not need to write a step by step algorithm for each function you wrote, just the key ideas behind how you implemented each major part of your solution.

We approached the solution by breaking it into three parts: button input, potentiometer input, and USB communication with the computer. In a loop, we check the state of the button, and toggle the state of the LED as well as the pen. The function read and scaled the values from the potentiometers to screen coordinates that mapped to the pixel range of the drawing area. Finally, using a Publisher-Receiver communication model, we sent these processed inputs from the Pico to an on-computer Python Turtle Graphics program moving the turtle accordingly.


## Reflections
### Ethical Reflection
This may seem a bit silly for a project like this, but try to reflect on whether there are any ethical components, good or bad, related to the kinds of technology you worked with in this project. Again, it is important to get into this practice, even if it sometimes seems superficial.

This project shows the possibilities and ethical considerations of physical computing. In and of themselves, they are rather simple, but in the bridge between digital and physical worlds, there is a potential to move into an area of remote robotics or devices that can assist people. Ethical considerations would include that such systems remain secure and accessible, particularly if expanded into areas deemed more critical.


### Personal Reflection
Briefly discuss any of the following: what challenges did you encounter in the completion of this project, technical, collaborative, or otherwise, and how did you overcome them? How did your previous knowledge and/or experiences help you with this project? Did you learn anything new? What directions might you want to explore further from this project? 

One technical challenge was the handling of the potentiometer, which was very unstable and created shaky lines in the drawing. We mitigated this by implementing a threshold filter that would reduce rapid changes in the values. It helped being collaborative in such a process; where each member from the team contributed ideas toward the smoothing of the input. This project was an opportunity to apply physical computing knowledge in a practical manner, and it opened up ideas for exploring more stable sensor integration techniques.


## Contribution Statement
Describe how each partner contributed to the work of this project. It is perfectly acceptable (and recommended) to describe how you actually worked together on all aspects of the project instead of dividing it and working separately, e.g. developing the algorithms together or pair programming. If so, try to think about what each of you brought to that process, e.g. Alice had the breakthrough about how to reverse scores, or Zheng's background in psychology helped us understand the problem.

We collaborated on every aspect of the project. An Dang was primarily responsible for coding of mapping of potentiometer to pixels and debugging of USB communication while Huy and Chris developed the logic for the buttons and toggling of pen states. Together, we tested and refined the output of the drawing. Both partners worked out solutions to stabilize the potentiometer and worked together on the final write-up and video demo.