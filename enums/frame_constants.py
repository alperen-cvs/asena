# This file created for all window frame constants

from . import IntEnum
from containers import WinPosition
class AnimatedOrderWindowConstants(IntEnum):

    """
    This is the class that stores how much the x, y,
    length and width information of the animated window that opens to show the order list should be enlarged or reduced. It is preferable not to change it!!
    """
    x = 235
    y = 180
    width = 270
    height = 200

def calculate_animated_order_window_position(position: WinPosition) -> WinPosition:
    """
    is a function created to calculate the position of the animated order screen.
    :param position:
    :return:
    """
    return WinPosition(x = position.x + AnimatedOrderWindowConstants.x,
                       y = position.y + AnimatedOrderWindowConstants.y,
                       width = position.width - AnimatedOrderWindowConstants.width,
                       height = position.height - AnimatedOrderWindowConstants.height
                       )