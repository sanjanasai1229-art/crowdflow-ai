import random

def get_crowd_data():
    locations = ["Gate A", "Gate B", "Gate C", "Food Court", "Washroom"]
    crowd_data = {}

    for loc in locations:
        crowd_data[loc] = random.randint(1, 100)

    return crowd_data