=====================================================
PyMCP2221A
=====================================================

What is.
----------------------------------------------------

This is a Microchip MCP2221(A) HID Library in python.

MCP2221 & MCP2221A work in Python. 

|

日本語はこちら

https://github.com/nonNoise/PyMCP2221A/blob/master/README_JP.rst

Install
----------------------------------------------------

PyMCP2221A Install

    pip install PyMCP2221A

or

    git clone https://github.com/nonNoise/PyMCP2221A.git

    cd pypi

    sudo python setup.py build

    sudo python setup.py install



Sample
----------------------------------------------------

from PyMCP2221A import PyMCP2221A

mcp2221 = PyMCP2221A.PyMCP2221A()

and More. SMBus (system management bus) compatible function 
----------------------------------------------------

from PyMCP2221A import SMBus 

bus = SMBus.SMBus()


Setup
----------------------------------------------------

.. image:: ./img/mcp2221.PNG

Example
----------------------------------------------------

- MCP2221 ADC : OK :

    https://github.com/nonNoise/PyMCP2221A/blob/master/example/MCP2221_ADC.py

- MCP2221 DAC : OK :

    https://github.com/nonNoise/PyMCP2221A/blob/master/example/MCP2221_DAC.py    

- MCP2221 GPIO : OK :

    https://github.com/nonNoise/PyMCP2221A/blob/master/example/MCP2221_GPIO.py

- MCP2221 Interrupt : No :

- MCP2221 Clock : OK :

    https://github.com/nonNoise/PyMCP2221A/blob/master/example/MCP2221_ClockOUT.py

- MCP2221 I2C  : OK :

    https://github.com/nonNoise/PyMCP2221A/blob/master/example/MCP2221_i2cdetect.py

    https://github.com/nonNoise/PyMCP2221A/blob/master/example/MCP2221_EEPROM_WriteReadTest.py




License
----------------------------------------------------

    The MIT License (MIT) Copyright (c) 2017 Yuta Kitagami (kitagami@artifactnoise.com,@nonnoise)
