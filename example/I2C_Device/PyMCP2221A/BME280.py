#############################################################
#    MIT License                                            #
#    Copyright (c) 2017 Yuta KItagami                       #
#############################################################
from PyMCP2221A import PyMCP2221A
import time

class BMX055 :
    def __init__(self,VID = 0x04D8,PID = 0x00DD,devnum = 0):
        self.mcp2221 = PyMCP2221A.PyMCP2221A()
        self.mcp2221.I2C_Init()
        self.self.I2CAddr =0x77
    def setup()
        dig_T1 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x89) << 8 + self.mcp2221.I2C_ReadReg(self.I2CAddr,0x88 )
        dig_T2 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x8B) << 8 + self.mcp2221.I2C_ReadReg(self.I2CAddr,0x8A )
        dig_T3 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x8D) << 8 + self.mcp2221.I2C_ReadReg(self.I2CAddr,0x8C )

        dig_P1 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x8F) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x8E )
        dig_P2 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x91) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x90 )
        dig_P3 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x93) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x92 )
        dig_P4 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x95) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x94 )
        dig_P5 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x97) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x96 )
        dig_P6 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x99) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x98 )
        dig_P7 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x9B) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x9A )
        dig_P8 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x9D) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x9C )
        dig_P9 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x9F) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x9E )

        dig_H1 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xA1 )
        dig_H2 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE2) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE1 )
        dig_H3 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE3 )
        dig_H4 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE4) << 4 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE5) & 0x0F 
        dig_H5 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE6) << 4 +   self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE5) >> 4) & 0x0F
        dig_H6 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE7 
    
    # Set the oversampling control words.
	# config will only be writeable in sleep mode, so first insure that.
	self.mcp2221.I2C_WriteReg(self.I2CAddr,0xF4, 0x00);
	
	# tStandby can be:
	# 0, 0.5ms: 1, 62.5ms: 2, 125ms: 3, 250ms: 4, 500ms: 5, 1000ms: 6, 10ms: 7, 20ms
	dataToWrite = (0 << 0x5) & 0xE0;
    # filter can be off or number of FIR coefficients to use:
	# 0, filter off; 1, coefficients = 2; 2, coefficients = 4; 3, coefficients = 8; 4, coefficients = 16
	dataToWrite |= (0 << 0x02) & 0x1C;
	self.mcp2221.I2C_WriteReg(self.I2CAddr,BME280_CONFIG_REG, dataToWrite);
	
	# Set ctrl_hum first, then ctrl_meas to activate ctrl_hum
    # humidOverSample can be:
	#  0, skipped
    #  1 through 5, oversampling *1, *2, *4, *8, *16 respectively
	dataToWrite = settings.humidOverSample & 0x07; //all other bits can be ignored
	self.mcp2221.I2C_WriteReg(self.I2CAddr,BME280_CTRL_HUMIDITY_REG, dataToWrite);
	
	# set ctrl_meas
	# First, set temp oversampling
	dataToWrite = (settings.tempOverSample << 0x5) & 0xE0;
	# Next, pressure oversampling
	dataToWrite |= (settings.pressOverSample << 0x02) & 0x1C;
	# Last, set mode
	dataToWrite |= (settings.runMode) & 0x03;
	# Load the byte
	self.mcp2221.I2C_WriteReg(self.I2CAddr,BME280_CTRL_MEAS_REG, dataToWrite);
	return readRegister(0xD0);