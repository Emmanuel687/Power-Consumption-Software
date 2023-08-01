# Power Consumption Measurement Readme
This README file provides an overview of the Python code for measuring power consumption of a specific application in the computer using the psutil and subprocess modules. The code utilizes the external tool powerstat to gather power consumption data and requires the psutil and subprocess libraries to be installed.

# Prerequisites
Before using this code, ensure that you have the following prerequisites:

1.Have Python installed on your system.

You can Install python from its website:-

https://www.python.org/downloads/


2.Have psutil library installed.

-This module allows you to access system details and process-related information.

You can install it using pip:

pip install psutil

3.powerstat utility installed. 

-The powerstat tool is used to measure power consumption on Linux systems. Make sure it is installed and accessible from the command line.

-This are the commands for installation
sudo apt-get update
sudo apt-get install powerstat

# Code Overview
The code provided in the Python script (measure_power_consumption.py) allows you to measure the power consumption of a specified application for a given duration using the powerstat utility.

1.Function: get_application_pid(application_name)
This function retrieves the process ID (PID) of a specific application by its name. It utilizes the psutil library to iterate through all running processes and identify the process with the given application_name. If found, it returns the PID; otherwise, it returns None.

2.Function: measure_power_consumption(application_name, duration_sec=10)
This function measures the power consumption of a specified application for a given duration using the powerstat tool. The function takes two parameters:

application_name: The name of the target application whose power consumption you want to measure.
duration_sec: The duration (in seconds) for which power consumption will be measured. By default, it is set to 10 seconds.
The function internally calls get_application_pid(application_name) to retrieve the PID of the target application. If the application is found, it executes the powerstat command through the subprocess module to measure the power consumption.

# Execution /Running the program
To execute the power consumption measurement, follow these steps:

1.Open a terminal or command prompt.

Navigate to the directory where the measure_power_consumption.py script is located.

Run the script using Python:

python measure_power_consumption.py

The script will display a message indicating that it's measuring the power consumption of the specified application for the specified duration (default: 10 seconds).

After the measurement is completed, the script will print the output from powerstat tool, which includes information about power consumption during the specified duration.



Note
The script is designed to work on Linux systems due to the dependency on the powerstat tool.

Ensure that the powerstat tool is installed and available in the system's PATH for successful execution.







