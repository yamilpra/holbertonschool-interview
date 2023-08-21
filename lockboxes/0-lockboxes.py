#!/usr/bin/python3
"""Method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Function for unlockboxes"""
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
