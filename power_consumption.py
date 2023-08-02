import psutil
import time
import platform

def get_application_power_consumption(app_name, duration=5):
    """
    Measure the power consumption of a single application using CPU-based heuristics.

    Parameters:
    app_name (str): The name of the target application.
    duration (int): The measurement duration in seconds.

    Returns:
    float: Estimated power consumption in watts.
    """
    # Function to get CPU usage
    def get_cpu_usage():
        return psutil.cpu_percent(interval=0.1) / 100.0  # CPU usage as a fraction (0 to 1)

    # Function to get system-wide power consumption on macOS and Linux
    def get_system_power_usage_unix():
        try:
            with open('/sys/class/power_supply/BAT0/power_now', 'r') as f:
                return int(f.read()) / 1e6  # Power consumption in watts
        except FileNotFoundError:
            return None  # If the file is not found, return None

    # Function to get system-wide power consumption on Windows
    def get_system_power_usage_windows():
        try:
            return psutil.sensors_battery().power_plugged
        except AttributeError:
            return None  # If 'psutil' version does not support 'psutil.sensors_battery()', return None

    # Get initial system-wide power consumption
    if platform.system() == 'Windows':
        initial_power = get_system_power_usage_windows()
    else:
        initial_power = get_system_power_usage_unix()

    # Get the process ID (PID) of the target application
    pid = None
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == app_name:
            pid = proc.info['pid']
            break

    if not pid:
        print(f"Application '{app_name}' not found.")
        return None

    print(f"Measuring power consumption of '{app_name}' for {duration} seconds...")
    time.sleep(duration)

    # Get final system-wide power consumption
    if platform.system() == 'Windows':
        final_power = get_system_power_usage_windows()
    else:
        final_power = get_system_power_usage_unix()

    # Calculate power consumption estimation
    if initial_power is not None and final_power is not None:
        power_diff = abs(final_power - initial_power)
        cpu_usage = get_cpu_usage()
        power_consumption = power_diff * cpu_usage * duration
        return power_consumption

    return None

if __name__ == "__main__":
    # Prompt for the name of the application
    app_name = input("Enter the name of the application: ")

    # Prompt for the measurement duration in seconds
    measurement_duration = int(input("Enter the measurement duration in seconds: "))

    power_consumption = get_application_power_consumption(app_name, measurement_duration)
    if power_consumption is not None:
        print(f"Estimated power consumption of '{app_name}': {power_consumption:.2f} watts.")
