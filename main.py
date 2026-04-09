from crowd_simulator import get_crowd_data
from assistant import suggest_path

def run():
    print("Welcome to CrowdFlow AI")

    while True:
        query = input("\nAsk something: ")

        crowd_data = get_crowd_data()
        response = suggest_path(query, crowd_data)

        print("AI:", response)
        print("Crowd Data:", crowd_data)

if __name__ == "__main__":
    run()