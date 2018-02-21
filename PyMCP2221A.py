
import hid
# pip install hidapi
# https://github.com/trezor/cython-hidapi
import time

class PyMCP2221A :
    def __init__(self,VID = 0x04D8,PID = 0x00DD):
        self.mcp2221a = hid.device()
        self.mcp2221a.open(VID,PID)
        self.CLKDUTY_0 = 0x00
        self.CLKDUTY_25 = 0x08
        self.CLKDUTY_50 = 0x10
        self.CLKDUTY_75 = 0x18

        self.CLKDIV_1 = 0x00    # 48MHz
        self.CLKDIV_2 = 0x01    # 24MHz
        self.CLKDIV_4 = 0x02    # 12MHz
        self.CLKDIV_8 = 0x03    # 6MHz
        self.CLKDIV_16 = 0x04   # 3MHz
        self.CLKDIV_32 = 0x05   # 1.5MHz
        self.CLKDIV_64 = 0x06   # 750KHz
        self.CLKDIV_128 = 0x07  # 375KHz


#######################################################################
# Command Structure
#######################################################################
    def Command_Structure(self,I2C_Cancel_Bit,I2C_Speed_SetUp_Bit,I2C_Speed_SetVal_Byte):
        I2C_Cancel_Bit = 0
        I2C_Speed_SetUp_Bit = 0
        I2C_Speed_SetVal_Byte = 0
        buf = [0x00,0x10,0x00,I2C_Cancel_Bit<<4,I2C_Speed_SetUp_Bit<<5,I2C_Speed_SetVal_Byte]
        buf = buf + [0 for i in range(65-len(buf))]
        self.mcp2221a.write(buf)
        buf = self.mcp2221a.read(65)

        print (chr(buf[46]))
        print (chr(buf[47]))
        print (chr(buf[48]))
        print (chr(buf[49]))
#######################################################################
# Read Flash Data
#######################################################################
    def Read_Flash_Data(self,Read_Deta_Setting_Byte):
        Read_Deta_Setting_Byte = 0x00
        #Read_Chip_Settings             = 0x00
        #Read_GP_Settings               = 0x01
        #Read_USB_Manufacturer_Settings = 0x02
        #Read_USB_Product_Settings      = 0x03
        #Read_USB_SerialNum_Settings    = 0x04
        #Read_Chip_Factory_Settings     = 0x05
        buf = [0x00,0xB0,Read_Deta_Setting_Byte]
        buf = buf + [0 for i in range(65-len(buf))]
        #print ("Write")
        #print (buf)
        self.mcp2221a.write(buf)
        buf = self.mcp2221a.read(65)
        #print ("Read")
        #print (buf)
#######################################################################
# Write Flash Data
#######################################################################
    def Write_Flash_Data(self,data):
        pass
        #Write_Deta_Setting_Byte = 0x00
        #Write_Chip_Settings             = 0x00
        #Write_GP_Settings               = 0x01
        #Write_USB_Manufacturer_Settings = 0x02
        #Write_USB_Product_Settings      = 0x03
        #Write_USB_SerialNum_Settings    = 0x04
        #buf = [0x00,0xB1,Write_Deta_Setting_Byte]
        #buf = buf + [0 for i in range(65-len(buf))]
        # !!!! Be careful when making changes !!!!
        #buf[6+1] =  0xD8    # VID (Lower)
        #buf[7+1] =  0x04    # VID (Higher)
        #buf[8+1] =  0xDD    # PID (Lower)
        #buf[9+1] =  0x00    # PID (Higher)

        #print ("Write")
        #print (buf)
        #h.write(buf)
        #buf = h.read(65)
        #print ("Read")
        #print (buf)

