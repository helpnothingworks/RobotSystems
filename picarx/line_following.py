import time
from robot_hat import ADC
from picarx_improved import Picarx

class Sensor:
    def __init__(self):
        self.left_sensor = ADC('A0')
        self.middle_sensor = ADC('A1')
        self.right_sensor = ADC('A2')

    def read_sensors(self):
        return [self.left_sensor.read(), self.middle_sensor.read(), self.right_sensor.read()]

class Interpreter:
    def __init__(self, polarity='dark'):
        self.polarity = polarity

    def interpret(self, sensor_values):
        left, middle, right = sensor_values

        if self.polarity == 'dark':
            if middle < left and middle < right:
                return 0  # Center
            elif left < right:
                return -1  #left
            else:
                return 1  #right
        else:
            if middle > left and middle > right:
                return 0  # Centered
            elif left > right:
                return -1  #left
            else:
                return 1  #right

class Controller:
    def __init__(self, scaling_factor=20, speed=30):
        self.car = Picarx()
        self.scaling_factor = scaling_factor
        self.speed = speed

    def control(self, position):
        steering_angle = position * self.scaling_factor  # Scaling for smoothness
        self.car.set_dir_servo_angle(steering_angle)

    def run(self):
        sensor = Sensor()
        interpreter = Interpreter()

        try:
            while True:
                sensor_values = sensor.read_sensors()
                position = interpreter.interpret(sensor_values)
                self.control(position)

                self.car.forward(self.speed)

                time.sleep(0.1)  # delay for smooth movement

        except KeyboardInterrupt:
            self.car.stop()
            print("Program stopped.")

if __name__ == "__main__":
    controller = Controller(scaling_factor=20, speed=30)
    controller.run()
