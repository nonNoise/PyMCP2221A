#############################################################
#    MIT License                                            #
#    Copyright (c) 2017 Yuta KItagami                       #
#############################################################
from PyMCP2221A import PyMCP2221A
import time

class BME280 :
    def __init__(self,I2CAddr =0x76,VID = 0x04D8,PID = 0x00DD,devnum = 0):
        self.mcp2221 = PyMCP2221A.PyMCP2221A(VID,PID,devnum)
        self.mcp2221.I2C_Init()
        self.I2CAddr = I2CAddr
        # defolt Setting
        self.mode = 0x11    # Normal mode
        self.osrs_t = 0x00  # Skipped (output set to 0x80000)
        self.osrs_p = 0x00  # Skipped (output set to 0x80000)
        self.osrs_h = 0x00  # Skipped (output set to 0x80000)
        self.filter = 0x00    # Filter coefficient Filter off
        self.t_sb = 0x00    # 0.5ms


    def SoftReset(self):
        self.mcp2221.I2C_WriteReg(self.I2CAddr,0xE0, 0xB6)
        time.sleep(0.1)
    def ReadCoefficients(self):
        self.dig_T1 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x89) << 8 + self.mcp2221.I2C_ReadReg(self.I2CAddr,0x88 )
        self.dig_T2 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x8B) << 8 + self.mcp2221.I2C_ReadReg(self.I2CAddr,0x8A )
        self.dig_T3 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x8D) << 8 + self.mcp2221.I2C_ReadReg(self.I2CAddr,0x8C )

        self.dig_P1 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x8F) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x8E )
        self.dig_P2 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x91) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x90 )
        self.dig_P3 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x93) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x92 )
        self.dig_P4 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x95) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x94 )
        self.dig_P5 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x97) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x96 )
        self.dig_P6 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x99) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x98 )
        self.dig_P7 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x9B) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x9A )
        self.dig_P8 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x9D) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x9C )
        self.dig_P9 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x9F) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0x9E )

        self.dig_H1 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xA1 )
        self.dig_H2 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE2) << 8 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE1 )
        self.dig_H3 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE3 )
        self.dig_H4 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE4) << 4 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE5) & 0x0F 
        self.dig_H5 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE6) << 4 +  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE5) >> 4 & 0x0F
        self.dig_H6 =  self.mcp2221.I2C_ReadReg(self.I2CAddr,0xE7)

    def SetSampling(self):

        data = self.osrs_h & 0x07
        print("Register 0xF2 [ctrl_hum] = 0x{:02x}".format(data))
        self.mcp2221.I2C_WriteReg(self.I2CAddr,0xF2,data)
        data = self.t_sb<<5 | self.filter<<2
        print("Register 0xF5 [config] = 0x{:02x}".format(data))
        self.mcp2221.I2C_WriteReg(self.I2CAddr,0xF5, data)
        data = self.osrs_t<<5 | self.osrs_p<<2 | self.mode<<0
        print("Register 0xF4 [ctrl_meas] = 0x{:02x}".format(data))
        self.mcp2221.I2C_WriteReg(self.I2CAddr,0xF4,data);
    def ReadTemperature(self):
        adc_T = self.mcp2221.I2C_ReadReg(self.I2CAddr,0xFC)>>4
        adc_T = adc_T |self.mcp2221.I2C_ReadReg(self.I2CAddr,0xFA)<<12
        print("0x{:02x}".format(adc_T))
        if(adc_T == 0x80000):
            print("NAN")

        var1 = (((adc_T>>3) - (self.dig_T1 <<1)) *(self.dig_T2)) >> 11             
        var2 = (((((adc_T>>4) - (self.dig_T1)) *((adc_T>>4) - (self.dig_T1))) >> 12) * (self.dig_T3)) >> 14
        t_fine = var1 + var2
        T = (t_fine * 5 + 128) >> 8
        print( T/100.00)
        return T/100.00;
