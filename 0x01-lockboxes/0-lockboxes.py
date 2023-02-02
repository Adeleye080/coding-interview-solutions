#!/usr/bin/python3
""" LockBoxex Interview Challenge """

def canUnlockAll(boxes):
    """
    determine if all boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    """
    keys = []
    for key in boxes[0]:
        if key in keys:
            pass
        else:
            keys.append(key)

    for i in range(1, (len(boxes) -1)):
        if i in keys:
            for key_in_box in boxes[i]:
                if key_in_box not in keys:
                    keys.append(key_in_box)

    return False if len(keys) < (len(boxes) - 1) else True