#######################################################################
# GPIO Init
#######################################################################
    def GPIO_Init(self):
        buf = [0x00,0x61]
        buf = buf + [0 for i in range(65-len(buf))]
        #self.mcp2221a.write(buf)
        #rbuf = self.mcp2221a.read(65)

        buf = [0x00,0x60]
        buf = buf + [0 for i in range(65-len(buf))]
        #buf[2+1] = 0x00     #   Clock Output Divider value
        #buf[3+1] = 0x00     #   DAC Voltage Reference
        #buf[4+1] = 0x00     #   Set DAC output value
        #buf[5+1] = 0x00     #   ADC Voltage Reference
        #buf[6+1] = 0x00     #   Setup the interrupt detection mechanism and clear the detection flag
        buf[7+1] = 0x80     #   Alter GPIO configuration: alters the current GP designation
                            #   datasheet says this should be 1, but should actually be 0x80

        self.GPIO_0_BIT = 0#(rbuf[22]>>4)&0x01      # 1:Hi 0:LOW
        self.GPIO_0_DIR = 0#(rbuf[22]>>3)&0x01      # 0:OutPut 1:Input
        self.GPIO_0_MODE =0# rbuf[22]&0x07  # GPIO MODE = 0x00 
        self.GPIO_1_BIT = 0#(rbuf[23]>>4)&0x01      # 1:Hi 0:LOW
        self.GPIO_1_DIR = 0#(rbuf[23]>>3)&0x01      # 0:OutPut 1:Input
        self.GPIO_1_MODE =0# rbuf[23]&0x07  # GPIO MODE = 0x00 
        self.GPIO_2_BIT = 0#(rbuf[24]>>4)&0x01      # 1:Hi 0:LOW
        self.GPIO_2_DIR = 0#(rbuf[24]>>3)&0x01      # 0:OutPut 1:Input
        self.GPIO_2_MODE = 0#rbuf[24]&0x07  # GPIO MODE = 0x00 
        self.GPIO_3_BIT = 0#(rbuf[25]>>4)&0x01      # 1:Hi 0:LOW
        self.GPIO_3_DIR = 0#(rbuf[25]>>3)&0x01      # 0:OutPut 1:Input
        self.GPIO_3_MODE = 0#rbuf[25]&0x07  # GPIO MODE = 0x00 
        
        #for(i in range(64)):
        #    buf[i] = rbuf[i] | buf[i]
        self.mcp2221a.write(buf)
        buf = self.mcp2221a.read(65)


#######################################################################
# GPIO Write command
#######################################################################
    def GPIO_Write(self):
        buf = [0x00,0x60]
        buf = buf + [0 for i in range(65-len(buf))]
        #buf[2+1] = 0x00     #   Clock Output Divider value
        #buf[3+1] = 0x00     #   DAC Voltage Reference
        #buf[4+1] = 0x00     #   Set DAC output value
        #buf[5+1] = 0x00     #   ADC Voltage Reference
        #buf[6+1] = 0x00     #   Setup the interrupt detection mechanism and clear the detection flag
        buf[7+1] = 0x80     #   Alter GPIO configuration: alters the current GP designation
                            #   datasheet says this should be 1, but should actually be 0x80

        buf[8+1] =  self.GPIO_0_BIT<<4 | self.GPIO_0_DIR<<3 | self.GPIO_0_MODE       #   GP0 settings
        buf[9+1] =  self.GPIO_1_BIT<<4 | self.GPIO_1_DIR<<3 | self.GPIO_1_MODE       #   GP0 settings
        buf[10+1] = self.GPIO_2_BIT<<4 | self.GPIO_2_DIR<<3 | self.GPIO_2_MODE       #   GP0 settings
        buf[11+1] = self.GPIO_3_BIT<<4 | self.GPIO_3_DIR<<3 | self.GPIO_3_MODE       #   GP0 settings
        #print (buf)
        #for(i in range(64)):
        #    buf[i] = rbuf[i] | buf[i]
        self.mcp2221a.write(buf)
        rbuf = self.mcp2221a.read(65)

#######################################################################
# Read GPIO Data command
#######################################################################
    def GPIO_Read(self):
        buf = [0x00,0x51]
        buf = buf + [0 for i in range(65-len(buf))]
        self.mcp2221a.write(buf)
        buf = self.mcp2221a.read(65)
        self.GPIO_0_INPUT =  buf[2]
        self.GPIO_0_DIR   =  buf[3]
        self.GPIO_1_INPUT =  buf[4]
        self.GPIO_1_DIR   =  buf[5]
        self.GPIO_2_INPUT =  buf[6]
        self.GPIO_2_DIR   =  buf[7]
        self.GPIO_3_INPUT =  buf[8]
        self.GPIO_3_DIR   =  buf[9]

