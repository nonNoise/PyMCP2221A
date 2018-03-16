#############################################################
#    MIT License                                            #
#    Copyright (c) 2017 Yuta KItagami                       #
#############################################################
from PyMCP2221A import BME280

import time
print('-'*50)
print('MCP2221(A) BME280 ')
print('-'*50)

bme280 = BME280.BME280()
BME280.SoftReset()
bme280.ReadCoefficients()
bme280.SetSampling()
bme280.ReadTemperature()
