# input_processing.py
# Rick Zhang ENSF 692 P24
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
        # decare and initialize traffic light status, pedestrian status, and vehicle status
        self.traffic_light_status = "green"
        self.pedestrian_status = "no"
        self.vehicle_status = "no"
        # variable program_status changes when invalid input got detected. def print_message() use it as conditon to print error message
        self.program_status = 1
        # declare and intialize decison made by the car
        self.decision = "STOP"
        
    #def update_status takes 2 inputs and makes update 
    #Input 1: 1 for traffic_light_status    2 for pedestrain_status     3 for vehicle_status
    #Input 2: green, yellow, or red for trafic_light_status     yes or no for pedestrian_status     yes or no for vehicle_status
    #When either input is invalid, 3 vision status remain unchange, program_status will update to reflect detection of invalid input
    def update_status(self, status_to_change, change):
        if status_to_change == "1":
            try: # Vision input other than yellow, green or red will trigger Value Error
                if not(change == "yellow" or change == "green" or change == "red"):
                    raise ValueError()
                else:self.traffic_light_status = change
            except ValueError:
                print("In valid vision change.\n")
        elif status_to_change == "2":
            try: # Vision input other than yes or no will trigger Value Error
                if not (change == "yes" or change == "no"):
                    raise ValueError()
                else: self.pedestrian_status = change
            except ValueError:
                print("In valid vision change.\n")
        elif status_to_change == "3":
            try: # Vision input other than yes or no will trigger Value Error
                if not(change == "yes" or change == "no"):
                    raise ValueError
                else: self.vehicle_status = change
            except ValueError:
                print("In valid vision change.\n")
    
    #def dcision_making makes decision upon program requirment
    #Any scenario where a red light, a pedestrian or a vehicle are detected makes variable decision "STOP"
    #A green light with no pedestrian or vehicle detected makes variable decision "Proceed"
    #A yellow light with no pedestrian or vehicle detected makes variable decision "Caution"
    def decision_making(self):
        if self.traffic_light_status == "red" or self.pedestrian_status == "yes" or self.vehicle_status == "yes":
            self.decision = "STOP"
        elif self.traffic_light_status == "green" and self.pedestrian_status == "no" and self.vehicle_status == "no":
            self.decision = "Proceed"
        elif self.traffic_light_status == "yellow" and self.pedestrian_status == "no" or self.vehicle_status == "no":
            self.decision = "Caution"
        


#def print_message() wor
#1. check if any input is invalid by checking program_status in the input sensor object
#2. print out sensor status and decision made if all inputs are valid
#   or  print out error message if any input is invalid
def print_message(sensor):
        sensor.decision_making()
        print(sensor.decision, "\n")
        print("Light =",sensor.traffic_light_status,",",
             "Pedestrian =",sensor.pedestrian_status,",",
             "Vehicle =",sensor.vehicle_status)

#User will provide 2 inputs
#After first input, def status_change_option() displays message to tell user what the first input is and what the 2nd input can be
def status_change_option(input):
    if input == "1":
        print("You have selected light status. Please input green, yellow, or red.")
    elif input == "2":
        print("You have selected pedstrian status. Please input yes or no. ")
    elif input == "3":
        print("You have selected vehicle status. Please input yes or no. ")
    elif input == "0":
        print("Program Ends")



# main function
def main():

    #create a sensor object
    sensor1 = Sensor()
    #Initialize user input to start the while loop
    status_select = 1

    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    
    #while loop to keep program running. Loop breaks when first input is o
    while status_select != "0":

        #Program asks for the first input
        #Input 1: 1 for traffic_light_status    2 for pedestrain_status     3 for vehicle_status
        print("\nAre changes detected in the vision input?")
        status_select = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
        status_change_option(status_select)
        try: # input other than 1, 2, 3 or 4 will trigger Value Error
            if not (status_select == "1" or status_select == "2" or status_select == "3" or status_select == "0"):
                raise ValueError()
            else:
                if status_select == "0":#If first input is "0", break. Display "Program ends". No need to ask for the second input
                    break
                else:
                    status_update_option = input("What change has been identified? : ") #Program asks for the second input. #Input 2: green, yellow, or red for trafic_light_status     yes or no for pedestrian_status     yes or no for vehicle_status
                    print()
                    sensor1.update_status(status_select, status_update_option) #After both input are collected, object sensor 1 will update internal variables. Object sensor will check if the second input is valid or not.
                    print_message(sensor1)#Program displays sensor status and decision made. It also diplay message if the second input is invalid.
        except ValueError:
            print("Invalid input. Please input 1, 2, 3, or 0")
        


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

