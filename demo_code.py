import pygame
from math import sin, cos
from pylx16a.lx16a import *
import time

def control_motors(l, r):
    #print(f"Left Motors: {left_speed}, Right Motors: {right_speed}") 
    
    left_speed = max(min(1000, int(l)), -1000)
    right_speed = max(min(1000, -1 * int(r)), -1000)
    #left side
    servo_28.motor_mode(left_speed)
    servo_22.motor_mode(left_speed)
    servo_27.motor_mode(left_speed)

    #right side
    servo_21.motor_mode(right_speed)
    servo_20.motor_mode(right_speed)
    servo_23.motor_mode(right_speed)
    _speed = [l, r]
    return _speed


LX16A.initialize("COM12")
# Initialize pygame
pygame.init()
pygame.joystick.init()

# Check if a joystick is connected
if pygame.joystick.get_count() == 0:
    print("No controller connected!")

else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Controller connected: {joystick.get_name()}")


    #Motors
    servo_20 = LX16A(20)
    servo_20.enable_torque()

    servo_21 = LX16A(21)
    servo_21.enable_torque()

    servo_22 = LX16A(22)
    servo_22.enable_torque()

    servo_23 = LX16A(23)
    servo_23.enable_torque()

    servo_27 = LX16A(27)
    servo_27.enable_torque()

    servo_28 = LX16A(28)
    servo_28.enable_torque()

    #Servos
    servo_24 = LX16A(24)
    servo_25 = LX16A(25)
    servo_26 = LX16A(26)
    servo_29 = LX16A(29)

    servo_24.servo_mode()
    #servo_24.set_angle_limits(0, 240)
    servo_24.set_angle_offset(-30)

    servo_25.servo_mode()
    #servo_25.set_angle_limits(0, 240)
    servo_25.set_angle_offset(15)

    servo_29.servo_mode()
    #servo_29.enable_torque()
    #servo_29.set_angle_limits(0, 240)
    servo_29.set_angle_offset(15)

    servo_26.servo_mode()
    #servo_26.set_angle_limits(0, 240)
    servo_26.set_angle_offset(29)
    
    left_x=0.0
    left_y=0.0

# Loop to read inputs
run = True
speed = [0,0]
base_speed = 0
servo_24.move(0)

while run:
    # Check for button press
    for event in pygame.event.get():

    # Check for button press
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")
            if event.button == 1:
                control_motors(0,0)
                run = False
                break

    
    left_y = joystick.get_axis(1)
    left_x = joystick.get_axis(0)
    
    if left_y < -0.2: #foward
        base_speed = abs(left_y) * 1000 

        if left_x < -0.2:  # Turn Left
            left_motor = base_speed * 0.4  # Reduce left speed
            right_motor = base_speed  # Keep right motor full
        elif left_x > 0.2:  # Turn Right
            left_motor = base_speed  # Keep left motor full
            right_motor = base_speed * 0.4  # Reduce right speed
        else:  # Move straight
            left_motor = base_speed
            right_motor = base_speed

    elif left_y > 0.2: #backward
        base_speed = abs(left_y) * 1000 

        if left_x < -0.2:  # Turn Left
            left_motor = (-1*base_speed) * 0.4  # Reduce left speed
            right_motor = (-1*base_speed)  # Keep right motor full
        elif left_x > 0.2:  # Turn Right
            left_motor = (-1*base_speed)  # Keep left motor full
            right_motor = (-1*base_speed) * 0.4  # Reduce right speed
        else:  # Move straight
            left_motor = (-1*base_speed)
            right_motor = (-1*base_speed)

    elif left_x > 0.2: #turn right
        base_speed = abs(left_x) * 1000 
        left_motor = (base_speed) 
        right_motor = 0

    elif left_x < -0.2: #turn left
        base_speed = abs(left_x) * 1000 
        right_motor = (base_speed) 
        left_motor = 0

    else:
        base_speed = 0
        left_motor = base_speed
        right_motor = base_speed

    print(f"basespeed {base_speed}")
    speed = control_motors(left_motor, right_motor)
    
pygame.quit()