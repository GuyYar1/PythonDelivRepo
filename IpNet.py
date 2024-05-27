#import subprocess
#import platform
#import socket
#import requests

from common_imports import *


def renew_ip_windows():
    try:
        # Release the current IP address
        subprocess.run(["ipconfig", "/release"], check=True)
        print("Released IP address.")

        # Renew the IP address
        subprocess.run(["ipconfig", "/renew"], check=True)
        print("Renewed IP address.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


def get_ip_address():
    hostname = socket.gethostname()  # Get the hostname
    ip_address = socket.gethostbyname(hostname)  # Get the IP address associated with the hostname
    # Print the IP address
    return ip_address


def check_internet(url='http://www.google.com/', timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return True if response.status_code == 200 else False
    except (requests.ConnectionError, requests.Timeout):
        return False


def renewip():
    renew_ip_windows()
    #Delay for 2 seconds
    time.sleep(20)
    print("IP Address:", get_ip_address())
    time.sleep(20)