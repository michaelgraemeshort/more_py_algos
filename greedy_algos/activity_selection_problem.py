# given N activities and their start and end times, and assuming that only one activity can be performed at a time,
# determine which tasks to perform in order to maximise the number of tasks performed

# he uses a list so going with that...

from collections import deque

activities = [
    ["1", 0, 6],
    ["2", 3, 4],
    ["3", 1, 2],
    ["4", 5, 8],
    ["5", 5, 7],
    ["6", 8, 9]
]


def select_activities(activities):
    # return the names of the activities?
    # sort activities based on finish time
    # select first item from sorted activities
    # then select next item that begins after the first ends
    activities = deque(
        sorted(activities, key=lambda i: i[2]))
    selected = []
    selected.append(activities.popleft())
    while activities:
        if activities[0][1] >= selected[-1][2]:
            selected.append(activities.popleft())
        else:
            activities.popleft()
    return [i[0] for i in selected]


print(select_activities(activities))
