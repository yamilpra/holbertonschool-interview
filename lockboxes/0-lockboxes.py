#!/usr/bin/python3
"""Method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Function for unlockboxes"""
    unlocked_boxes = [False] * len(boxes)
    unlocked_boxes[0] = True
    keys = [0]

    while keys:
        box_idx = keys.pop(0)
        for key in boxes[box_idx]:
            if not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                keys.append(key)

    return all(unlocked_boxes)
