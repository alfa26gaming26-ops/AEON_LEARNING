import time
import random

class Robot:
    """
    Simulates a physical robot with locomotion, sensing, and manipulation capabilities.
    This class abstracts the hardware interactions for the 'fix generator' task.
    """
    def __init__(self):
        self.location = (0, 0)  # Current (x,y) coordinates of the robot
        self.power_level = 100  # Internal power level of the robot (0-100%)
        self.tools = []         # List of tools currently possessed by the robot
        self.generator_state = {
            "located": False,
            "power_cable_connected": False,
            "fuel_level": random.uniform(0, 100),  # Initial random fuel level
            "oil_level": random.uniform(0, 100),   # Initial random oil level
            "start_switch_on": False,
            "running": False,
            "error_code": None,
            "fuel_type": "gasoline",
            "oil_type": "SAE30"
        }
        self.environment = {
            "generator_location": (10, 5),      # Known location of the generator
            "fuel_station_location": (20, 10),  # Known location to acquire fuel
            "oil_storage_location": (25, 12),   # Known location to acquire oil
            "power_outlet_location": (8, 4)     # Known location of a power outlet (for cable)
        }

    def _consume_power(self, amount):
        """Internal method to simulate power consumption for actions."""
        self.power_level -= amount
        if self.power_level <= 0:
            print("Robot: Power critically low. Shutting down.")
            raise SystemExit("Robot out of power.")

    def move_to(self, target_location):
        """Simulates the robot moving to a specified location."""
        print(f"Robot: Moving to {target_location} (current power: {self.power_level:.1f}%)...")
        self._consume_power(random.randint(5, 15))
        time.sleep(random.uniform(1, 3))  # Simulate travel time
        self.location = target_location
        print(f"Robot: Arrived at {target_location}.")
        return True

    def scan_area(self, radius=5):
        """Simulates the robot scanning its surroundings for objects."""
        print(f"Robot: Scanning area around {self.location} for objects...")
        self._consume_power(3)
        time.sleep(random.uniform(0.5, 1.5))
        
        # Simulate detection of the generator and its initial state
        if abs(self.location[0] - self.environment["generator_location"][0]) < radius and \
           abs(self.location[1] - self.environment["generator_location"][1]) < radius:
            self.generator_state["located"] = True
            print("Robot: Generator detected.")
            # Randomly set initial generator fault states
            self.generator_state["power_cable_connected"] = random.choice([True, False]) if random.random() < 0.7 else True
            self.generator_state["fuel_level"] = random.uniform(0, 100)
            self.generator_state["oil_level"] = random.uniform(0, 100)
            self.generator_state["start_switch_on"] = random.choice([True, False])
            self.generator_state["running"] = False # Assume it's not running if we're fixing it
            print(f"Robot: Initial generator assessment: {self.generator_state}")
            return True
        print("Robot: Generator not found in current scan area.")
        return False

    def manipulate_object(self, action, target_object):
        """Simulates the robot performing an action on a physical object."""
        print(f"Robot: Performing '{action}' on '{target_object}'...")
        self._consume_power(random.randint(2, 10))
        time.sleep(random.uniform(0.5, 2))

        if target_object == "power_cable":
            if action == "connect":
                self.generator_state["power_cable_connected"] = True
                print("Robot: Power cable connected to generator and outlet.")
                return True
        elif target_object == "fuel_cap":
            if action == "open":
                print("Robot: Fuel cap opened.")
                return True
            elif action == "close":
                print("Robot: Fuel cap closed.")
                return True
        elif target_object == "oil_cap":
            if action == "open":
                print("Robot: Oil cap opened.")
                return True
            elif action == "close":
                print("Robot: Oil cap closed.")
                return True
        elif target_object == "fuel_tank":
            if action == "refill":
                if "fuel_can" in self.tools:
                    self.generator_state["fuel_level"] = 100  # Assume full refill
                    print("Robot: Fuel tank refilled.")
                    return True
                else:
                    print("Robot: Error: No fuel can available.")
                    return False
        elif target_object == "oil_reservoir":
            if action == "add_oil":
                if "oil_can" in self.tools:
                    self.generator_state["oil_level"] = 100  # Assume full
                    print("Robot: Oil reservoir filled.")
                    return True
                else:
                    print("Robot: Error: No oil can available.")
                    return False
        elif target_object == "start_switch":
            if action == "turn_on":
                self.generator_state["start_switch_on"] = True
                print("Robot: Start switch turned ON.")
                return True
            elif action == "turn_off":
                self.generator_state["start_switch_on"] = False
                print("Robot: Start switch turned OFF.")
                return True
        elif target_object == "starter":
            if action == "engage":
                print("Robot: Attempting to engage generator starter...")
                time.sleep(random.uniform(2, 5))
                # Simulate success based on fixed preconditions
                if self.generator_state["power_cable_connected"] and \
                   self.generator_state["fuel_level"] >= 20 and \
                   self.generator_state["oil_level"] >= 20 and \
                   self.generator_state["start_switch_on"]:
                    self.generator_state["running"] = True
                    print("Robot: Generator started successfully!")
                    return True
                else:
                    print("Robot: Generator failed to start. Reviewing conditions.")
                    return False
        
        print(f"Robot: Unknown manipulation action or target: '{action}' on '{target_object}'")
        return False

    def check_generator_running(self):
        """Simulates the robot checking if the generator is operational."""
        print("Robot: Checking if generator is running (sound, vibration, power output)...")
        self._consume_power(2)
        time.sleep(random.uniform(1, 2))
        
        if self.generator_state["running"]:
            print("Robot: Generator is running and producing power.")
            return True
        else:
            print("Robot: Generator is not running.")
            return False

    def acquire_resource(self, resource_type):
        """Simulates the robot acquiring a specific resource (e.g., fuel can)."""
        if resource_type in self.tools:
            print(f"Robot: Already possess {resource_type}.")
            return True

        print(f"Robot: Acquiring {resource_type}...")
        if resource_type == "fuel_can":
            self.move_to(self.environment["fuel_station_location"])
            time.sleep(1)
            self.tools.append("fuel_can")
            print(f"Robot: {resource_type} acquired.")
            return True
        elif resource_type == "oil_can":
            self.move_to(self.environment["oil_storage_location"])
            time.sleep(1)
            self.tools.append("oil_can")
            print(f"Robot: {resource_type} acquired.")
            return True
        
        print(f"Robot: Cannot acquire unknown resource type: {resource_type}")
        return False

