import os

if os.geteuid() == 0:
    os.system("sudo rm /etc/apt/preferences.d/nosnap.pref")
    os.system("sudo apt update && sudo apt upgrade")
    os.system("sudo snap install snap-store")
    os.system("sudo apt install firefox")
    print("\n\033[92m {}\033[00m" .format("Reinstalled snap sucessfully!.."))
else:
    print("\n\033[91m {}\033[00m" .format("You need to have root privileges to run this script.\n try running with sudo!"))
