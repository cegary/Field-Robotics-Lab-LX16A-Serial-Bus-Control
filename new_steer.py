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

    
    servo_21.motor_mode(right_speed)
    servo_20.motor_mode(right_speed)
    servo_23.motor_mode(right_speed)
    _speed = [l, r]
    return _speed

def set_speed(s):
    s = max(min(1000, s), -1000)
    
    #left side
    servo_28.motor_mode(s)
    servo_22.motor_mode(s)
    servo_27.motor_mode(s)
    #right side
    servo_21.motor_mode(-1*s)
    servo_20.motor_mode(-1*s)
    servo_23.motor_mode(-1*s)
    return s

def turn(t):
    # *** RANGE [0-80] (set of angles -> center +/- 40) ***
    #26 front-left, center at 40, default = 40
    #24 front-right(X-X), center at XX, default = 40
    #29 back-left(X-X),  center at XX, default = 200
    #25 back-right(X-X), center at XX, default = 165
    t = max(min(40, t), -40)
    servo_24.move(fl + t)
    servo_25.move(bl + t)
    servo_26.move(fr + t)
    servo_29.move(br + t)
    return t




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
    servo_24.set_angle_offset(-15)

    servo_25.servo_mode()
    #servo_25.set_angle_limits(0, 240)
    servo_25.set_angle_offset(30)

    servo_29.servo_mode()
    #servo_29.enable_torque()
    #servo_29.set_angle_limits(0, 240)
    servo_29.set_angle_offset(0)

    servo_26.servo_mode()
    #servo_26.set_angle_limits(0, 240)
    servo_26.set_angle_offset(30)


    fl = 40
    fr = 40
    bl = 200
    br = 165
    servo_24.move(fl)
    servo_25.move(bl)
    servo_26.move(fr)
    servo_29.move(br)
    left_x=0.0
    left_y=0.0

# Loop to read inputs
run = True
speed = [0,0]
base_speed = 0
theta = 0
paused = False
servo_24.move(0)

while run:
    # Check for button press
    for event in pygame.event.get():

    # Check for button press
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")
            if event.button == 1:
                if paused:
                    print("Unpaused.")
                    paused = False
                else:
                    control_motors(0,0)
                    print("Paused.")
                    paused = True

    if not paused:
        left_y = joystick.get_axis(1)
        left_x = joystick.get_axis(0)
        
        theta = turn(left_x * 40)
        if abs(left_y) > 0.2:
            base_speed = int(left_y * 1000)
        else: base_speed = 0
        set_speed(base_speed)
                    
pygame.quit()
