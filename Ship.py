"""
Create a base spaceship class to use in an animated GUI.
Class has methods to start, stop, increase/decrease speed, turn, fire missiles.
"""


class Ship:
    def __init__(self, name, speed, status):
        self.name = name
        self.speed = speed
        self.status = status

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_speed(self):
        return self.speed

    def set_speed(self, new_speed):
        self.speed = new_speed

    def increase_speed(self):
        self.speed += 500

    def decrease_speed(self):
        self.speed -= 500

    def get_status(self):
        return self.status

    def set_status(self, x):
        self.status = x