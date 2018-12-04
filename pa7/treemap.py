# CS121: PA 7 - Diversity Treemap
#
# Code for constructing a treemap.

import argparse
import pandas as pd
import sys
import tree
import drawing
import click

###############
#             #
#  Your code  #
#             #
###############

def load_diversity_data(filename, debug=False):
    '''
    Load Silicon Valley diversity data and print summary

    Inputs:
        filename: (string) the name pf the file with the data

    Returns: a pandas dataframe
    '''
    data = pd.read_csv(filename)

    ### Add print statements here (if debug is True)
    if (debug == True):
        print('Diversity data comes from the following {} companies:'.format(len(data['company'].value_counts())))
        companies_ = list(data['company'].value_counts().index)
        companies_.sort()
        print(', '.join(companies_))
        print()
        print('The data includes {} employees'.format(sum(data['count'])))
        print()
        print('gender')
        gender_ = data.groupby('gender').sum()['count']
        print('    female: {}'.format(gender_['female']))
        print('    male: {}'.format(gender_['male']))
        print()
        print('race')
        race_ = data.groupby('race').sum()['count'] 
        for race in list(race_.index):
            print('    ', race, ' : ', race_[race])
        print()
        print('job_category')
        job_ = data.groupby('job_category').sum()['count'] 
        for job in list(job_.index):
            print('    ', job, ' : ', job_[job])

    return data


def compute_internal_counts(t):
    '''
    Assign a count to the interior nodes.  The count of the leaves
    should already be set.  The count of an internal node is the sum
    of the counts of its children.

    Inputs:
        t (Tree): a tree

    Returns:
        The input tree t should be modified so that every internal node's
        count is set to be the sum of the counts of its children.

        The return value will be:
        - If the tree has no children: the value of the count attribute
        - If the tree has children: the sum of the counts of the children
    '''

    ### Replace 0 with the appropriate return value
    if (t.num_children() == 0): # Set value for base case
        return t.count
    # Recursive step to compute sum of all children
    t.count = sum([compute_internal_counts(child) for child in t.children])
    return t.count


def compute_verbose_labels(t, prefix=None):
    '''
    Assign a verbose label to non-root nodes. Verbose labels contain the 
    full path to that node through the tree. For example, following the 
    path "Google" --> "female" --> "white" should create the verbose label 
    "Google: female: white"

    Inputs:
        t (Tree): a tree

    Outputs:
        Nothing. The input tree t should be modified to contain
            verbose labels for all non-root nodes
    '''


    ### YOUR CODE HERE
    if (prefix == None or prefix == ''): # If root node or no prefix
        t.verbose_label = t.label
    else: # Set verbose label if there's a prefix
        t.verbose_label = prefix + ': ' + t.label
    for child in t.children: # Recursive step on the node's children
        compute_verbose_labels(child, t.verbose_label)
    # Do not modify this return statement.
    # This function doesn't return anything!
    return None


def prune_tree(t, values_to_discard):
    '''
    Returns a tree with any node whose label is in the list values_to_discard
    (and thus all of its children) pruned. This function should return a copy
    of the original tree and should not destructively modify the original tree.
    The pruning step must be recursive.

    Inputs:
        t (Tree): a tree
        values_to_discard (list of strings): A list of strings specifying the
                  labels of nodes to discard

    Returns: a new Tree object representing the pruned tree
    '''

    ### YOUR CODE HERE
    # We construct a new tree as we go from the root to leaf of the old tree
    # If node is in the discard list, then don't copy and return None
    if (t.label in values_to_discard): 
        return None
    t_ = tree.Tree(t.label, t.count) # Form a copy of the old node
    if (t.num_children == 0): # If leaf then return the node
        return t_
    for child in t.children: # Recursive step for the node's children
        child_t = prune_tree(child, values_to_discard)
        # Add child to the tree if it's not in the discard list
        if (child_t is not None): 
            t_.add_child(child_t)

    ### Replace t with the appropriate return value
    return t_


def validate_tuple_param(p, name):
    assert isinstance(p, (list, tuple)) and len(p) == 2 \
        and isinstance(p[0], float) and isinstance(p[1], float), \
        name + " parameter to Rectangle must be a tuple or list of two floats"

    assert p[0] >= 0.0 and p[1] >= 0.0, \
        "Incorrect value for rectangle {}: ({}, {}) ".format(name, p[0], p[1]) + \
        "(both values must be >= 0)"


