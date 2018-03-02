from PyMCP2221A import PyMCP2221A

import time
mcp2221 = PyMCP2221A.PyMCP2221A()
mcp2221.Reset()
mcp2221 = PyMCP2221A.PyMCP2221A()
print('-'*20)
print('MCP2221(A) I2C Test')
print('-'*20)
print(" CTRL+C keys to exit.")

mcp2221.I2C_Init()


for i in range(0,0xFFF,32):
    data=[0]*(32+2)
    data[0] = (0xFF00&i)>>8
    data[1] = 0xFF&i
    for n in range(0,32):
        data[n+2] = 0x00
    mcp2221.I2C_Write(0x50,data)
time.sleep(1)
print('-'*3 + " Clear " + '-'*3)
time.sleep(1)

for i in range(0x1F):
    data=[0]*2
    data[0] = (0xFF00&i)>>8
    data[1] = 0x00FF&i
    mcp2221.I2C_Write(0x50,data)
    rdata = mcp2221.I2C_Read(0x50,1)
    print ('0x{:02x}: 0x{:02x}'.format(i,rdata[0]))
print("-"*10)
time.sleep(1)


for i in range(0,0xFFF,32):
    data=[0]*(32+2)
    data[0] = (0xFF00&i)>>8
    data[1] = 0xFF&i
    for n in range(0,32):
        data[n+2] = 0xFF& n
    mcp2221.I2C_Write(0x50,data)
time.sleep(1)
print('-'*3 + " Write " + '-'*3)
time.sleep(1)


for i in range(0xFF):
    data=[0]*2
    data[0] = (0xFF00&i)>>8
    data[1] = 0x00FF&i
    mcp2221.I2C_Write(0x50,data)
    rdata = mcp2221.I2C_Read(0x50,1)
    print ('0x{:02x}: 0x{:02x}'.format(i,rdata[0]))

