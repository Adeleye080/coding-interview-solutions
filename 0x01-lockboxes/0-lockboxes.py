#!/usr/bin/python3
""" LockBoxex Interview Challenge """


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked
    Returns:
        True: all boxes can be unlocked
        False: not all boxes can be opened
    """
    if len(boxes) == 0:
        return False
    if len(boxes[0]) == 0:
        return True
    keys = [key for key in boxes[0]]
    keys.append(0)

    track = 0
    while track < len(boxes):
        for box_key in boxes[track]:
            if box_key in keys:
                try:
                    for key in boxes[box_key]:
                        keys.append(key)
                except Exception:
                    pass
        track = track + 1

    keys = list(set(keys))
    for key in keys:
        if key >= len(boxes):
            keys.remove(key)

    return True if len(keys) == len(boxes) else False
