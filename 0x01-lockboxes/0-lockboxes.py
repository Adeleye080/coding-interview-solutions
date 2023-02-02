#!/usr/bin/python3
""" LockBoxex Interview Challenge """


def canUnlockAll(boxes):
    """
    determine if all boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    """
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True

    keys = []
    for key in boxes[0]:
        if key in keys or key == 0:
            pass
        else:
            keys.append(key)

    for i in range(1, len(boxes)):
        if i in keys:
            for key_in_box in boxes[i]:
                if key_in_box not in keys and key_in_box != 0:
                    keys.append(key_in_box)

    for key in keys:
        if key >= len(boxes):
            keys.remove(key)
    keys.append(0)
    return False if len(keys) < len(boxes) else True
