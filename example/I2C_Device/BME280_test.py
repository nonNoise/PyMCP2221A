#############################################################
#    MIT License                                            #
#    Copyright (c) 2017 Yuta KItagami                       #
#############################################################
from PyMCP2221A import BMX055

import time
print('-'*50)
print('MCP2221(A) BMX055 ')
print('-'*50)

bmx055 = BMX055.BMX055()
bmx055.setup()
while 1:
    print(bmx055.GetAcclData())
    print(bmx055.GetGyroData())
    print(bmx055.GetMegData())
    print("-"*10)
    time.sleep(1)