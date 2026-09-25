import random

def simple_reflex_vacuum_agent(location, status):
    """
    Condition-Action Rules:
    If current room is Dirty -> Suck
    If in Room A and Clean -> Right
    If in Room B and Clean -> Left
    """
    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Right'
    elif location == 'B':
        return 'Left'

def run_simple_reflex():
    print("=== Simple Reflex Vacuum Agent ===")
    environment = {
        'A': random.choice(['Clean', 'Dirty']),
        'B': random.choice(['Clean', 'Dirty'])
    }
    location = random.choice(['A', 'B'])

    print(f"Initial State: Location = {location}, Rooms = {environment}")

    for step in range(1, 5):
        status = environment[location]
        action = simple_reflex_vacuum_agent(location, status)
        print(f"Step {step}: Agent at '{location}' sees status '{status}' -> Action: {action}")

        if action == 'Suck':
            environment[location] = 'Clean'
        elif action == 'Right':
            location = 'B'
        elif action == 'Left':
            location = 'A'

    print(f"Final State: {environment}\n")

run_simple_reflex()
