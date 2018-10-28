"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    drive = robot.drive_system
    color = robot.color_sensor
    turn_right = True

    while True:
        # Moving forward until light is reflected
        drive.start_moving()
        color.wait_until_intensity_is_greater_than(10)

        # Try turning clockwise (to the right)
        counter = 0
        while True:

            if turn_right is True:
                drive.start_moving(100, 0)
            else:
                drive.start_moving(0, 100)

            # Runs if robot is back on black within 0.25 seconds (implying that robot is turning in right direction)
            if color.get_reflected_intensity() < 10:
                drive.stop_moving()
                break

            # Runs if robot has not encountered black after 0.25 seconds in direction it's turning
            if counter > 0.25 and color.get_reflected_intensity() > 10:
                print('No black detected, turn around!')
                drive.stop_moving()

                # Revert to original position
                if turn_right is True:
                    drive.move_for_seconds(0.25, -100, 0)
                else:
                    drive.move_for_seconds(0.25, 0, -100)

                # Changes direction to turn in the future
                if turn_right is True:
                    turn_right = False
                else:
                    turn_right = True
                print('Turn direction changed! Now turn_right is :', turn_right)

                # Turn for certain amount of time
                while True:
                    if turn_right is True:
                        drive.start_moving(100, 0)
                    else:
                        drive.start_moving(0, 100)

                    if color.get_reflected_intensity() < 10:
                        drive.stop_moving()
                        break

            counter = counter + 0.05
            print(counter, color.get_reflected_intensity())
            time.sleep(0.05)


main()
