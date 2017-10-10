#!/usr/bin/env python
# -*- coding: utf-8 -*-
# argparse_action.py

"""
store
    Save the value, after optionally converting it to a different type.
    This is the default action taken if none is specified explicitly.

store_const
    Save a value defined as part of the argument specification,
    rather than a value that comes from the arguments being parsed.
    This is typically used to implement command-line flags that are not Booleans.

store_true / store_false
    Save the appropriate Boolean value. These actions are used to implement Boolean switches.

append
    Save the value to a list. Multiple values are saved if the argument is repeated.

append_const
    Save a value defined in the argument specification to a list.

version
    Prints version details about the program and then exits. """

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s", action="store",
                    dest="simple_value",
                    help="Store a simple value")

parser.add_argument("-c", action="store_const",
                    dest="const_value",
                    const="value-to-store",
                    help="Store a constant value")

parser.add_argument("-t", action="store_true",
                    default=False,
                    dest="boolean_true",
                    help="Set a switch to True")

parser.add_argument("-f", action="store_false",
                    default=True,
                    dest="boolean_false",
                    help="Set a switch to False.")

parser.add_argument("-a", action="append",
                    dest="collection",
                    default=[],
                    help="Add repeated values to list.")

parser.add_argument("-A", action="append_const",
                    dest="const_collection",
                    const="value-1-to-append",
                    default=[],
                    help="Add different values to list.")

parser.add_argument("-B", action="append_const",
                    dest="const_collection",
                    const="value-2-to-append",
                    help="Add different values to list.")

parser.add_argument("--version", action="version",
                    version='argparse_actions.py 1.0')


results = parser.parse_args()

print('simple_value      = {!r}'.format(results.simple_value))
print('const_value       = {!r}'.format(results.const_value))
print('boolean_true      = {!r}'.format(results.boolean_true))
print('boolean_false     = {!r}'.format(results.boolean_false))
print('collection        = {!r}'.format(results.collection))
print("const_collection  = {!r}".format(results.const_collection))