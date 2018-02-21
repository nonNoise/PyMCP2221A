import PyMCP2221A
import time
gpio = PyMCP2221A.PyMCP2221A()

gpio.Reset()
time.sleep(1)
mcp2221 = PyMCP2221A.PyMCP2221A()
mcp2221.GPIO_Init()
mcp2221.GPIO_0_OutputMode()

print(mcp2221.CLKDUTY_50)
print(mcp2221.CLKDIV_32)
print ('0x{:02x}'.format(mcp2221.CLKDUTY_50))
print ('0x{:02x}'.format(mcp2221.CLKDIV_32))

mcp2221.ClockOut(mcp2221.CLKDUTY_50,mcp2221.CLKDIV_128);
    #mcp2221.GPIO_0_Output(1)
    #time.sleep(0.1)
    #mcp2221.GPIO_0_Output(0)
    #time.sleep(0.1)


