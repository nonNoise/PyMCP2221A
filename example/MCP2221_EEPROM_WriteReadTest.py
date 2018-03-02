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

MAX = 0x00FF


for i in range(MAX):
    data=[0]*3
    data[0] = (0xFF00&i)>>8
    data[1] = 0xFF&i
    data[2] = 0x00
    mcp2221.I2C_Write(0x50,data)
print('-'*3 + " Clear " + '-'*3)
time.sleep(1)
for i in range(MAX):
    data=[0]*3
    data[0] = (0xFF00&i)>>8
    data[1] = 0xFF&i
    data[2] = 0xFF&i
    mcp2221.I2C_Write(0x50,data)
print('-'*3 + " Write " + '-'*3)
time.sleep(1)
for i in range(MAX):
    data=[0]*2
    data[0] = (0xFF00&i)>>8
    data[1] = 0x00FF&i
    mcp2221.I2C_Write(0x50,data)
    rdata = mcp2221.I2C_Read(0x50,1)
    if(rdata == -1):
        print("Error")
        exit()
    #print ('0x{:02x}: 0x{:02x}'.format(i,rdata[0]))
    if(rdata[0]!=(0xFF&i)):
        pass
        print ('0x{:02x}: 0x{:02x}'.format(i,rdata[0]))
    #time.sleep(0.01)
print('-'*3 + " Read " + '-'*3)
