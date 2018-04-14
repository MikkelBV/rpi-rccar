import time, sys
import RPi.GPIO as GPIO
import smbus

bus = smbus.SMBus(1)

class MotorDriver:
    MOTOR_SPEED_SET	    = 0x82
    PWM_FREQUENCY_SET	= 0x84
    DIRECTION_SET	    = 0xaa
    MOTOR_SET_A		    = 0xa1
    MOTOR_SET_B		    = 0xa5
    NOTHING		        = 0x01
    ENABLE_STEPPER	    = 0x1a
    DISABLE_STEPPER	    = 0x1b

    def __init__(self, address = 0x0f):
        self.I2CMotorDriverAdd = address

    def _map_vals(self, value, leftMin, leftMax, rightMin, rightMax):
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin
        valueScaled = float(value - leftMin / float(leftSpan))
        return int(rightMin + (valueScaled * rightSpan))

    def motor_speed_set(self, MotorSpeedA, MotorSpeedB):
        MotorSpeedA = self._map_vals(MotorSpeedA, 0, 100, 0, 255)
        MotorSpeedB = self._map_vals(MotorSpeedB, 0, 100, 0, 255)
        bus.write_i2c_block_data(self.I2CMotorDriverAdd, self.MOTOR_SPEED_SET, [MotorSpeedA, MotorSpeedB])
        time.sleep(.02)

    def motor_direction_set(self, direction):
        bus.write_i2c_block_data(self.I2CMotorDriverAdd, self.DIRECTION_SET, [direction, 0])
        time.sleep(.02)
