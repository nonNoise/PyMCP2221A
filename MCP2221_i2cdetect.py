#############################################################
#    MIT License                                            #
#    Copyright (c) 2017 Yuta KItagami                       #
#############################################################
import PyMCP2221A
import time
print('-'*50)
print('MCP2221(A) i2cdetect ')
print('-'*50)
mcp2221 = PyMCP2221A.PyMCP2221A()
mcp2221.Reset()
mcp2221 = PyMCP2221A.PyMCP2221A()

mcp2221.I2C_Init()
#print(mcp2221.I2C_Write(0x10,[0]))
#print(mcp2221.I2C_Write(0x19,[0]))
#print(mcp2221.I2C_Write(0x53,[0]))
#print(mcp2221.I2C_Write(0x53,[0]))
#print(mcp2221.I2C_Read(0x19,1))
#mcp2221.I2C_Cancel()
#print(mcp2221.I2C_Write(0x19,[]))
#print(mcp2221.I2C_Write(0x13,[]))
print(mcp2221.I2C_Write(0x14,[]))
print(mcp2221.I2C_Write(0x14,[]))
print(mcp2221.I2C_Write(0x13,[]))
#print(mcp2221.I2C_Write(0x69,[]))

exit()
print("   0   1   2   3   4   5   6   7   8   9   A   B   C   D   E   F  ")
for i in range(0x00,0x7F) :
    if(i%16==0 and i>0):
        print("   {:02X}".format(i-1))

    if(mcp2221.I2C_Write(i,[]) != -1):
        print('  {:02x}'.format(i), end='')
    else:
        print('  --', end='')
    #time.sleep(0.1)

print("")


