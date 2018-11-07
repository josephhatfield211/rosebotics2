"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
from ev3dev import ev3
import time


def main():
    robot = rb.Snatch3rRobot
    while True:
        print(robot.beacon_sensor.get_distance_to_beacon())
        print(robot.beacon_sensor.get_heading_to_beacon())


main()
