CS 121: Schelling's Model of Housing Segregation

The grid file format is simple. The first line contains the grid
size. Each subsequent line contains information for a single row,
starting with row 0. An "M" means that the corresponding location has a maroon 
homeowner, a "B" means that the corresponding location has a blue 
homeowner, and an "O" means that the location is open.  See the file
``a18-sample-grid.txt``, which contains the initial grid from
the example discussed in the programming assignment.

a18-sample-grid.txt: example from the writeup.

grid-sea-of-red.txt: A grid in which all the homes are
occupied by maroon homeowners, except two open homes and two home
occupied by blue homeowners.

Examples that use the sample grid from the assignment description:

  a18-sample-grid.txt: original state

  a18-sample-grid-1-30-50-1-final.txt: result of running simulation with 
    an M threshold of 0.30, a B threshold of 0.50, R=1, and one step.

  a18-sample-grid-1-33-33-0-final.txt: result of running simulation with 
    an M threshold of 0.33, a B threshold of 0.33, R=1, and zero steps.

  a18-sample-grid-1-33-33-3-final.txt: result of running simulation with 
    an M threshold of 0.33, a B threshold of 0.33, R=1, and three steps.

  a18-sample-grid-1-50-30-1-final.txt: result of running simulation with 
    an M threshold of 0.50, a B threshold of 0.30, R=1, and one step.

  a18-sample-grid-1-60-40-1-final.txt: result of running simulation with 
    an M threshold of 0.60, a B threshold of 0.40, R=1, and one step.

  a18-sample-grid-1-60-40-2-final.txt: result of running simulation with 
    an M threshold of 0.60, a B threshold of 0.40, R=1, and two steps.

  a18-sample-grid-1-75-25-1-final.txt: result of running simulation with 
    an M threshold of 0.75, a B threshold of 0.25, R=1, and one step.

  a18-sample-grid-2-44-70-7-final.txt: result of running simulation with 
    an M threshold of 0.44, a B threshold of 0.70, R=2, and seven steps.

  a18-sample-writeup.txt: original state of the grid used in writeup examples

  grid-sea-of-red.txt: A grid in which most the homes are occupied by
    maroon homeowners.

  grid-sea-of-red-1-40-70-1-final.txt: result of simulation with 
    M threshold of 0.40, B threshold of 0.70, R=1, and one step

  grid-no-neighbors.txt: a sparsely populated grid used in
    compute_similarity score tests.

  grid-ten.txt: a 10x10 grid used in a number of tests.

  grid-ten-2-32-62-4-final.txt: result of simulation with
    M threshold of 0.32, B threshold of 0.62, R=2, and four steps

  grid-ten-2-32-62-4-final.txt: result of simulation with
    M threshold of 0.32, B threshold of 0.62, R=2, and four steps

  grid-ten-2-40-65-2-final.txt: result of simulation with
    M threshold of 0.40, B threshold of 0.65, R=2, and two steps

  grid-ten-3-32-62-4-final.txt: result of simulation with
    M threshold of 0.32, B threshold of 0.62, R=3, and four steps

  grid-ties.txt: grid used to test a relocation where the homeowner
    would be satisfied in multiple equidistant open homes.

  grid-ties-2-33-70-2-final.txt: result of simulation with
    M threshold of 0.33, B threshold of 0.70, R=2, and two steps

Large grid example:

  large-grid.txt: grid used in large example

  large-grid-2-33-70-20-final.txt: Result of simulation of R-2
    neighborhood w/ M threshold of 0.33, B threshold of 0.70, and 
    up to 20 steps. In some of the relocations in this grid, all tiebreakers 
    are needed.
