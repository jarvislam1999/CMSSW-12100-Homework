'''
Polling places

JARVIS LAM

Main file for polling place simulation
'''

import sys
import random
import queue
import click
import util


### YOUR Voter, VoterGenerator, and Precinct classes GO HERE.

class Voter(object):
    def __init__(self, arrival_time, voting_duration):
        '''
        Initializing 4 attributes: (made it public because will make code
        much shorter with same efficiency)
        arrival_time: voter's arrival time
        start_time: when they get assigned to a booth
        departure_time: when they leave the booth
        voting_duration: how long it takes them to vote in the booth
        '''
        self.arrival_time = arrival_time
        self.start_time = None
        self.departure_time = None
        self.voting_duration = voting_duration

    # I did not include a repr process because it was not used
    # anywhere in the code


class VoterGenerator(object):
    def __init__(self, arrival_rate, voting_duration_rate, num_voters):
        '''
        Initiating five attributes:
        arrival_rate: rate at which voters arrive
        voting_duration_rate: rate at which voters spend voting
        
        These two act as parameter for the Poisson distribution
        from which we will derive our next arrival time

        num_voters: maximum number of voters to generate
        t: time to keep track of the current voter arrival time
        num_voter_current: number of voters to keep track of max voters
        '''
        self.arrival_rate = arrival_rate
        self.voting_duration_rate = voting_duration_rate
        self.num_voters = num_voters
        self.t = 0
        self.num_voter_current = 0

    def next(self):
        '''
        Generate the next voter to arrive based on the Poisson 
        distribution

        Output: a Voter object or None if the limit is achieved
        '''
        # Check if the maximum number of voters are reached
        if (self.num_voter_current >= self.num_voters):
            return None

        # Get the next arrival time and voter duration from the Poisson
        # distribution
        arrival_time_, voting_duration_ = util.\
        gen_poisson_voter_parameters(self.arrival_rate, self.voting_duration_rate)
        # Create a Voter object with this updated information
        voter = Voter(self.t + arrival_time_, voting_duration_)
        # Update current time and number of voters
        self.t += arrival_time_
        self.num_voter_current += 1
        return voter

        
class Precinct(object):
    def __init__(self, name, hours_open, num_voters, num_booths, \
        arrival_rate, voting_duration_rate):
        '''
        Initiating four attributes:
        name: Name of the precinct
        hours_open: The number of MINUTES it's open
        num_booth: The number of booths the precinct has
        voter_generator: A VoterGenerator object for the precinct
        '''
        self.name = name
        self.num_booths = num_booths
        self.hours_open = hours_open * 60
        self.voter_generator = VoterGenerator(arrival_rate, \
            voting_duration_rate, num_voters)

    def __voter_queue_create(self):
        '''
        Create a PriorityQueue, which will be the voting booth

        Output: An empty priority queue
        '''
        return queue.PriorityQueue(self.num_booths)

    def __booth_is_full(self, queue_):
        '''
        Check if the queue/ booth is full
        
        Input: The queue/ booth
        Output: True if the booth is full, False otherwise
        '''
        return queue_.full()

    def __booth_is_empty(self, queue_):
        '''
        Check if the queue/ booth is empty
        
        Input: The queue/ booth
        Output: True if the booth is empty, False otherwise
        '''
        return queue_.empty()

    def __voter_queue_get(self, queue_):
        '''
        Remove the lowest priority item from the list and 
        return that item
        
        Input: The queue/booth
        Output: A tuple containing a Voter object and its 
        departure time
        '''
        return queue_.get(block = False)

    def __voter_queue_put(self, queue_, item):
        '''
        Insert an item into the queue

        Input: 
        queue_: The queue/ booth
        item: The item to insert in the list

        Output: Empty, but the queue should be updated
        '''
        return queue_.put(item, block = False)
    
    def simulate(self):
        '''
        Simulate a voting session at the precinct

        Output: A list of Voter objects/ the people who voted
        '''
        # Create an empty queue/ booth
        voter_queue = self.__voter_queue_create()
        # Initiate variable to keep count of voters who arrive
        num_voter = 0
        voter_list = [] # Initiate output list
        voter = self.voter_generator.next()
        # Begin simulation
        while (voter != None and voter.arrival_time < self.hours_open):
            # If the booth is full, remove proper voter from queue, 
            # save it to voter 1
            if (self.__booth_is_full(voter_queue)):
                voter1 = self.__voter_queue_get(voter_queue)
                # Set start_time of new voter to either their arrival or
                # the old one's departure, whatever comes later
                if (voter.arrival_time >= voter1[0]):
                    voter.start_time = voter.arrival_time
                else: 
                    voter.start_time = voter1[0]
            else:
                # If booth if not full just set start_time to arrival time
                voter.start_time = voter.arrival_time

            # Calculate departure time and insert new voter into the queue
            voter.departure_time = voter.start_time +\
            voter.voting_duration
            self.__voter_queue_put(voter_queue, (voter.departure_time,\
                    voter))
            # Get the voter who will surely finish voting into output list
            voter_list.append(voter)
            # Generate the next voter
            voter = self.voter_generator.next() 
        # Empty out queue (for no reason at all)
        while( not self.__booth_is_empty(voter_queue)):
            self.__voter_queue_get(voter_queue)
        return voter_list


