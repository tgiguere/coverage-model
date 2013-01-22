#!/usr/bin/env python

"""
@package coi
@file writers/writer_slocum.py
@author Tim Giguere
@brief Slocum writer
"""

import numpy as np
from external_data_translation.writers.writer_base import Writer


class SlocumWriter(Writer):
    def __init__(self, file_path=''):
        self._file_path = file_path
        self._variables = []
        self._units = []
        self._variable_data = {}

    def add_variable(self, var_name='', units=''):
        self._variables.append(var_name)
        self._units.append(units)

    def add_variable_data(self, var_name='', data=None):
        self._variable_data[var_name] = data

    def write_file(self):
        all_data = None
        for var in self._variables:
            if all_data is None:
                all_data = np.array([self._variable_data[var]])
            else:
                all_data = np.append(all_data, [self._variable_data[var]], axis=0)

        aligned_data = all_data.transpose()
        with open(self._file_path, 'w') as f:
            f.write(' '.join(self._variables) + '\n')
            f.write(' '.join(self._units) + '\n')

            for vals in aligned_data:
                f.write(' '.join(map(str, vals)) + '\n')