"""
Author: Henry "TJ" Chen
Last modified: July 9, 2023

Run this file to generate a visualisation of a standing wave
Animates the movement of the waves

** USE THIS FOR REFERENCE**
"""
from numpy import *
import matplotlib.pyplot as plt
from matplotlib import animation


def sine_wave_zero_phi(x_value, time, k_value, ang_freq):
    """This function returns the computed displacement value of the wave at a certain point
    x based on the inputted parameters
    """
    return sin(k_value * x_value - ang_freq * time)


# First set up the figure, the axes, and the subplots we want to animate
fig = plt.figure()
subplot = plt.axes(xlim=(0, 10), xlabel="x", ylim=(-2, 2), ylabel="y")
line1, = subplot.plot([], [], lw=2)
line2, = subplot.plot([], [], lw=2)
line3, = subplot.plot([], [], lw=2)

# Create a list of plot lines
lines = [line1, line2, line3]


def init():
    """ This function will be called before the animation begins to set all the plots to be empty
    before you begin adding data to them
    """
    for line in lines:
        line.set_data([], [])

        return lines


# creating an independent variable which will be used in the animate function
x = linspace(0, 10, 1000)


def animate(i):
    """ This function defines 3 variable lists, which are used in generating the animation.
    Uses an index-based for loop to use the set_data method for each line to set the
    appropriate function from the ‘waveFunctions’ variable

    Note, the amplitude of y1 and y2 is already 1 by default in the sineWaveZeroPhi function
    """
    y1 = sine_wave_zero_phi(ang_freq=(2 * pi), time=(0.01 * i), x_value=x, k_value=(pi / 2))
    y2 = sine_wave_zero_phi(ang_freq=(-2 * pi), time=(0.01 * i), x_value=x, k_value=(pi / 2))
    y3 = y1 + y2
    wavefunctions = [[x, y1], [x, y2], [x, y3]]

    # index based for loop
    for index in range(len(lines)):
        lines[index].set_data(wavefunctions[index][0], wavefunctions[index][1])

    return lines


# generates the animation and displays it to the user
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
plt.show()
