#!/usr/bin/env python

"""
@package coi
@file output/output_writer.py
@author Tim Giguere
@brief Class used to output a coverage to a file
"""

#from coverage_model.coverage import SimplexCoverage
#from external_data_translation.output.output_writer import output_writer
#cov = SimplexCoverage.load('test_data/1BF2DC34-4CCB-4F1B-A333-28CD4173E6D2')
#writer = output_writer('external_data_translation.writers.writer_csv', 'CSVWriter', cov, 'external_data_translation/examples/cov_to_file.pmap', 'external_data_translation/examples/test_out.csv')
#writer.create_output()

from external_data_translation.mappers.parameter_mapper import ParameterMapper

class output_writer():
    def __init__(self, mod_name, class_name, coverage, mapping_file, file_path):

        module = __import__(mod_name, fromlist=[class_name])
        classobj = getattr(module, class_name)

        self._writer = classobj(file_path)
        self._coverage = coverage
        self._mapper = ParameterMapper(pmap_file=mapping_file, parameter_dictionary=self._coverage.parameter_dictionary).get_mapping()

    def create_output(self):
        vars = self._coverage.list_parameters()
        vars.reverse()
        for var in vars:
            self._writer.add_variable(self._mapper[var])
            var_data = self._coverage.get_parameter_values(var)
            self._writer.add_variable_data(var_name=self._mapper[var], data=var_data)

        self._writer.write_file()