'''
Practice problem for classes
'''

import random

PRESENT_PRODUCTION_TIME = 1.8

class Present(object):
    ''' Class for representing presents '''
    def __init__(self, start_time):
        self._production_end_time = start_time + PRESENT_PRODUCTION_TIME

    def present_ready(self, current_time):
        return current_time >= self._production_end_time

### YOUR ELF CLASS GOES HERE

class Santa(object):
    ''' Class for representing Santa '''

    def __init__(self):
        self._total_num_presents = 0
        self._total_num_ready_presents = 0
        self._elves = []
        self._next_elf_index = 0

    def get_total_num_presents(self):
        return self._total_num_presents

    def get_total_num_ready_presents(self):
        return self._total_num_ready_presents


    def gather_elves(self, num_elves):
        self._elves = [Elf() for i in range(num_elves)]

    def distribute_presents_to_make(self, num_presents_to_make, current_time):
        elf_index = self._next_elf_index
        for i in range(num_presents_to_make):
            present = Present(current_time)
            self._elves[elf_index].add_present(present)
            elf_index = (elf_index + 1) % len(self._elves)

        self._next_elf_index = elf_index
        self._total_num_presents += num_presents_to_make

    def collect_ready_presents_from_elves(self, current_time):
        total = sum(elf.remove_presents(current_time) for elf in self._elves)
        self._total_num_ready_presents += total


def simulate_Santa(num_elves, max_time, seed=None):
    '''
    Simulate Santa's workshop.
    '''

    if seed:
        random.seed(seed)

    # initilize
    santa = Santa()
    santa.gather_elves(num_elves)

    for i in range(max_time):
        #odd hours, assign work to elves
        if i%2:
            num_presents_to_make = random.randrange(100, 200)
            santa.distribute_presents_to_make(num_presents_to_make, i)
        #even hours, collect presents from elves
        else:
            santa.collect_ready_presents_from_elves(i)

    print("Santa has {} presents ready, and {} presents in progress!".format
          (santa.get_total_num_presents(),
           santa.get_total_num_presents() - santa.get_total_num_ready_presents()))


if __name__ == "__main__":
    simulate_Santa(100, 100)
    simulate_Santa(200, 1000)

