"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    robot.drive_system.turn_degrees(360, -100)
    time.sleep(1)
    robot.drive_system.turn_degrees(90, 100)
    time.sleep(1)
    robot.drive_system.turn_degrees(180, -50)
    time.sleep(1)

main()
