"""
  Capstone Project.  Code written by Yuanning Zuo.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    robot = rb.Snatch3rRobot()
    print()
    print("Testing touch sensor")
    print("CTRL-C to terminate the program!")
    time.sleep(1)
    count = 1
    while True:
        print("{:4}.".format(count),"touch sensor value is: ",robot.touch_sensor.get_value())
        time.sleep(0.5)
        count = count +1








main()
