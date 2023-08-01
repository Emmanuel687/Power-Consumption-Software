import psutil
import subprocess
import time

def get_application_pid(application_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == application_name:
            return process.info['pid']
    return None

def measure_power_consumption(application_name, duration_sec=10):
    application_pid = get_application_pid(application_name)
    if application_pid is None:
        print(f"Error: Application '{application_name}' not found.")
        return

    command = ['powerstat', '-d', '1', '-t', str(duration_sec), '-p', str(application_pid)]
    try:
        print(f"Measuring power consumption of '{application_name}' for {duration_sec} seconds...")
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("Error: 'powerstat' tool not found. Make sure it's installed.")
    except Exception as e:
        print(f"Error: An error occurred - {e}")

if __name__ == "__main__":
    target_application_name = "chrome.exe"
    measurement_duration_sec = 10  # Adjust the duration as needed

    measure_power_consumption(target_application_name, measurement_duration_sec)
