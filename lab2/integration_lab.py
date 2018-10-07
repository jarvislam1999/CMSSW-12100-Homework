def f(x):
    '''
    Real valued square function  f(x) == x^2
    '''

    return x*x


def integrate(N):
    ''' Integrate the function f using the rectangle method '''

    # Your code here
    # decide on the number of rectangles
    # N = 1000
    # compute the width of the rectangles
    dx = 1/N
    # use a loop to compute the total area
    totalArea = 0
    for i in range(0,N):
    	totalArea= totalArea + dx*f(i*dx)
    # return the value of totalArea
    return totalArea
    # remove the next line
    # pass
