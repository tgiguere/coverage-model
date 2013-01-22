#!/usr/bin/env python

"""
@package coi
@file parsers/parser_slocum.py
@author Tim Giguere
@brief Example Slocum parser class
"""

"""
import numpy
from coverage_model.parameter import ParameterDictionary, ParameterContext
from coverage_model.parameter_types import QuantityType
from coverage_model.basic_types import VariabilityEnum
from external_data_translation.coverage_creator.coverage_creator import coverage_creator

pdict = ParameterDictionary()

t_ctxt = ParameterContext('c_wpt_y_lmc', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'm'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('sci_water_cond', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 's/m'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_y_lmc', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'm'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('u_hd_fin_ap_inflection_holdoff', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'sec'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('sci_m_present_time', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'timestamp'
pdict.add_context(t_ctxt, is_temporal=True)

t_ctxt = ParameterContext('m_leakdetect_voltage_forward', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'volts'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('sci_bb3slo_b660_scaled', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'nodim'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('c_science_send_all', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'bool'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_gps_status', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'enum'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_water_vx', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'm/s'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_water_vy', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'm/s'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('c_heading', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'rad'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('sci_fl3slo_chlor_units', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'ug/l'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('u_hd_fin_ap_gain', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = '1/rad'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_vacuum', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'inHg'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('u_min_water_depth', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'm'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_gps_lat', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'lat'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_veh_temp', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'c'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('f_fin_offset', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'rad'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('u_hd_fin_ap_hardover_holdoff', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'sec'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('c_alt_time', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'sec'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_present_time', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'timestamp'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_heading', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'rad'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('sci_bb3slo_b532_scaled', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'nodim'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('sci_fl3slo_cdom_units', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'qsde'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_fin', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'rad'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('x_cycle_overrun_in_ms', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'msec'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('sci_water_pressure', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'bar'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('u_hd_fin_ap_igain', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = '1/rad-sec'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('sci_fl3slo_phyco_units', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'ppb'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_battpos', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'in'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('sci_bb3slo_b470_scaled', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'nodim'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_lat', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'lat'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_gps_lon', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'lon'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('sci_ctd41cp_timestamp', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'timestamp'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_pressure', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'bar'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('c_wpt_x_lmc', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'm'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('c_ballast_pumped', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'cc'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('x_lmc_xy_source', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'enum'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_lon', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'lon'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_avg_speed', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'm/s'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('sci_water_temp', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'degc'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('u_pitch_ap_gain', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = '1/rad'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_roll', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'rad'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_tot_num_inflections', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'nodim'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_x_lmc', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'm'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('u_pitch_ap_deadband', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'rad'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_final_water_vy', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'm/s'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_final_water_vx', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'm/s'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_water_depth', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'm'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_leakdetect_voltage', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'volts'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('u_pitch_max_delta_battpos', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'in'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_coulomb_amphr', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'amp-hrs'
pdict.add_context(t_ctxt)

t_ctxt = ParameterContext('m_pitch', param_type=QuantityType(value_encoding=numpy.dtype('float32')))
t_ctxt.uom = 'rad'
pdict.add_context(t_ctxt)

cov = coverage_creator('external_data_translation.parsers.parser_slocum', 'SlocumParser', 'external_data_translation/examples/ru05-2012-021-0-0-sbd.dat')
new_cov = cov.create_coverage('test_data', 'external_data_translation/examples/slocum_to_cov.pmap', pdict)
new_cov.close()
"""

from external_data_translation.parsers.parser_base import Parser
from StringIO import StringIO
import requests
import csv
import numpy as np

class SlocumParser(Parser):
    # John K's documentation says there are 16 header lines, but I believe there are actually 17
    # The 17th indicating the 'dtype' of the data for that column
    DEFAULT_HEADER_SIZE = 17
    header_map = {}
    sensor_map = {}
    data_map = {}

    def __init__(self, url=None):
        """
        Constructor for the parser. Initializes headers and data

        @param url the url/filepath of the file
        @param header_size number of header lines. This is information is in the header already, so it will be removed
        """
        if not url:
            raise SlocumParseException('Must provide a filename')

        self.file_path = url

        sb = None
        try:
            # Get a byte-string generator for use in the data-retrieval loop (to avoid opening the file every time)
            sb = self.get_sbuffer(self.file_path)
            sb.seek(0)
            line = sb.readline()
            key, value = line.split(':', 1)
            while key.strip() != 'num_ascii_tags':
                line = sb.readline()
                key, value = line.split(':', 1)
            self.header_size = int(value.strip())

            sb.seek(0)
            for x in xrange(self.header_size):
                line = sb.readline()
                key, value = line.split(':', 1)
                self.header_map[key.strip()] = value.strip()

            # Collect the sensor names & units
            self._sensor_names = sb.readline().split()
            units = sb.readline().split()
            # Keep track of the intended data type for each sensor
            dtypes = []
            for d in sb.readline().split():
                if d is '1':
                    dtypes.append('byte')
                elif d is '2':
                    dtypes.append('short')
                elif d is '4':
                    dtypes.append('float')
                elif d is '8':
                    dtypes.append('double')

            assert len(self._sensor_names) == len(units) == len(dtypes)

            for i in xrange(len(self._sensor_names)):
                #sb.seek(0)
                self.sensor_map[self._sensor_names[i]] = (units[i], dtypes[i])
        finally:
            if not sb is None:
                sb.close()

    def get_col_names(self):
        return self._sensor_names

    def get_var_shape(self, var_name=''):
        vals = self.read_var(var_name)
        return vals.shape

    def get_values(self, var_name='', _slice=None):
        vals = self.read_var(var_name)
        if _slice:
            return vals[_slice]
        else:
            return vals

    def read_var(self, var_name=''):
        col_index = self._sensor_names.index(var_name)    # Will raise ValueError is name is not in list
        return np.genfromtxt(self.file_path, delimiter=' ', skip_header=self.header_size + 2, usecols=col_index, missing_values='NaN')

    #TODO:  IMPROVE - Function similar to above that reads a file to a StringIO from http, ftp, or fs
    #VERY BASIC
    def get_sbuffer(self, url, type=None):
        # If type isn't specified, attempt to determine based on url
        type = type or self._get_type(url)

        # Switch on type
        if type is 'http':
            response = requests.get(url)
            buf = StringIO(response.content)
        elif type is 'ftp':
            raise NotImplementedError
        elif type is 'fs':
            buf = StringIO(open(url).read())
        else:
            #log.warn('Unknown type specified: {0}'.format(type))
            buf = None

        return buf

    def _get_type(self, base):
        if base.startswith('http://'):
            type = 'http'
        elif base.startswith('ftp://'):
            type = 'ftp'
        else:
            type = 'fs'

        return type

class SlocumParseException(Exception):
    pass