# CS121 Lab 3: Functions

import math
import numpy
import pylab

def sinc(x):
    '''
    Real value sinc function  f(x) == sin(x)/x

    Inputs:
        x: float

    Return: float
    '''
    # Make sure we don't divide by zero  
    if x != 0:
        return math.sin(x) / x
    else:
        # sin(0) / 0 is defined as the limiting value 1
        return 1.0

def square(x):
	return x * x


def plot_sinc(left_boundary, right_boundary, dx):
    '''
    Plot the sinc function from left_boundary...right_boundary with
    increments of size dx.
    '''
    xs = numpy.arange(left_boundary, right_boundary, dx) 

    # apply the sinc function onto the xs list
    ys = []
    for x in xs:
        ys.append(sinc(x))
                
    # plot the figure
    pylab.figure()
    pylab.plot(xs,ys)
    pylab.title("Sinc function")
    pylab.xlabel("X values")
    pylab.ylabel("sinc(x)")
    pylab.show()

def plot_square(left_boundary, right_boundary, dx):
    '''
    Plot the sinc function from left_boundary...right_boundary with
    increments of size dx.
    '''
    xs = numpy.arange(left_boundary, right_boundary, dx) 

    # apply the sinc function onto the xs list
    ys = []
    for x in xs:
        ys.append(square(x))
                
    # plot the figure
    pylab.figure()
    pylab.plot(xs,ys)
    pylab.title("Square function")
    pylab.xlabel("X values")
    pylab.ylabel("x ** 2")
    pylab.show()
