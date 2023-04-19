import subprocess
import os
import time

# colors
def Red(msg): print("\033[91m {}\033[00m" .format("\n"+msg))
def Green(msg): print("\033[92m {}\033[00m" .format('\n'+msg))
def Yellow(msg): print("\033[93m {}\033[00m" .format('\n'+msg))
def Purple(msg): print("\033[95m {}\033[00m" .format('\n'+msg)) 
def Cyan(msg): print("\033[96m {}\033[00m" .format('\n'+msg))


def check_root():# checking 
    if os.geteuid() != 0:
        exit(Red("You need to have root privileges to run this script.\n try running with sudo!"))

def check_distro():
    try:
        lsb_id = subprocess.check_output("lsb_release -i", shell=True).decode("utf-8")
        id = lsb_id.split(":")[-1].lower().strip()
    except Exception:
        id = ""
    return id

if __name__ == "__main__":
    check_root()
    if check_distro() == "debian" or "ubuntu":
        pass
    else:
        print(Red("Can't find your distribution type.. this is only for debian based distributions!."))