class Rectangle:
    '''
    Simple class for representing rectangles
    '''
    def __init__(self, origin, size, label, verbose_label):
        # Validate parameters
        validate_tuple_param(origin, "origin")
        validate_tuple_param(origin, "size")
        assert label is not None, "Rectangle label can't be None"
        assert isinstance(label, str), "Rectangle label must be a string"
        assert verbose_label is not None, "Rectangle verbose_label can't be None"
        assert isinstance(verbose_label, str), "Rectangle verbose_label must be a string"

        self.x, self.y = origin
        self.width, self.height = size
        self.label = label
        self.verbose_label = verbose_label

    def __str__(self):
        if self.verbose_label is None:
            label = self.label
        else:
            label = self.verbose_label

        return "RECTANGLE {:.4f} {:.4f} {:.4f} {:.4f} {}".format(self.x, self.y,
                                                                 self.width, self.height,
                                                                 label)

    def __repr__(self):
        return str(self)


def rectangulize(t, origin, size, label, verbose_label, vertical):
    '''
    Recursive helper function to aid Task 3

    Inputs:
        t: a Tree object
        origin: origin of the mother rectangle
        size: width and height of the mother rectangle
        label: label of the mother rectangle
        verbose_label: verbose_label of the mother rectangle
        vertical: Boolean to determine if we need to slice the
        mother traingle vertically or horizontally
    
    Output: a list of Rectangle objects after we finish tracing the tree

    '''
    if (t.num_children() == 0): # If leaf node then return mother rectangle
        return [Rectangle(origin, size, label, verbose_label)]
    x,y = origin
    w,h = size
    rec_list =[] # Initializing output list
    for child in t.children: # Begin recursive step on the node's children
        if (child.count == 0): # Check against division by 0
            ratio = 0
        else:
            ratio = child.count/ t.count # Ratio to slice mother rectangle 
        if (vertical == True): # Slice vertically
            rec_list = rec_list + rectangulize(child, (x,y), \
                (w * ratio, h), child.label, child.verbose_label, \
                not vertical) # Recursive step
            x += w * ratio # Move to the next point on mother rectangle's width
        else: # Slice horizontally
            rec_list = rec_list + rectangulize(child, (x,y), \
                (w, h * ratio), child.label, child.verbose_label, \
                not vertical) # Recursive step
            y += h * ratio # Next point on mother rectangle's height

    return rec_list

def compute_rectangles(t, bounding_rec_height=1.0, bounding_rec_width=1.0):
    '''
    Computes the rectangles for drawing a treemap of the provided tree

    Inputs:
        t (Tree): a tree
        bounding_rec_height, bounding_rec_width (floats): the size of
           the bounding rectangle.

    Returns: a list of Rectangle objects
    '''

    # Do not remove these function calls
    compute_internal_counts(t)
    compute_verbose_labels(t)

    ### YOUR CODE HERE
    
    # Replace [] with the appropriate return value
    return rectangulize(t, (0.0, 0.0), \
        (bounding_rec_width, bounding_rec_height), t.label, \
        t. verbose_label, True) # Perform recursive function


#############################
#                           #
#  Our code: DO NOT MODIFY  #
#                           #
#############################

@click.command(name="treemap")
@click.argument('diversity_file', type=click.Path(exists=True))
@click.option('--categories', '-c', type=str)
@click.option('--prune', '-p', type=str)
@click.option('--output', '-o', type=str)
def cmd(diversity_file, categories, prune, output):

    data = load_diversity_data(diversity_file)

    if categories is not None:
        categories = categories.split(",")

    if prune is not None:
        prune = prune.split(",")

    data_tree = tree.data_to_tree(data, categories)

    compute_internal_counts(data_tree)

    compute_verbose_labels(data_tree)

    if prune is not None:
        data_tree = prune_tree(data_tree, prune)

    rectangles = compute_rectangles(data_tree)

    if output == "-":
        for rect in rectangles:
            print(rect)
    else:
        drawing.draw_rectangles(rectangles, output)

if __name__ == "__main__":
    cmd() # pylint: disable=no-value-for-parameter