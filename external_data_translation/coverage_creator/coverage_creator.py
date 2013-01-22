#!/usr/bin/env python

"""
@package coi
@file coverage_creator/coverage_creator.py
@author Tim Giguere
@brief Class used to create a coverage from an input data source
"""

"""
import numpy as np
from coverage_model.parameter import ParameterDictionary, ParameterContext
from coverage_model.parameter_types import QuantityType
from coverage_model.basic_types import VariabilityEnum
from external_data_translation.coverage_creator.coverage_creator import coverage_creator
pdict = ParameterDictionary()
t_ctxt = ParameterContext('time', param_type=QuantityType(value_encoding=np.dtype('int64')), variability=VariabilityEnum.TEMPORAL)
t_ctxt.uom = 'seconds since 01-01-1979'
pdict.add_context(t_ctxt, is_temporal=True)
temp_ctxt = ParameterContext('temp', param_type=QuantityType(value_encoding=np.dtype('float32')))
temp_ctxt.uom = 'K'
pdict.add_context(temp_ctxt)
sal_ctxt = ParameterContext('salinity', param_type=QuantityType(value_encoding=np.dtype('float32')))
sal_ctxt.uom = 'ppm'
pdict.add_context(sal_ctxt)
cov = coverage_creator('external_data_translation.parsers.parser_csv', 'CSVParser', 'external_data_translation/examples/test.csv')
new_cov = cov.create_coverage('test_data', 'external_data_translation/examples/csv_to_cov.pmap', pdict)
new_cov.close()
"""

import os

from coverage_model.coverage import SimplexCoverage, CRS, GridDomain, GridShape
from coverage_model.basic_types import AxisTypeEnum, MutabilityEnum
from coverage_model.utils import create_guid
from external_data_translation.mappers.parameter_mapper import ParameterMapper

class coverage_creator():
    def __init__(self, mod_name='', class_name='', file_path=''):

        module = __import__(mod_name, fromlist=[class_name])
        classobj = getattr(module, class_name)

        self._file_path = file_path

        self._parser = classobj(self._file_path)
        self._coverage = None

    def create_coverage(self, cov_name, mapping_file, param_dict):

        if param_dict:
            self._param_mapper = ParameterMapper(pmap_file=mapping_file, parameter_dictionary=param_dict)

            # Construct temporal Coordinate Reference System objects
            tcrs = CRS([AxisTypeEnum.TIME])

            # Construct temporal and spatial Domain objects
            tdom = GridDomain(GridShape('temporal', [0]), tcrs, MutabilityEnum.EXTENSIBLE) # 1d (timeline)

            self._coverage = SimplexCoverage(cov_name,
                                             create_guid(),
                                             os.path.splitext(os.path.basename(self._file_path))[0],
                                             parameter_dictionary=param_dict,
                                             temporal_domain=tdom)

            shp = self._parser.get_var_shape(self._coverage.temporal_parameter_name)
            self._coverage.insert_timesteps(shp[0])

            mapping = self._param_mapper.get_mapping()

            for var in self._parser.get_col_names():
                vals = self._parser.get_values(var_name=var)
                self._coverage.set_parameter_values(mapping[var],
                                                    value=vals)
            return self._coverage