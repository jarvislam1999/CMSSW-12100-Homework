from math import sin
from tree import Tree

def is_power_of_two(n):
    # replace the pass statement with your code
    pass


def fib(n):
    # replace the pass statement with your code
    pass

def find_root_sqrt2(epsilon, a, b):
    # replace the pass statement with your code
    pass


t0 = Tree("node0", 27)

t1 = Tree("node0", 1)
t1.add_child( Tree("node1", 2, children=[Tree("node2", 3)]))
t1.add_child( Tree("node3", 4))
t1.add_child( Tree("node4", 5))


def count_leaves(t):
    '''
    Count the number of leaves in the tree rooted at t
    
    Inputs: (Tree) a tree
    
    Returns: (integer) number of leaves in t
    '''
    assert t is not None

    if t.num_children() == 0:
        return 1

    num_leaves = 0
    for kid in t.children:
        num_leaves += count_leaves(kid)

    return num_leaves


def add_values(t):
    # replace the pass statement with your code
    pass
