from collections import deque

network = {
    "p1": ["p2", "p3", "p4"],
    "p2": ["p1", "p5"],
    "p3": [],
    "p4": ["p5"],
    "p5": [],
}


def is_correct_v(person: str) -> bool:
    if person[-1] == "5":
        return True
    return False


def search(start_v: str) -> str:
    my_queue = deque()
    my_queue += network[start_v]
    searched = []
    while my_queue:
        v_to_check = my_queue.popleft()
        print(f"Checking {v_to_check}")
        if is_correct_v(v_to_check):
            print(f"Found it: {v_to_check}")
            return v_to_check

        if v_to_check not in searched:
            my_queue += network[v_to_check]

        searched.append(v_to_check)

    return "not_found"


result = search("p1")
