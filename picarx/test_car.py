from picarx_improved import Picarx
import time

def main():
    px = Picarx()

    print("Testing car movements...")

    # Move forward
    print("Moving forward...")
    px.set_dir_servo_angle(0)
    px.forward(50)
    time.sleep(2)

    # Turn left and move forward
    print("Turning left...")
    px.set_dir_servo_angle(-15)
    px.forward(50)
    time.sleep(2)

    # Turn right and move forward
    print("Turning right...")
    px.set_dir_servo_angle(15)
    px.forward(50)
    time.sleep(2)

    # Stop motors manually by setting speed to 0
    print("Stopping...")
    px.set_motor_speed(1, 0)
    px.set_motor_speed(2, 0)

    print("Test completed.")

if __name__ == "__main__":
    main()