def simulate_election_day(precincts, seed=0):
    '''
    Simulate the election day

    Input: 
    precincts: dictionary of precinct information
    seed: random seed

    Output: dictionary matching precinct name with list of voters
    who voted for that precinct
    '''
    # YOUR CODE HERE.
    # Initializing output dict
    precinct_dict = {}
    # Get data form the input dictionary and simulate the precincts
    # Store the result into output dictionary
    for p in precincts:
        random.seed(seed) # Set seed
        precinct = Precinct(p["name"], p["hours_open"], p["num_voters"],\
            p["num_booths"], p["voter_distribution"]["arrival_rate"],\
            p["voter_distribution"]["voting_duration_rate"])
        precinct_dict[precinct.name] = precinct.simulate() # Filling dictionary

    # REPLACE {} with a dictionary mapping precint names
    # to a list of voters for that precinct
    return precinct_dict


def find_avg_wait_time(precinct, num_booths, ntrials, initial_seed=0):
    '''
    Find average wait time of a voter when arriving at a precinct
    Input:
    precinct: a dictionary containing info for the precinct
    num_booths: alternative maximum number of booths
    ntrials: number of trials
    initial_seed: initial seed

    Output: Float representing average waiting time
    '''

    # YOUR CODE HERE.
    # Initializing output list
    wt_list = []
    p = precinct # Just to reduce length of code
    # Run through trail and record waiting time
    for num in range(0,ntrials):
        random.seed(initial_seed) # Set seed
        precinct_ = Precinct(p["name"], p["hours_open"], p["num_voters"],\
            num_booths, p["voter_distribution"]["arrival_rate"],\
            p["voter_distribution"]["voting_duration_rate"])
        pvoters = precinct_.simulate() # Simulate the precinct
        wt_list.append(sum([v.start_time - v.arrival_time\
         for v in pvoters]) / len(pvoters)) # Fill waiting time list
        initial_seed += 1 # Change the seed every round
    wt_list.sort() #Sort the list in ascending order

    # REPLACE 0.0 with the waiting time this function computes
    return wt_list[ntrials//2] # Return the median of the sorted list


def find_number_of_booths(precinct, target_wait_time, max_num_booths, ntrials, seed=0):
    '''
    Find the smallest number of booth where the average wait time will drop below a 
    certain threshold

    Input: 
    precinct: dictionary containing precinct info
    target_wait_time: maximum wait time
    max_num_booth: maximum number of booths
    ntrials: number of trials for average wait time calculation
    seed: initial seed

    Output: integer with number of booths and float with average wait time
    '''
    # YOUR CODE HERE
    # Find the average wait time for different numbers of booths,
    # return values if conditions are met
    for num_booths in range(1,max_num_booths): 
        avg_wt = find_avg_wait_time(precinct, num_booths, ntrials, seed)
        if (avg_wt < target_wait_time):
            return(num_booths, avg_wt)
    # Replace (0,0) with a tuple containing the optimal number of booths
    # and the average waiting time for that number of booths
    return (0, None)

# DO NOT REMOVE THESE LINES OF CODE
# pylint: disable-msg= invalid-name, len-as-condition, too-many-locals

@click.command(name="simulate")
@click.argument('precincts_file', type=click.Path(exists=True))
@click.option('--max-num-booths', type=int)
@click.option('--target-wait-time', type=float)
@click.option('--print-voters', is_flag=True)
def cmd(precincts_file, max_num_booths, target_wait_time, print_voters):
    '''
    Run the command.
    '''

    precincts, seed = util.load_precincts(precincts_file)

    if target_wait_time is None:
        voters = simulate_election_day(precincts, seed)
        print()
        if print_voters:
            for p in voters:
                print("PRECINCT '{}'".format(p))
                util.print_voters(voters[p])
                print()
        else:
            for p in precincts:
                pname = p["name"]
                if pname not in voters:
                    print("ERROR: Precinct file specified a '{}' precinct".format(pname))
                    print("       But simulate_election_day returned no such precinct")
                    print()
                    return -1
                pvoters = voters[pname]
                if len(pvoters) == 0:
                    print("Precinct '{}': No voters voted.".format(pname))
                else:
                    pl = "s" if len(pvoters) > 1 else ""
                    closing = p["hours_open"]*60.
                    last_depart = pvoters[-1].departure_time
                    avg_wt = sum([v.start_time - v.arrival_time for v in pvoters]) / len(pvoters)
                    print("PRECINCT '{}'".format(pname))
                    print("- {} voter{} voted.".format(len(pvoters), pl))
                    msg = "- Polls closed at {} and last voter departed at {:.2f}."
                    print(msg.format(closing, last_depart))
                    print("- Avg wait time: {:.2f}".format(avg_wt))
                    print()
    else:
        precinct = precincts[0]

        if max_num_booths is None:
            max_num_booths = precinct["num_voters"]

        nb, avg_wt = find_number_of_booths(precinct, target_wait_time, max_num_booths, 20, seed)

        if nb is 0:
            msg = "The target wait time ({:.2f}) is infeasible"
            msg += " in precint '{}' with {} or fewer booths"
            print(msg.format(target_wait_time, precinct["name"], max_num_booths))
        else:
            msg = "Precinct '{}' can achieve average waiting time"
            msg += " of {:.2f} with {} booths"
            print(msg.format(precinct["name"], avg_wt, nb))
    return 0


if __name__ == "__main__":
    cmd() # pylint: disable=no-value-for-parameter
