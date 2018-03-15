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
        # BMX055 Accl I2C address is 0x18(24)
        self.Addr_Accl = 0x19
        # BMX055 Gyro I2C address is 0x68(104)
        self.Addr_Gyro = 0x69
        # BMX055 Mag I2C address is 0x10(16)
        self.Addr_Mag = 0x13
    def setup(self):
        wdata = [0]*2
        #----------------------------------------------------------------#
        wdata[0] = 0x0F  # Select PMU_Range register
        wdata[1] = 0x03  # Range = +/- 2g
        self.mcp2221.I2C_Write(self.Addr_Accl,wdata)  
        wdata[0] = 0x10   # Select PMU_BW register
        wdata[1] = 0x08   # Bandwidth = 7.81 Hz
        self.mcp2221.I2C_Write(self.Addr_Accl,wdata)  
        wdata[0] = 0x11 # Select PMU_LPW register
        wdata[1] = 0x00 # Normal mode, Sleep duration = 0.5ms
        self.mcp2221.I2C_Write(self.Addr_Accl,wdata)  
        #----------------------------------------------------------------#
        wdata[0] = 0x0F # Select Range register
        wdata[1] = 0x04  # Full scale = +/- 125 degree/s
        self.mcp2221.I2C_Write(self.Addr_Gyro,wdata)  
        wdata[0] = 0x10   # Select Bandwidth register
        wdata[1] = 0x07   # ODR = 100 Hz
        self.mcp2221.I2C_Write(self.Addr_Gyro,wdata)  
        wdata[0] = 0x11   # Select LPM1 register
        wdata[1] = 0x00   # Normal mode, Sleep duration = 2ms
        self.mcp2221.I2C_Write(self.Addr_Gyro,wdata)  
        #----------------------------------------------------------------#
        wdata[0] = 0x4B # Select Mag register
        wdata[1] = 0x83 # Soft reset
        self.mcp2221.I2C_Write(self.Addr_Mag,wdata)  
        wdata[0] = 0x4C   # Select Mag register
        wdata[1] = 0x00   # Normal Mode, ODR = 10 Hz
        self.mcp2221.I2C_Write(self.Addr_Mag,wdata)  
        wdata[0] = 0x4E   # Select Mag register
        wdata[1] = 0x84   # X, Y, Z-Axis enabled
        self.mcp2221.I2C_Write(self.Addr_Mag,wdata)  
        wdata[0] = 0x51 # Select Mag register
        wdata[1] = 0x04 # No. of Repetitions for X-Y Axis = 9
        self.mcp2221.I2C_Write(self.Addr_Mag,wdata)  
        wdata[0] = 0x52 # Select Mag register
        wdata[0] = 0x0F # No. of Repetitions for Z-Axis = 15
        self.mcp2221.I2C_Write(self.Addr_Mag,wdata)  
    def GetAcclData(self):
        #==================================================================#
        rdata = [0]*6
        for i in range(6):
            wdata = [0]
            wdata[0]= 2+i # Select data register
            self.mcp2221.I2C_Write(self.Addr_Accl,wdata)  
            # Read 6 bytes of data
            # xAccl lsb, xAccl msb, yAccl lsb, yAccl msb, zAccl lsb, zAccl msb
            rdata[i] = self.mcp2221.I2C_Read(self.Addr_Accl,1)[0]
        xAccl = ((rdata[1] * 256) + (rdata[0] & 0xF0)) / 16
        if (xAccl > 2047):
            xAccl -= 4096
        yAccl = ((rdata[3] * 256) + (rdata[2] & 0xF0)) / 16
        if (yAccl > 2047):
            yAccl -= 4096
        zAccl = ((rdata[5] * 256) + (rdata[4] & 0xF0)) / 16
        if (zAccl > 2047):
            zAccl -= 4096
        xAccl = xAccl * 0.0098  # renge +-2g
        yAccl = yAccl * 0.0098  # renge +-2g
        zAccl = zAccl * 0.0098  # renge +-2g
        return (round(xAccl,4),round(yAccl,4),round(zAccl,4))
        #==================================================================#
    def GetGyroData(self):
        rdata = [0]*6
        for i in range(6):
            wdata = [0]
            wdata[0]= 2+i # Select data register
            self.mcp2221.I2C_Write(self.Addr_Gyro,wdata)  
            # Read 6 bytes of data
            # xGyro lsb, xGyro msb, yGyro lsb, yGyro msb, zGyro lsb, zGyro msb
            rdata[i] = self.mcp2221.I2C_Read(self.Addr_Gyro,1)[0]
        xGyro = (rdata[1] * 256) + rdata[0]
        if (xGyro > 32767):
            xGyro -= 65536
        yGyro = (rdata[3] * 256) + rdata[2]
        if (yGyro > 32767):
            yGyro -= 65536;
        zGyro = (rdata[5] * 256) + rdata[4]
        if (zGyro > 32767):
            zGyro -= 65536
        xGyro = xGyro * 0.0038  #  Full scale = +/- 125 degree/s
        yGyro = yGyro * 0.0038  #  Full scale = +/- 125 degree/s
        zGyro = zGyro * 0.0038  #  Full scale = +/- 125 degree/s
        return (round(xGyro,4),round(yGyro,4),round(zGyro,4)) 
    def GetMegData(self):
        #==================================================================#
        rdata = [0]*6
        for i in range(6):
            wdata = [0]
            wdata[0]= 66+i # Select data register
            self.mcp2221.I2C_Write(self.Addr_Mag,wdata)  
            # Read 6 bytes of data
            # xMag lsb, xMag msb, yMag lsb, yMag msb, zMag lsb, zMag msb
            rdata[i] = self.mcp2221.I2C_Read(self.Addr_Mag,1)[0]
        xMag = ((rdata[1] * 256) + (rdata[0] & 0xF8)) / 8
        if (xMag > 4095):
            xMag -= 8192
        yMag = ((rdata[3] * 256) + (rdata[2] & 0xF8)) / 8
        if (yMag > 4095):
            yMag -= 8192
        zMag = ((rdata[5] * 256) + (rdata[4] & 0xFE)) / 2
        if (zMag > 16383):
            zMag -= 32768
        return (round(xMag,4),round(yMag,4),round(zMag,4))
