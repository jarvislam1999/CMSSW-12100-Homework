def compute_cfd(values, max_value):
    '''
    Compute the CFD of a list of integers.

    Inputs:
        values (list of ints): Integers
        max_value: The maximum value

    Returns: (list of floats) The CFD
    '''
    # STEP 1: COMPUTE THE FREQUENCIES
    
    # Create a list of all zeroes
    freq = [0] * (max_value+1)

    # Count the occurrence of each value
    for x in values:
        freq[x] += 1

    # STEP 2: COMPUTE THE CFD
    
    # Create an empty list
    cfreq = []

    # We need to know the total number of values
    count = 0
    for i in range(0, max_value+1):
        count += freq[i]
        cfreq.append(count / len(values))

    return cfreq
    
