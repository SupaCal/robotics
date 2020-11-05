# VEX IQ Python-Project
import sys
import vexiq

#region config
liftRightMotor = vexiq.Motor(1, True)
leftMotor      = vexiq.Motor(2)
rightMotor     = vexiq.Motor(4, True) # Reverse Polarity
clawMotor      = vexiq.Motor(7) # Reverse Polarity
middleMotor    = vexiq.Motor(9, True) # Reverse Polarity
liftLeftMotor  = vexiq.Motor(10) # Reverse Polarity
joystick       = vexiq.Joystick()
#endregion config
joystick.set_deadband(5)
while True:
    if joystick.axisC() == 0:
        leftMotor.run(joystick.axisA())
        rightMotor.run(joystick.axisA())
    elif joystick.axisD() < 10:
        rightMotor.run(joystick.axisC() * -1)
        leftMotor.run(joystick.axisC())
    middleMotor.run(joystick.axisB())
    liftRightMotor.run(joystick.axisD())
    liftLeftMotor.run(joystick.axisD())
    buttonDown = joystick.bLdown()
    buttonUp = joystick.bLup()
    if buttonDown and buttonUp:
        clawMotor.run(0)
    elif buttonDown:
        clawMotor.run(-100)
    elif buttonUp:
        clawMotor.run(100)
    else:
        clawMotor.run(0)
