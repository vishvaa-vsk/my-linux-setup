import os
import time
if os.geteuid() == 0:
    os.system("sudo apt install apt-transport-https curl")
    print("\033[96m {}\033[00m" .format("Wait.. Adding vscode repo!..\n"))
    time.sleep(0.5)
    os.system("curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg")
    time.sleep(0.2)
    os.system("sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/microsoft-archive-keyring.gpg")
    os.system("sudo touch /etc/apt/sources.list.d/vscode.list")
    os.system("echo 'deb [arch=amd64,arm64,armhf signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/repos/vscode stable main' | sudo tee -a vscode.list")
    print("\033[93m {}\033[00m".format("Added vscode repo to system!..\n"))
    time.sleep(0.4)
    os.system("sudo apt-get install apt-transport-https")
    os.system("sudo apt-get update")
    print("\033[93m {}\033[00m".format("Installing vscode!..\n"))
    os.system("sudo apt-get install code")
else:
    exit("\033[91m {}\033[00m" .format("You need to have root privileges to run this script.\n try running with sudo!"))