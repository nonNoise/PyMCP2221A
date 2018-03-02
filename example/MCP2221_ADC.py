from PyMCP2221A import PyMCP2221A
import time
mcp2221 = PyMCP2221A.PyMCP2221A()

mcp2221.Reset()
time.sleep(1)
mcp2221 = PyMCP2221A.PyMCP2221A()
print('-'*20)
print('MCP2221(A) ADC Test')
print('-'*20)
print(" CTRL+C keys to exit.")

mcp2221.ADC_1_Init()
mcp2221.ADC_2_Init()
mcp2221.ADC_3_Init()
while 1:
    mcp2221.ADC_DataRead()
    print("----------------")
    print ('AD1: 0x{:02x}'.format(mcp2221.ADC_1_data))
    print ('AD2: 0x{:02x}'.format(mcp2221.ADC_2_data))
    print ('AD3: 0x{:02x}'.format(mcp2221.ADC_3_data))
    time.sleep(2)

