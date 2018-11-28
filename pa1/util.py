'''
Utility code for SIR assignment
'''

import json

def read_json_file(data_filename):
    '''
    Purpose: to read in the json data file
    Inputs: data_filename (str): name of the json file to read in
    Returns: json_data (dict): json file contents
    '''
    try:
        with open(data_filename) as f:
            json_data = json.load(f)
        return json_data
    except IOError:
        print("error: could not read in json file {}".format(data_filename))


def get_config(data_filename):
    '''
    Purpose: get starting configuration of a given city for a
      simulation from a json file.
    Inputs: data_filename (str): name of the json file to read in
    Returns:
      parameters for the simulation: starting states of simulation
        (list), starting state seed (int), d (int) for the simulation,
        r (float) for the simulation, and N (int) for the simulation
    '''
    json_data = read_json_file(data_filename)
    return (
        json_data['starting_state'],
        int(json_data['starting_seed']),
        int(json_data['max_num_days']),
        float(json_data['infection_rate']),
        int(json_data['num_trials']))
