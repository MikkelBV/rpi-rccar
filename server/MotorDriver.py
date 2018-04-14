import time, sys
import RPi.GPIO as GPIO
import smbus

bus = smbus.SMBus(1)

class MotorDriver:
    MotorSpeedSet	= 0x82
    PwMFrequenceSet	= 0x84
    DirectionSet	= 0xaa
    MotorSetA		= 0xa1
    MotorSetB		= 0xa5
    Nothing		= 0x01
    EnableStepper	= 0x1a
    UnenableStepper	= 0x1b
    Stepernu		= 0x1c
    I2CMotorDriverAdd	= 0x0f

    def __init__(self, address = 0x0f):
        self.I2CMotorDriverAdd = address

    def map_vals(self, value, leftMin, leftMax, rightMin, rightMax):
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin
        valueScaled = float(value - leftMin / float(leftSpan))
        return int(rightMin + (valueScaled * rightSpan))

    def MotorSpeedSetAB(self, MotorSpeedA, MotorSpeedB):
        MotorSpeedA = self.map_vals(MotorSpeedA, 0, 100, 0, 255)
        MotorSpeedB = self.map_vals(MotorSpeedB, 0, 100, 0, 255)
        bus.write_i2c_block_data(self.I2CMotorDriverAdd, self.MotorSpeedSet, [MotorSpeedA, MotorSpeedB])
        time.sleep(.02)

    def MotorDirectionSet(self, direction):
        bus.write_i2c_block_data(self.I2CMotorDriverAdd, self.DirectionSet, [direction, 0])
        time.sleep(.02)
