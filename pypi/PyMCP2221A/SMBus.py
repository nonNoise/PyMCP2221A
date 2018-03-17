#############################################################
#    MIT License                                            #
#    Copyright (c) 2017 Yuta KItagami                       #
#############################################################
from PyMCP2221A import PyMCP2221A
import time

#-------------------------------------------------------------#
# SMBus (system management bus) function compatible function  #
#-------------------------------------------------------------#
class SMBus :
    def __init__(self,VID = 0x04D8,PID = 0x00DD,devnum = 0):
        self.mcp2221 = PyMCP2221A.PyMCP2221A(VID,PID,devnum)
        self.mcp2221.I2C_Init()
    def read_byte(self, addrs):
        return self.mcp2221.I2C_Read(addrs,1)[0]
    def write_byte(self, addrs,val):
        self.mcp2221.I2C_Write(addrs,1,[val])
    def read_byte_data(self, addrs,cmd):
        self.mcp2221.I2C_Write_No_Stop(addrs,[cmd])
        return self.mcp2221.I2C_Read_Repeated(addrs,1)[0]
    def write_byte_data(self, addrs,cmd,val):
        self.mcp2221.I2C_Write(addrs,[cmd,val])
    def read_word_data(self, addrs,cmd):
        self.mcp2221.I2C_Write_No_Stop(addrs,[cmd])
        tmp = self.mcp2221.I2C_Read_Repeated(addrs,2)
        return tmp[0] | tmp[1]<<8
    def write_word_data(self, addrs,cmd,val):
        self.mcp2221.I2C_Write(addrs,[cmd,val&0x00FF,(val&0xFF00)>>8])
    def read_i2c_block_data(self, addrs,cmd,size):
        self.mcp2221.I2C_Write_No_Stop(addrs,[cmd])
        return self.mcp2221.I2C_Read_Repeated(addrs,size)
    def write_i2c_block_data(self, addrs,cmd,vals):
        self.mcp2221.I2C_Write(addrs,[cmd,va])
        
