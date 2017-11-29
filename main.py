
import hid
# pip install hidapi
# https://github.com/trezor/cython-hidapi


# Microchip MCP2221A
VID = 0x04D8 
PID = 0x00DD



h = hid.device()
h.open(VID,PID)

#######################################################################
# Command Structure
#######################################################################
I2C_Cancel_Bit = 0
I2C_Speed_SetUp_Bit = 0
I2C_Speed_SetVal_Byte = 0
buf = [0x00,0x10,0x00,I2C_Cancel_Bit<<4,I2C_Speed_SetUp_Bit<<5,I2C_Speed_SetVal_Byte]
buf = buf + [0 for i in range(65-len(buf))]
#print ("Write")
#print (buf)
h.write(buf)
buf = h.read(65)
#print ("Read")
#print (buf)

print (chr(buf[46]))
print (chr(buf[47]))
print (chr(buf[48]))
print (chr(buf[49]))
#######################################################################
# Read Flash Data
#######################################################################
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
h.write(buf)
buf = h.read(65)
#print ("Read")
#print (buf)
#######################################################################
# Write Flash Data
#######################################################################
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
# Write SRAM Data
#######################################################################
buf = [0x00,0x60]
buf = buf + [0 for i in range(65-len(buf))]
#buf[2+1] = 0x00     #   Clock Output Divider value
#buf[3+1] = 0x00     #   DAC Voltage Reference
#buf[4+1] = 0x00     #   Set DAC output value
#buf[5+1] = 0x00     #   ADC Voltage Reference
#buf[6+1] = 0x00     #   Setup the interrupt detection mechanism and clear the detection flag
buf[7+1] = 0x80     #   Alter GPIO configuration: alters the current GP designation
                    #   datasheet says this should be 1, but should actually be 0x80

GPIO_0_BIT = 1      # 1:Hi 0:LOW
GPIO_0_DIR = 0      # 0:OutPut 1:Input
GPIO_0_MODE = 0x00  # GPIO MODE = 0x00 
buf[8+1] = GPIO_0_BIT<<4 | GPIO_0_DIR<<3 | GPIO_0_MODE       #   GP0 settings
GPIO_1_BIT = 1      # 1:Hi 0:LOW
GPIO_1_DIR = 0      # 0:OutPut 1:Input
GPIO_1_MODE = 0x00  # GPIO MODE = 0x00 
buf[9+1] = GPIO_1_BIT<<4 | GPIO_1_DIR<<3 | GPIO_1_MODE       #   GP0 settings
GPIO_2_BIT = 0      # 1:Hi 0:LOW
GPIO_2_DIR = 0      # 0:OutPut 1:Input
GPIO_2_MODE = 0x00  # GPIO MODE = 0x00 
buf[10+1] = GPIO_2_BIT<<4 | GPIO_2_DIR<<3 | GPIO_2_MODE       #   GP0 settings
GPIO_3_BIT = 0      # 1:Hi 0:LOW
GPIO_3_DIR = 0      # 0:OutPut 1:Input
GPIO_3_MODE = 0x00  # GPIO MODE = 0x00 
buf[11+1] = GPIO_3_BIT<<4 | GPIO_3_DIR<<3 | GPIO_3_MODE       #   GP0 settings

#print ("Write")
#print (buf)
h.write(buf)
buf = h.read(65)
#print ("Read")
#print (buf)

#######################################################################
# Read GPIO Data
#######################################################################
buf = [0x00,0x51]
buf = buf + [0 for i in range(65-len(buf))]
print ("Write")
print (buf)
h.write(buf)
buf = h.read(65)
GPIO_0_INPUT =  buf[2]
GPIO_0_DIR   =  buf[3]
GPIO_1_INPUT =  buf[4]
GPIO_1_DIR   =  buf[5]
GPIO_2_INPUT =  buf[6]
GPIO_2_DIR   =  buf[7]
GPIO_3_INPUT =  buf[8]
GPIO_3_DIR   =  buf[9]
print ("Read")
print (buf)
print (GPIO_0_INPUT)
print (GPIO_0_DIR)
print (GPIO_1_INPUT)
print (GPIO_1_DIR)
print (GPIO_2_INPUT)
print (GPIO_2_DIR)
print (GPIO_3_INPUT)
print (GPIO_3_DIR)


#######################################################################
# SET GPIO OUTPUT VALUES
#######################################################################
#buf = [0x00,0x50]
#buf = buf + [0 for i in range(65-len(buf))]
#buf[2+1] = 0x01     #   Clock Output Divider value
#buf[3+1] = 0x00     #   DAC Voltage Reference
#buf[4+1] = 0x00     #   Set DAC output value
#buf[5+1] = 0x00     #   ADC Voltage Reference
#buf[6+1] = 0x00     #   Setup the interrupt detection mechanism and clear the detection flag
#buf[7+1] = 0x00     #   Alter GPIO configuration: alters the current GP designation
#buf[8+1] = 0x00     #   GP0 settings
#buf[9+1] = 0x00     #   GP1 settings
#buf[10+1] = 0x00    #   GP2 settings
#buf[11+1] = 0x00    #   GP3 settings
#buf[12+1] = 0x00    #   GP3 settings
#buf[13+1] = 0x00    #   GP3 settings
#buf[14+1] = 0x00    #   GP3 settings
#buf[15+1] = 0x00    #   GP3 settings
#buf[16+1] = 0x00    #   GP3 settings
#buf[17+1] = 0x00    #   GP3 settings




#######################################################################
# reset
#######################################################################
#print ("Rseat")
#h.write([0x00,0x70,0xAB,0xCD,0xEF])
#h.read(64)
