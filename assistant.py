from utils import generate_maps_link

def suggest_best_gate(crowd_data):
    gates = {k: v for k, v in crowd_data.items() if "Gate" in k}
    return min(gates, key=gates.get)

def suggest_food(crowd_data):
    food_places = {k: v for k, v in crowd_data.items() if "Food" in k}
    return min(food_places, key=food_places.get)

def suggest_path(user_query, crowd_data):
    query = user_query.lower()

    if "gate" in query or "enter" in query:
        best_gate = suggest_best_gate(crowd_data)
        link = generate_maps_link(best_gate)
        return f"Use {best_gate} (least crowded entry)\nNavigate: {link}"

    elif "food" in query or "eat" in query:
        best_food = suggest_food(crowd_data)
        link = generate_maps_link(best_food)
        return f"Go to {best_food} (shortest queue)\nNavigate: {link}"

    elif "washroom" in query or "toilet" in query:
        link = generate_maps_link("Washroom")
        return f"Nearest washroom available\nNavigate: {link}"

    else:
        return "Try asking about entry gates, food, or washrooms"