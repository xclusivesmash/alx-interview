"""
Module: 0-lockboxes
Description: checks if all boxes can be opened.
"""


def lookNextOpenedBox(openedBoxes):
    """check for the next opened box"""
    for _, box in openedBoxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Check if all boxes can be opened"""
    # return True of boxes is empty
    if len(boxes) <= 1 or boxes == [[]]:
        return True
    temp = {}
    while True:
        if len(temp) == 0:
            temp[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = lookNextOpenedBox(temp)
        if keys:
            for key in keys:
                try:
                    if temp.get(key) and temp.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    temp[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in temp.values()]:
            continue
        elif len(temp) == len(boxes):
            break
        else:
            return False
    return len(temp) == len(boxes)
