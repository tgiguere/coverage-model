#!/usr/bin/env python

"""
@package coi
@file writers/writer_base.py
@author Tim Giguere
@brief Base writer class that all writers should inherit from
"""

class Writer(object):
    def __init__(self, file_path=''):
        raise NotImplementedError('__init__ must be implemented in child class')

    def add_variable(self, var_name=''):
        raise NotImplementedError('add_variable must be implemented in child class')

    def add_variable_data(self, var_name='', data=None):
        raise NotImplementedError('add_variable_data must be implemented in child class')

    def write_file(self):
        raise NotImplementedError('write_file must be implemented in child class')