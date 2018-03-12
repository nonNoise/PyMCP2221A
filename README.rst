=====================================================
PyMCP2221A
=====================================================

What is.
----------------------------------------------------

This is a Microchip MCP2221(A) HID Library in python.

MCP2221 & MCP2221A work in Python. 

|

これはMCP2221(A)のHIDを使ったPythonライブラリーです。

MCP2221 と MCP2221A で動作します。


Install
----------------------------------------------------

This library uses hitapi.

    pip install hidapi

    https://github.com/trezor/cython-hidapi

PyMCP2221A Install

    pip install PyMCP2221A

Sample
----------------------------------------------------

import PyMCP2221A

mcp2221 = PyMCP2221A.PyMCP2221A()

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

    The MIT License (MIT) Copyright (c) 2017 Yuta KItagami (kitagami@artifactnoise.com,@nonnoise)
