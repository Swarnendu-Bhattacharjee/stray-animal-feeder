# src/main.py
from nlp_bot import NLPBot
from feeder_robot import FeederRobot
from cv_module import CVModule
from utils import log_event

def main():
    log_event("Starting StrayMate AI Bot")
    nlp = NLPBot()
    robot = FeederRobot()
    cv = CVModule()

    print(nlp.greet())

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            log_event("User exited chat.")
            break

        response = nlp.get_response(user_input)
        print(f"StrayMate AI Bot: {response}")

        # Optional simulated commands
        if "dispense food" in user_input.lower():
            amount = 50  # default
            status = robot.dispense_food(amount)
            print(f"Robot Status: {status}")

if __name__ == "__main__":
    main()