def fix_generator():
    """
    This function contains the complete autonomous logic for Aeon (the robot)
    to identify and fix a non-operational generator.
    It orchestrates the robot's movements, sensory inputs, and physical manipulations.
    """
    aeon_robot = Robot()
    max_attempts = 3
    attempt = 0

    print("Aeon: Initiating 'fix generator' protocol.")

    while attempt < max_attempts:
        attempt += 1
        print(f"\nAeon: Fix attempt {attempt}/{max_attempts} (Robot power: {aeon_robot.power_level:.1f}%)...")

        # Step 1: Locate the generator
        if not aeon_robot.generator_state["located"]:
            if not aeon_robot.move_to(aeon_robot.environment["generator_location"]):
                print("Aeon: Failed to reach generator location. Aborting attempt.")
                continue
            if not aeon_robot.scan_area():
                print("Aeon: Failed to locate generator after reaching its known area. Aborting attempt.")
                continue
        else:
            print("Aeon: Generator already located.")

        # Step 2: Initial check - is it already running?
        if aeon_robot.check_generator_running():
            print("Aeon: Generator is already running. Task complete.")
            return True

        print("Aeon: Performing diagnostic checks and corrective actions...")

        # Action 2.1: Check and connect power cable
        if not aeon_robot.generator_state["power_cable_connected"]:
            print("Aeon: Power cable disconnected. Attempting to connect.")
            # Move to power outlet if not already near it, then connect
            if not aeon_robot.move_to(aeon_robot.environment["power_outlet_location"]):
                 print("Aeon: Failed to reach power outlet location.")
                 continue
            if not aeon_robot.manipulate_object("connect", "power_cable"):
                print("Aeon: Failed to connect power cable. Aborting attempt.")
                continue
            # After connecting, move back to generator for further checks
            if not aeon_robot.move_to(aeon_robot.environment["generator_location"]):
                 print("Aeon: Failed to return to generator location after connecting cable.")
                 continue
            print("Aeon: Power cable connected. Retesting generator status.")
            if aeon_robot.check_generator_running():
                print("Aeon: Generator started after connecting power cable. Task complete.")
                return True

        # Action 2.2: Check and refill fuel
        if aeon_robot.generator_state["fuel_level"] < 20: # Threshold for low fuel
            print(f"Aeon: Fuel level is low ({aeon_robot.generator_state['fuel_level']:.1f}%). Proceeding to refill.")
            if not aeon_robot.acquire_resource("fuel_can"):
                print("Aeon: Could not acquire fuel can. Cannot refill fuel. Aborting attempt.")
                continue
            # Ensure robot is at generator before manipulating
            if not aeon_robot.move_to(aeon_robot.environment["generator_location"]):
                 print("Aeon: Failed to reach generator location for fuel refill.")
                 continue
            if not aeon_robot.manipulate_object("open", "fuel_cap"):
                print("Aeon: Failed to open fuel cap. Aborting attempt.")
                continue
            if not aeon_robot.manipulate_object("refill", "fuel_tank"):
                print("Aeon: Failed to refill fuel tank. Aborting attempt.")
                aeon_robot.manipulate_object("close", "fuel_cap") # Attempt to close even if refill failed
                continue
            aeon_robot.manipulate_object("close", "fuel_cap")
            print("Aeon: Fuel refilled. Retesting generator status.")
            if aeon_robot.check_generator_running():
                print("Aeon: Generator started after refilling fuel. Task complete.")
                return True

        # Action 2.3: Check and add oil
        if aeon_robot.generator_state["oil_level"] < 20: # Threshold for low oil
            print(f"Aeon: Oil level is low ({aeon_robot.generator_state['oil_level']:.1f}%). Proceeding to add oil.")
            if not aeon_robot.acquire_resource("oil_can"):
                print("Aeon: Could not acquire oil can. Cannot add oil. Aborting attempt.")
                continue
            # Ensure robot is at generator before manipulating
            if not aeon_robot.move_to(aeon_robot.environment["generator_location"]):
                 print("Aeon: Failed to reach generator location for oil addition.")
                 continue
            if not aeon_robot.manipulate_object("open", "oil_cap"):
                print("Aeon: Failed to open oil cap. Aborting attempt.")
                continue
            if not aeon_robot.manipulate_object("add_oil", "oil_reservoir"):
                print("Aeon: Failed to add oil. Aborting attempt.")
                aeon_robot.manipulate_object("close", "oil_cap") # Attempt to close
                continue
            aeon_robot.manipulate_object("close", "oil_cap")
            print("Aeon: Oil added. Retesting generator status.")
            if aeon_robot.check_generator_running():
                print("Aeon: Generator started after adding oil. Task complete.")
                return True

        # Action 2.4: Check and turn on start switch
        if not aeon_robot.generator_state["start_switch_on"]:
            print("Aeon: Start switch is OFF. Attempting to turn ON.")
            # Ensure robot is at generator before manipulating
            if not aeon_robot.move_to(aeon_robot.environment["generator_location"]):
                 print("Aeon: Failed to reach generator location for switch manipulation.")
                 continue
            if not aeon_robot.manipulate_object("turn_on", "start_switch"):
                print("Aeon: Failed to turn on start switch. Aborting attempt.")
                continue
            print("Aeon: Start switch ON. Retesting generator status.")
            if aeon_robot.check_generator_running():
                print("Aeon: Generator started after turning on switch. Task complete.")
                return True

        # Step 3: Attempt to start the generator (after all known preconditions are met)
        print("Aeon: All identified preconditions met. Attempting to start generator.")
        # Ensure robot is at generator before manipulating
        if not aeon_robot.move_to(aeon_robot.environment["generator_location"]):
             print("Aeon: Failed to reach generator location for starting.")
             continue
        if aeon_robot.manipulate_object("engage", "starter"):
            if aeon_robot.check_generator_running():
                print("Aeon: Generator successfully started! Task complete.")
                return True
        else:
            print("Aeon: Failed to start generator after addressing all known issues.")

        print("Aeon: Generator still not running. Re-evaluating for next attempt or waiting.")
        time.sleep(5) # Wait a bit before next attempt

    print(f"\nAeon: Failed to fix generator after {max_attempts} attempts. Manual intervention may be required.")
    return False

# Example of how to run this script if it were the main entry point:
# if __name__ == "__main__":
#     fix_generator()