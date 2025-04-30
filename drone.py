from subsystems import *


class DroneSim:
    def __init__(self, weight, diameter, height, motor_model: str):
        self.weight = weight # max propeller thrust should be twice this
        self.diameter = diameter
        self.height = height

        self.motor =  Motor(motor_model)
        self.deflector = Deflector()
        self.drone_state = DroneState()
        self.flight_records = FlightLog()

        self.initial_thrust_direction = np.array([0, 0, 1]) # Drone is standing upright

    def update(self, dt):
        # compute forces
        # update drone_state.velocity and .position
        # log state
        ...

"""
To take off, the motor has to provide thrust greater than the weight of the drone. Once the desired height has been 
reached, the thrust must be equal to the weight of the drone.
"""
