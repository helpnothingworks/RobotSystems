from threading import Event
import time
from concurrent.futures import ThreadPoolExecutor
from readerwriterlock import rwlock
from line_following import Sensor, Interpreter, Controller

shutdown_event = Event()

class Bus:
    def __init__(self): 
        self.lock = rwlock.RWLockWriteD()
        self.message = None

    def write(self, message):  
        with self.lock.gen_wlock():  
            self.message = message

    def read(self):  
        with self.lock.gen_rlock():  
            return self.message

def handle_exception(future):
    exception = future.exception()
    if exception:
        print(f"Exception in worker thread: {exception}")

def producer(sensor_bus, sleep_time=0.05):  
    sensor = Sensor()

    for _ in range(3):  
        sensor_bus.write(sensor.read_sensors())
        time.sleep(0.1)

    while not shutdown_event.is_set():  
        sensor_data = sensor.read_sensors()
        sensor_bus.write(sensor_data)
        time.sleep(sleep_time)

def consumer_producer(sensor_bus, position_bus, sleep_time=0.05):  
    interpreter = Interpreter()
    last_position = 0  #the car was randomly moving to the left(deviating from the tape) before coming back and following the line so I used the help of chatgpt and found references to similar problem people faced and how keeping track of the last position helped.

    while not shutdown_event.is_set():  
        sensor_data = sensor_bus.read()
        if sensor_data:
            processed_data = interpreter.interpret(sensor_data)
            if processed_data is not None:
                last_position = processed_data  
                position_bus.write(processed_data)
            else:
                position_bus.write(last_position)  
        time.sleep(sleep_time)


def consumer(position_bus, sleep_time=0.05):  
    controller = Controller(scaling_factor=12, speed=30)
    last_position = 0  
    for _ in range(3):
        controller.control(0)
        controller.car.forward(controller.speed)
        time.sleep(0.2)

    while not shutdown_event.is_set():
        position = position_bus.read()
        if position is not None:
            last_position = position  
        else:
            position = last_position  

        controller.control(position)
        controller.car.forward(controller.speed)
        time.sleep(sleep_time)


def main():
    sensor_bus = Bus()  
    position_bus = Bus()

    with ThreadPoolExecutor(max_workers=3) as executor:
        eSensor = executor.submit(producer, sensor_bus)
        eSensor.add_done_callback(handle_exception)

        eInterpreter = executor.submit(consumer_producer, sensor_bus, position_bus)
        eInterpreter.add_done_callback(handle_exception)

        eController = executor.submit(consumer, position_bus)
        eController.add_done_callback(handle_exception)

        try:
            while not shutdown_event.is_set():
                time.sleep(1)
        except KeyboardInterrupt:
            print("shutting down")
            shutdown_event.set()
        finally:
            executor.shutdown()

if __name__ == "__main__":
    main()
