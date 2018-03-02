from PyMCP2221A import PyMCP2221A

import time
gpio = PyMCP2221A.PyMCP2221A()

gpio.Reset()
time.sleep(1)
mcp2221 = PyMCP2221A.PyMCP2221A()
mcp2221.DAC_2_Init()
print('-'*20)
print('MCP2221(A) DAC Test')
print('-'*20)
print(" CTRL+C keys to exit.")

while 1:
    for i in range(0,0x0F,1) :
        mcp2221.DAC_Datawrite(i)
        time.sleep(0.01)