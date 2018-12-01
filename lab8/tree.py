#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Class for representing tree nodes
#
#####################################
# DO NOT MODIFY THE CODE IN THIS FILE
#####################################

import textwrap


class Tree(object):

    def __init__(self, label, count=None, children=None):
        '''
        Construct a Tree

        Inputs:
            label: (string) a label that identifies the root node
            count: (float) an application specific weight
            children: (list of Tree) child nodes, or None if no children
        '''
        self.label = label
        self.count = count
        if children is None:
            self.children = []
        else:
            self.children = children
        self.verbose_label = None

    def num_children(self):
        '''
        Returns the number of children in the tree
        '''
        return len(self.children)

    def add_child(self, other_tree):
        """
        Adds an existing tree as a child of the tree.

        Parameter:
        - other_tree: Tree to add as a subtree
        """
        if not isinstance(other_tree, Tree):
            raise ValueError("Parameter to add_child must be a Tree object")

        self.children.append(other_tree)

    def __print_r(self, prefix, last, kformat, vformat, maxdepth, verbose):
        ''' Recursive helper method for print() '''
        if maxdepth is not None:
            if maxdepth == 0:
                return
            else:
                maxdepth -= 1

        if len(prefix) > 0:
            if last:
                lprefix1 = prefix[:-3] + u"  └──"
            else:
                lprefix1 = prefix[:-3] + u"  ├──"
        else:
            lprefix1 = u""

        if len(prefix) > 0:
            lprefix2 = prefix[:-3] + u"  │"
        else:
            lprefix2 = u""

        if last:
            lprefix3 = lprefix2[:-1] + "   "
        else:
            lprefix3 = lprefix2 + "  "

        if verbose:
            label = self.verbose_label
        else:
            label = self.label

        if self.count is None:
            ltext = (kformat).format(label)
        else:
            ltext = (kformat + ": " + vformat).format(label, self.count)

        ltextlines = textwrap.wrap(ltext, 80, initial_indent=lprefix1,
                                   subsequent_indent=lprefix3)

        print(lprefix2)
        print(u"\n".join(ltextlines))

        if self.children is None:
            return
        else:
            for i, st in enumerate(self.children):
                if i == len(self.children) - 1:
                    newprefix = prefix + u"   "
                    newlast = True
                else:
                    newprefix = prefix + u"  │"
                    newlast = False

                st.__print_r(newprefix, newlast, kformat, vformat, maxdepth, verbose)

    def print(self, kformat="{}", vformat="{}", maxdepth=None, verbose=False):
        '''
        Inputs: self: (the tree object)
                kformat: (format string) specifying format for label
                vformat: (format string) specifying format for label and count
                maxdepth: (integer) indicating number of levels to print.
                          None sets no limit
                verbose: (boolean) Prints verbose labels if True

        Returns:  no return value, but a tree is printed to screen
        '''
        self.__print_r(u"", False, kformat, vformat, maxdepth, verbose)