#######################################################################
# GPIO Outpu/Input Data
#######################################################################
    def GPIO_0_Output(self,bit):
        self.GPIO_0_BIT = bit # 1:Hi 0:LOW
        self.GPIO_0_DIR = 0 # 0:OutPut 1:Input
        self.GPIO_0_MODE = 0 #  0:GPIO
        self.GPIO_Write()
    def GPIO_0_InputMode(self):
        self.GPIO_0_DIR = 1 # 0:OutPut 1:Input
        self.GPIO_Write()
    def GPIO_0_OutputMode(self):
        self.GPIO_0_DIR = 0 # 0:OutPut 1:Input
        self.GPIO_Write()
    def GPIO_0_Input(self):
        self.GPIO_Read()
        return self.GPIO_0_INPUT, self.GPIO_0_DIR

    def GPIO_1_Output(self,bit):
        self.GPIO_1_BIT = bit # 1:Hi 0:LOW
        self.GPIO_1_DIR = 0 # 0:OutPut 1:Input
        self.GPIO_1_MODE = 0 #  0:GPIO
        self.GPIO_Write()
    def GPIO_1_InputMode(self):
        self.GPIO_1_DIR = 1 # 0:OutPut 1:Input
        self.GPIO_Write()
    def GPIO_1_OutputMode(self):
        self.GPIO_1_DIR = 0 # 0:OutPut 1:Input
        self.GPIO_Write()
    def GPIO_1_Input(self):
        self.GPIO_Read()
        return self.GPIO_1_INPUT, self.GPIO_1_DIR

    def GPIO_2_Output(self,bit):
        self.GPIO_2_BIT = bit # 1:Hi 0:LOW
        self.GPIO_2_DIR = 0 # 0:OutPut 1:Input
        self.GPIO_2_MODE = 0 #  0:GPIO
        self.GPIO_Write()
    def GPIO_2_InputMode(self):
        self.GPIO_2_DIR = 1 # 0:OutPut 1:Input
        self.GPIO_Write()
    def GPIO_2_OutputMode(self):
        self.GPIO_2_DIR = 0 # 0:OutPut 1:Input
        self.GPIO_Write()
    def GPIO_2_Input(self):
        self.GPIO_Read()
        return self.GPIO_2_INPUT, self.GPIO_2_DIR

    def GPIO_3_Output(self,bit):
        self.GPIO_3_BIT = bit # 1:Hi 0:LOW
        self.GPIO_3_DIR = 0 # 0:OutPut 1:Input
        self.GPIO_3_MODE = 0 #  0:GPIO
        self.GPIO_Write()
    def GPIO_3_InputMode(self):
        self.GPIO_3_DIR = 1 # 0:OutPut 1:Input
        self.GPIO_Write()
    def GPIO_3_OutputMode(self):
        self.GPIO_3_DIR = 0 # 0:OutPut 1:Input
        self.GPIO_Write()
    def GPIO_3_Input(self):
        self.GPIO_Read()
        return self.GPIO_3_INPUT, self.GPIO_3_DIR




#######################################################################
# Clock Out Value & Duty
#######################################################################
    def ClockOut(self,duty,value):
        buf = [0x00,0x61]
        buf = buf + [0 for i in range(65-len(buf))]
        self.mcp2221a.write(buf)
        rbuf = self.mcp2221a.read(65)
        
        buf = [0x00,0x60]
        buf = buf + [0 for i in range(65-len(buf))]
        buf[2+1] = 0x80 | duty | (0x07&value)    #   Clock Output Divider value
        buf[3+1] = rbuf[3+1]     #   DAC Voltage Reference
        buf[4+1] = rbuf[4+1]     #   Set DAC output value
        buf[5+1] = rbuf[5+1]     #   ADC Voltage Reference
        buf[6+1] = rbuf[6+1]     #   Setup the interrupt detection mechanism and clear the detection flag
        buf[7+1] = 0x80     #   Alter GPIO configuration: alters the current GP designation
                            #   datasheet says this should be 1, but should actually be 0x80
        buf[8+1] = rbuf[8+1]     #   GP0 settings
        buf[9+1] = 0x01     #   GP1 settings
        buf[10+1] = rbuf[10+1]    #   GP2 settings
        buf[11+1] = rbuf[11+1]    #   GP3 settings
        self.mcp2221a.write(buf)
        buf = self.mcp2221a.read(65)
        

