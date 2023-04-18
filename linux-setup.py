import subprocess
import os
import time

def check_root():
    if os.geteuid() != 0:
        exit("\033[91m {}\033[00m" .format("You need to have root privileges to run this script.\n try running with sudo!"))

def check_distro():
    try:
        lsb_id = subprocess.check_output("lsb_release -i", shell=True).decode("utf-8")
        id = lsb_id.split(":")[-1].lower().strip()
    except Exception:
        id = "unknown"
    return id


if __name__ == "__main__":
    check_root()
    if check_distro() == "debian" or "ubuntu":
        pass
    else:
        print("\033[91m {}\033[00m".format("Can't find your distribution type.. this is only for debian based distributions!."))