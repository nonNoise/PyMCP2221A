# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# BMX055
# This code is designed to work with the BMX055_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/products
# Fork @  https://github.com/ControlEverythingCommunity/BMX055/tree/master/Python

from PyMCP2221A import SMBus
import time

Addr_Accl = 0x19
Addr_Gyro = 0x69
Addr_Mag = 0x13

# Get I2C bus
bus = SMBus.SMBus()

# Select PMU_Range register, 0x0F(15)
#		0x03(03)	Range = +/- 2g
bus.write_byte_data(Addr_Accl, 0x0F, 0x03)
# Select PMU_BW register, 0x10(16)
#		0x08(08)	Bandwidth = 7.81 Hz
bus.write_byte_data(Addr_Accl, 0x10, 0x08)
# Select PMU_LPW register, 0x11(17)
#		0x00(00)	Normal mode, Sleep duration = 0.5ms
bus.write_byte_data(Addr_Accl, 0x11, 0x00)

time.sleep(0.5)

# Read data back from 0x02(02), 6 bytes
# xAccl LSB, xAccl MSB, yAccl LSB, yAccl MSB, zAccl LSB, zAccl MSB
data = bus.read_i2c_block_data(Addr_Accl, 0x02, 6)
print (data)
# Convert the data to 12-bits
xAccl = ((data[1] * 256) + (data[0] & 0xF0)) / 16
if xAccl > 2047 :
	xAccl -= 4096
yAccl = ((data[3] * 256) + (data[2] & 0xF0)) / 16
if yAccl > 2047 :
	yAccl -= 4096
zAccl = ((data[5] * 256) + (data[4] & 0xF0)) / 16
if zAccl > 2047 :
	zAccl -= 4096

# Select Range register, 0x0F(15)
#		0x04(04)	Full scale = +/- 125 degree/s
bus.write_byte_data(Addr_Gyro, 0x0F, 0x04)
# Select Bandwidth register, 0x10(16)
#		0x07(07)	ODR = 100 Hz
bus.write_byte_data(Addr_Gyro, 0x10, 0x07)
# Select LPM1 register, 0x11(17)
#		0x00(00)	Normal mode, Sleep duration = 2ms
bus.write_byte_data(Addr_Gyro, 0x11, 0x00)

time.sleep(0.5)

# Read data back from 0x02(02), 6 bytes
# xGyro LSB, xGyro MSB, yGyro LSB, yGyro MSB, zGyro LSB, zGyro MSB
data = bus.read_i2c_block_data(Addr_Gyro, 0x02, 6)

# Convert the data
xGyro = data[1] * 256 + data[0]
if xGyro > 32767 :
	xGyro -= 65536
yGyro = data[3] * 256 + data[2]
if yGyro > 32767 :
	yGyro -= 65536
zGyro = data[5] * 256 + data[4]
if zGyro > 32767 :
	zGyro -= 65536

# Select Mag register, 0x4B(75)
#		0x83(121)	Soft reset
bus.write_byte_data(Addr_Mag, 0x4B, 0x83)
# Select Mag register, 0x4C(76)
#		0x00(00)	Normal Mode, ODR = 10 Hz
bus.write_byte_data(Addr_Mag, 0x4C, 0x00)
# Select Mag register, 0x4E(78)
#		0x84(122)	X, Y, Z-Axis enabled
bus.write_byte_data(Addr_Mag, 0x4E, 0x84)
# Select Mag register, 0x51(81)
#		0x04(04)	No. of Repetitions for X-Y Axis = 9
bus.write_byte_data(Addr_Mag, 0x51, 0x04)
# Select Mag register, 0x52(82)
#		0x0F(15)	No. of Repetitions for Z-Axis = 15
bus.write_byte_data(Addr_Mag, 0x52, 0x0F)
time.sleep(0.5)
# Read data back from 0x42(66), 6 bytes
# X-Axis LSB, X-Axis MSB, Y-Axis LSB, Y-Axis MSB, Z-Axis LSB, Z-Axis MSB
data = bus.read_i2c_block_data(Addr_Mag, 0x42, 6)

# Convert the data
xMag = ((data[1] * 256) + (data[0] & 0xF8)) / 8
if xMag > 4095 :
	xMag -= 8192
yMag = ((data[3] * 256) + (data[2] & 0xF8)) / 8
if yMag > 4095 :
	yMag -= 8192
zMag = ((data[5] * 256) + (data[4] & 0xFE)) / 2
if zMag > 16383 :
	zMag -= 32768

# Output data to screen
print ("Acceleration in X-Axis : %d" %xAccl )
print ("Acceleration in Y-Axis : %d" %yAccl )
print ("Acceleration in Z-Axis : %d" %zAccl )
print ("X-Axis of Rotation : %d" %xGyro )
print ("Y-Axis of Rotation : %d" %yGyro )
print ("Z-Axis of Rotation : %d" %zGyro )
print ("Magnetic field in X-Axis : %d" %xMag )
print ("Magnetic field in Y-Axis : %d" %yMag )
print ("Magnetic field in Z-Axis : %d" %zMag )