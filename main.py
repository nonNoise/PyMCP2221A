
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
# !!!! Don't care !!!!
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
# reset
#######################################################################
print ("Rseat")
h.write([0x00,0x70,0xAB,0xCD,0xEF])
#h.read(64)
