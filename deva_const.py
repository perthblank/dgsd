class MoveKey:
    UP      = ord('w')
    DOWN    = ord('s')
    LEFT    = ord('a')
    RIGHT   = ord('d')

Directions = {
    MoveKey.UP: [0, -1],
    MoveKey.DOWN: [0, 1],
    MoveKey.LEFT: [-1, 0],
    MoveKey.RIGHT: [1, 0],
}

class MeshType:
    STATIC = 1
    RANDOM = 2
    ANIMATE_ON_TOUCH = 3
    ANIMATE_AUTO = 4

class MyKeyCode:
    ENTER = 10
    ESC = 27
    W = ord('w')
    S = ord('s')

class MenuConst:
    X = 3
    Y = 1

class RoleConst:
    COLLIDE_OFFSETS = [(1, 0), (0, 1), (2, 1), (1, 2)]

class SConst:
    BACK = 'Back'
    SAVE = 'Save'
    EXIT = 'Exit'

class ControlMode:
    MOVE = 1
    MENU = 2
    CHAT = 3

class MapGridType:
    FREE = '_'
    BLOCK = 2

class TriggerType:
    CHANGE_SCENE = 1
    CHAT = 2
    ITEM = 3

class ColorId:
    YELLOW  = 1
    GREEN   = 2
    BLUE    = 3
    RED     = 4
    MAGENTA = 5
    CYAN    = 6


TRIGGER_CHAR = '#'

ROLE_ZINDEX = 5

class ChatTextType:
    STATEMENT = 1
    BRANCH = 2

class ChatBoxConst:
    X = 4

class ItemType:
    WEAPON = 1
    ARMOR = 2
    MEDICIEN = 3
