import PyMCP2221A
import time
mcp2221 = PyMCP2221A.PyMCP2221A()
mcp2221.Reset()
mcp2221 = PyMCP2221A.PyMCP2221A()
print('-'*20)
print('MCP2221(A) I2C Test')
print('-'*20)
print(" CTRL+C keys to exit.")

mcp2221.I2C_Init()
mcp2221.I2C_Read(0x50,1)

for i in range(0x00,0xff) :
    #print ('[0x{:02x}]'.format(i))
    #print(mcp2221.I2C_Read(i,0))
    if(i%8==0):
        print("")

    if(mcp2221.I2C_Read(i,0) == 0):
        print('0x{:02x}'.format(i), end='')
    else:
        print(' -- ', end='')

data =[0]

#mcp2221.I2C_Write(0x00,data)

#while 1:
#    mcp2221.I2C_Write(0x01,0x01)
#    time.sleep(1)
