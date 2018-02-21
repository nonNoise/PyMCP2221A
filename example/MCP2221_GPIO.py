import PyMCP2221A
import time
gpio = PyMCP2221A.PyMCP2221A()

gpio.Reset()
time.sleep(1)
gpio = PyMCP2221A.PyMCP2221A()
gpio.GPIO_Init()
gpio.GPIO_0_OutputMode()

while 1:
    gpio.GPIO_0_Output(1)
    time.sleep(0.1)
    gpio.GPIO_0_Output(0)
    time.sleep(0.1)
    gpio.GPIO_1_Output(1)
    time.sleep(0.1)
    gpio.GPIO_1_Output(0)
    time.sleep(0.1)
    gpio.GPIO_2_Output(1)
    time.sleep(0.1)
    gpio.GPIO_2_Output(0)
    time.sleep(0.1)
    gpio.GPIO_3_Output(1)
    time.sleep(0.1)
    gpio.GPIO_3_Output(0)
    time.sleep(0.1)


