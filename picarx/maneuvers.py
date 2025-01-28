import logging
import time
from picarx_improved import Picarx

logging_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=logging_format, level=logging.INFO, datefmt="%H:%M:%S")
logging.getLogger().setLevel(logging.DEBUG)

class Maneuvers:
    def __init__(self):
        self.px = Picarx()

    def move_forward(self, speed=50, duration=2, angle=0):
        self.px.set_dir_servo_angle(angle)
        self.px.forward(speed)
        time.sleep(duration)
        self.px.stop()

    def move_backward(self, speed=50, duration=2, angle=0):
        self.px.set_dir_servo_angle(angle)
        self.px.backward(speed)
        time.sleep(duration)
        self.px.stop()

    def parallel_park(self, direction='left'):

        if direction == 'left':
            self.move_forward(speed=30, duration=1.5, angle=0) #to align
            time.sleep(1)

            self.move_backward(speed=30, duration=2, angle=-45) #backwards to the left
            time.sleep(1)

            self.move_backward(speed=30, duration=2, angle=45) #back right
            time.sleep(1)

            self.move_forward(speed=20, duration=1, angle=0) #final adjustment
            time.sleep(1)

        else:  # Right parallel parking
    
            self.move_forward(speed=30, duration=1.5, angle=0)
            time.sleep(1)

            self.move_backward(speed=30, duration=2, angle=45) #backwareds right
            time.sleep(1)

            self.move_backward(speed=30, duration=2, angle=-45) #backwards left
            time.sleep(1)

            self.move_forward(speed=20, duration=1, angle=0)
            time.sleep(1)

        self.px.stop()
        logging.info(f"Parallel parking to the {direction} completed.")



    def k_turn(self, initial_direction='left'):
        logging.info("Starting K-turn")
        if initial_direction == 'left':
            self.move_forward(speed=30, duration=2, angle=-30)
            self.move_backward(speed=30, duration=2, angle=30)
        else:
            self.move_forward(speed=30, duration=2, angle=30)
            self.move_backward(speed=30, duration=2, angle=-30)

        self.move_forward(speed=30, duration=2, angle=0)
        self.px.stop()
        logging.info("K-turn completed.")

    def control_loop(self):
        print("what do you want to perform?: ")
        print("[f] forward, [b] backward, [l] left parallel, [r] right parallel, [k] k turn")

        while True:
            command = input("enter command: ").lower()

            if command == 'f':
                print("Moving forward")
                self.move_forward(speed=50, duration=3, angle=0)

            elif command == 'b':
                print("Moving backward")
                self.move_backward(speed=50, duration=3, angle=0)

            elif command == 'l':
                print("left parallel parking")
                self.parallel_park(direction='left')

            elif command == 'r':
                print("right parallel parking")
                self.parallel_park(direction='right')

            elif command == 'k':
                print("executing K-turn")
                self.k_turn(initial_direction='left')

            else:
                print("Invalid command. Please enter f, b, l, r, k.")

            time.sleep(0.5)  # Short delay to avoid repeated inputs

if __name__ == "__main__":
    maneuver = Maneuvers()
    maneuver.control_loop()
