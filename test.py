import PyMCP2221A
import time
gpio = PyMCP2221A.PyMCP2221A()

gpio.Reset()
time.sleep(1)
gpio = PyMCP2221A.PyMCP2221A()
gpio.GPIO_Init()
gpio.GPIO_0_OutputMode()

#print("--Init--")
#gpio.I2C_Init(26)
#print("--Status--")
#gpio.I2C_Status()

#print(gpio.I2C_Read_byte(0x3E))
#for i in range (20):
while 1:
    #print("--I2C Write--")
    #gpio.I2C_Write(0x3E<<1,0x05)
    #print("--Status--")
    #gpio.I2C_Status()
    #gpio.I2C_Read(0x3E,0x01)
    gpio.GPIO_0_Output(1)
    print(gpio.GPIO_0_Input())
    time.sleep(1)

    gpio.GPIO_0_Output(0)
    print(gpio.GPIO_0_Input())
    time.sleep(1)


