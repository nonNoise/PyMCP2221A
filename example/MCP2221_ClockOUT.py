from PyMCP2221A import PyMCP2221A

import time
mcp2221 = PyMCP2221A.PyMCP2221A()
#mcp2221.Reset()
#time.sleep(1)

mcp2221 = PyMCP2221A.PyMCP2221A()
print('-'*20)
print('MCP2221(A) ClockOut Test')
print('-'*20)

#========================================#
#   CLKDUTY_0   # duty 0%
#   CLKDUTY_25  # duty 25%
#   CLKDUTY_50  # duty 50%
#   CLKDUTY_75  # duty 75%
#   --------------------------------   #
#   CLKDIV_2    # 24MHz
#   CLKDIV_4    # 12MHz
#   CLKDIV_8    # 6MHz
#   CLKDIV_16   # 3MHz
#   CLKDIV_32   # 1.5MHz
#   CLKDIV_64   # 750KHz
#   CLKDIV_128  # 375KHz
#========================================#
mcp2221.ClockOut(mcp2221.CLKDUTY_50,mcp2221.CLKDIV_4)



