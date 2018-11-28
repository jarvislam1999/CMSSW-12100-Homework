import math
import pylab
import numpy


def sinc(x):
    ''' Compute the sampling (or sine cardinal) function'''
    if x != 0:
        return math.sin(x) / x
    else:
        return 1


def plot_sinc(step):
    ''' Plot the sinc function '''

    # Compute Xs using range or numpy.arange
    #X = []
    #for i in range(-10,11):
    #	X.append(i)
    X = numpy.arange(-10, 10, step)

    Y= []
    for i in X:
    	Y.append(sinc(i))

    # Compute Ys using a loop
    # Call plot
    pylab.plot(X,Y)
    # Call show
    pylab.show()
    # remove the next line
    # pass