#######################################################################
# I2C Init
#######################################################################
    def I2C_Init(self,speed):
        buf = [0x00,0x10]
        buf = buf + [0 for i in range(65-len(buf))]
        buf[2+1] = 0x10 #Cancel current I2C/SMBus transfer (sub-command)
        self.mcp2221a.write(buf)
        rbuf = self.mcp2221a.read(65)
        for i in range(len(rbuf)):
            print(hex(rbuf[i]),end=',')
        print()
        print(rbuf)
        time.sleep(1)
        buf = [0x00,0x10]
        buf = buf + [0 for i in range(65-len(buf))]
        buf[2+1] = 0x00 #Cancel current I2C/SMBus transfer (sub-command)
        buf[3+1] = 0x20 #Set I2C/SMBus communication speed (sub-command)
        buf[4+1] = 26#speed #The I2C/SMBus system clock divider that will be used to establish the communication speed
        self.mcp2221a.write(buf)
        rbuf = self.mcp2221a.read(65)
        for i in range(len(rbuf)):
            print(hex(rbuf[i]),end=',')
        print()
        print(rbuf[8])
        print(hex(rbuf[14]))
        print(hex(rbuf[22]))
        print(hex(rbuf[46]))
        
        print(rbuf)
#######################################################################
# I2C Write
#######################################################################
    def I2C_Status(self):
        buf = [0x00,0x10]
        buf = buf + [0 for i in range(65-len(buf))]
        buf[3+1] = 0x20 #Set I2C/SMBus communication speed (sub-command)
        buf[4+1] = 26#speed #The I2C/SMBus system clock divider that will be used to establish the communication speed
        self.mcp2221a.write(buf)
        rbuf = self.mcp2221a.read(65)
        for i in range(len(rbuf)):
            print(hex(rbuf[i]),end=',')
        print()
        print(rbuf)
#######################################################################
# I2C Write
#######################################################################
    def I2C_Write(self,addrs,byte):
        buf = [0x00,0x90]
        buf = buf + [0 for i in range(65-len(buf))]
        buf[2+1] = (byte&0x00FF) #Cancel current I2C/SMBus transfer (sub-command)
        buf[3+1] = (byte&0xFF00)>>8 #Set I2C/SMBus communication speed (sub-command)
        buf[4+1] = addrs #The I2C/SMBus system clock divider that will be used to establish the communication speed
        self.mcp2221a.write(buf)
        rbuf = self.mcp2221a.read(65)
        for i in range(len(rbuf)):
            print(hex(rbuf[i]),end=',')
        print()
        print(rbuf)
#######################################################################
# I2C Read
#######################################################################
    def I2C_Read(self,addrs,byte):
        buf = [0x00,0x91]
        buf = buf + [0 for i in range(65-len(buf))]
        buf[2+1] = (byte&0x00FF) #Cancel current I2C/SMBus transfer (sub-command)
        buf[3+1] = (byte&0xFF00)>>8 #Set I2C/SMBus communication speed (sub-command)
        buf[4+1] = addrs #The I2C/SMBus system clock divider that will be used to establish the communication speed
        self.mcp2221a.write(buf)
        rbuf = self.mcp2221a.read(65)
        print (hex(rbuf[0]))
        print (rbuf)

    def I2C_Read_RepetedStart(self,addrs,byte):
        buf = [0x00,0x93]
        buf = buf + [0 for i in range(65-len(buf))]
        buf[2+1] = (byte&0x00FF) #Cancel current I2C/SMBus transfer (sub-command)
        buf[3+1] = (byte&0xFF00)>>8 #Set I2C/SMBus communication speed (sub-command)
        buf[4+1] = addrs #The I2C/SMBus system clock divider that will be used to establish the communication speed
        self.mcp2221a.write(buf)
        rbuf = self.mcp2221a.read(65)
        print (hex(rbuf[0]))
        print (rbuf)

    def I2C_Read_byte(self,addrs):
        buf = [0x00,0x91]
        buf = buf + [0 for i in range(65-len(buf))]
        buf[2+1] = 0x01 #Cancel current I2C/SMBus transfer (sub-command)
        buf[3+1] = 0x00 #Set I2C/SMBus communication speed (sub-command)
        buf[4+1] = addrs #The I2C/SMBus system clock divider that will be used to establish the communication speed
        self.mcp2221a.write(buf)
        rbuf = self.mcp2221a.read(65)

        buf = [0x00,0x40]
        buf = buf + [0 for i in range(65-len(buf))]
        self.mcp2221a.write(buf)
        rbuf = self.mcp2221a.read(65)
        print (hex(rbuf[0]))
        print (rbuf)
        return rbuf[4]

#######################################################################
# reset
#######################################################################
    def Reset(self):
        print ("Rseat")
        buf = [0x00,0x70,0xAB,0xCD,0xEF]
        buf = buf + [0 for i in range(65-len(buf))]
        self.mcp2221a.write(buf)