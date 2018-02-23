import PyMCP2221A
import time
gpio = PyMCP2221A.PyMCP2221A()

gpio.Reset()
time.sleep(1)
mcp2221 = PyMCP2221A.PyMCP2221A()
print('-'*20)
print('MCP2221(A) I2C Test')
print('-'*20)
print(" CTRL+C keys to exit.")

mcp2221.I2C_Init()
#mcp2221.I2C_Read(0x00)

data =[0]

mcp2221.I2C_Write(0x00,data)

#while 1:
#    mcp2221.I2C_Write(0x01,0x01)
#    time.sleep(1)
