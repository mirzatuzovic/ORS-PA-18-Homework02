"""
===================   TASK 3   ====================
* Name: Cube Volume
*
* Write a function `cube_volume` that will return
* volume of a cube for a given side length.
* If passed value is invalid, function should
* return -1 which indicates something went wrong.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

def cube_volume(a):
    if not (isinstance(a, float) or isinstance(a, int)):
        return -1

    return abs(a)**3


def main():

    side_in_cm = 8.0
    volume_of_cube = cube_volume(side_in_cm)
    print("Volume of a cube is: ", volume_of_cube)

main()

