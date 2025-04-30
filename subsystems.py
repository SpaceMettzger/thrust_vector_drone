import numpy as np

class Motor:
    # Parameters assuming 6040 2-blade propellers
    MOTOR_PARAMETERS = {
        "T-Motor F80 PRO 2408 Brushless Motor": {
            "max_rpm": 29613,
            "voltage": 18.79, # in V
            "current": 49.40, # in A
            "power": 928.25, # in W
            "max_thrust": 2037, # in g
            "power_ratio": 2.19, # in g/W
            "propeller_radius" : 15.24 # in cm (6 inches)
    }}

    def __init__(self, model: str):
        self.max_rpm = self.MOTOR_PARAMETERS[model]["max_rpm"]
        self.max_voltage = self.MOTOR_PARAMETERS[model]["voltage"]
        self.max_current = self.MOTOR_PARAMETERS[model]["current"]
        self.max_power = self.MOTOR_PARAMETERS[model]["power"]
        self.max_thrust = self.MOTOR_PARAMETERS[model]["max_thrust"]
        self.power_ratio = self.MOTOR_PARAMETERS[model]["power_ratio"]
        self.propeller_radius = self.MOTOR_PARAMETERS[model]["propeller_radius"] / 100  # cm to meters

class Deflector:
    def __init__(self):
        self.max_deflection_deg = 25 # in degrees
        self.max_deflection_per_sec = 15
        self.current_x_deflection_deg = 0
        self.current_y_deflection_deg = 0

class DroneState:
    def __init__(self):
        self.position = np.zeros(3)       # [x, y, z]
        self.velocity = np.zeros(3)       # [vx, vy, vz]
        self.acceleration = np.zeros(3)   # [ax, ay, az]
        self.orientation = np.zeros(3)    # [pitch, yaw, roll] or use quaternions if needed
        self.angular_velocity = np.zeros(3)  # [pitch_rate, yaw_rate, roll_rate]

    def __repr__(self):
        return f"Pos: {self.position}, Vel: {self.velocity}, Acc: {self.acceleration}"

class FlightLog:
    def __init__(self):
        self.records = []

    def add_state(self, state: DroneState, timestamp: float):
        self.records.append({'t': timestamp, 'state': state})

class Controller:
    def __init__(self):
        ...


class Battery:
    def __init__(self):
        ...