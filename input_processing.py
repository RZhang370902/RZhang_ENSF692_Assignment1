# input_processing.py
# YOUR NAME, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.traffic_light_status = "green"
        self.pedestrian_status = "no"
        self.vehicle_status = "no"
        self.last_traffic_light_status = "green"
        self.program_status = 1
        

    # Replace these comments with your function commenting
    def update_status(self, user_input): # You may decide how to implement the arguments for this function
        if user_input == "1":
            if self.traffic_light_status == "green":
                self.traffic_light_status = "yellow"
                self.last_traffic_light_status = "green"
            elif self.traffic_light_status == "yellow":
                if self.last_traffic_light_status == "green":
                    self.traffic_light_status = "red"
                else:
                    self.traffic_light_status = "green"
            else:
                self.traffic_light_status = "yellow"
                self.last_traffic_light_status = "red"
        elif user_input == "2":
            if self.pedestrian_status == "no":
                self.pedestrian_status = "yes"
            else:
                self.pedestrian_status = "no"
        elif user_input == "3":
            if self.vehicle_status == "no":
                self.vehicle_status = "yes"
            else:
                self.vehicle_status = "no"
        elif user_input == "0":
            self.program_status = 0
        else:
            self.program_status = 2



sensor1 = Sensor()
sensor2 = Sensor()
sensor2.pedestrian_status = "yes"

print(sensor1.vehicle_status)
# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    if sensor.program_status == 1:
        print("\n","Light =",sensor.traffic_light_status,",",
             "Pedestrian =",sensor.pedestrian_status,",",
             "Vehicle =",sensor.vehicle_status,"\n")
    elif sensor.program_status == 0:
        print("\n Program Ends\n")
    else:
        print("Invalid input. Please input 1, 2, 3, or 0")
        sensor.program_status = 1



# Complete the main function below
def main():
    #Initialize user input
    user_input = 1

    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    
    while user_input != "0":
       #print("\n\nCurrent vision status: ")
        #print("\n","Light =",sensor1.traffic_light_status,",",
        #    "Pedestrian =",sensor1.pedestrian_status,",",
        #   "Vehicle =",sensor1.vehicle_status,",","\n")
        print("\nAre changes detected in the vision input?")
        user_input = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
        sensor1.update_status(user_input)
        #print("\n\nCurrent vision status: ")
        print_message(sensor1)





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

