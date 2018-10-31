"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    #colorsensortest()
    polygontest(5)

def colorsensortest():
    """ Runs YOUR specific part of the project """
    colors = [rb.Color.RED.value, rb.Color.WHITE.value, rb.Color.BLUE.value]
    robot = rb.Snatch3rRobot()
    print(time.localtime())
    robot.color_sensor.wait_until_intensity_is_greater_than(20)
    print(time.localtime())
    robot.color_sensor.wait_until_intensity_is_less_than(80)
    print(time.localtime())
    robot.color_sensor.wait_until_color_is_one_of(colors)
    print(time.localtime())
    robot.color_sensor.wait_until_color_is(rb.Color.WHITE.value)
    print(time.localtime())
def polygontest(n):
    robot = rb.Snatch3rRobot()
    for k in range(n):
        robot.drive_system.go_straight_inches(10)
        time.sleep(.5)
        robot.drive_system.spin_in_place_degrees(180-((180*(n-2))//n))
        time.sleep(.5)
        print(180-((180*(n-2)//n)))

main()
